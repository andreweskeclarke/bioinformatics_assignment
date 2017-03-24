import ipdb
import copy
import time
import os
import math
import numpy as np
import pandas as pd
import scipy
import collections

from mass_calc import *
from isoelectric_calc import *
from statsmodels.tools import categorical
from sklearn.linear_model import *
from sklearn.ensemble import *
from sklearn.svm import *
from sklearn.neighbors import *
from sklearn.externals import joblib
from Bio import SeqIO
from physicochemical_properties import *

def load_data():
  print('Load data...')
  training_data_files = ['cyto.fasta', 'mito.fasta', 'nucleus.fasta', 'secreted.fasta']
  sequences = list()
  sequence_locs = list()
  for f in training_data_files:
    input_file = os.path.abspath(os.path.join('data',f))
    sequence_location = f.replace('.fasta', '')
    curent_sequences = [str(fasta_record.seq) for fasta_record in SeqIO.parse(open(input_file),'fasta')]
    sequences.extend(curent_sequences)
    sequence_locs.extend([sequence_location] * len(curent_sequences))
  return sequences, sequence_locs


def cv_train_model(model, input, output):
  n_data = input.shape[0]
  indices = np.random.permutation(n_data)
  step_size = math.ceil(n_data / 10)
  accuracies = list()
  for start in range(0, n_data, step_size):
    end = start + step_size
    train_input = np.vstack([input[indices[:start],:], input[indices[end:],:]])
    train_output = np.hstack([output[indices[:start]], output[indices[end:]]])
    validate_input = input[indices[start:end],:]
    validate_output = output[indices[start:end]]
    accuracies.append(train_model(model, train_input, train_output, validate_input, validate_output))
  return sum(accuracies)/len(accuracies)


def train_model(model, train_input, train_output, validate_input, validate_output):
  model.fit(train_input, train_output)
  predictions = model.predict(validate_input)
  accuracy = sum(predictions == validate_output) / predictions.shape[0]
  print(accuracy)
  return accuracy


def generate_features_and_experiments(start, sequences, sequence_locs):
  print('Generate generic features (%f)...' % (time.time() - start))
  data = pd.DataFrame({
    'sequence_len': [len(s) for s in sequences],
    'mass': [calc_mass(s) for s in sequences],
    'locations': sequence_locs,
    'garbage': [np.random.rand() for s in sequences]
    })

  print('Generate physicochemical features (%f)...' % (time.time() - start))
  data, physicochemical_features = add_physicochemical_properties(data, sequences)

  print('Generate single amino acid features (%f)...' % (time.time() - start))
  amino_acid_features = set()
  data['locations'] = data['locations'].astype('category').cat.codes
  for amino_acid, mass in MASSES.items():
    data['percent_%s' % amino_acid] = [percent(amino_acid, s) for s in sequences]
    amino_acid_features.add('percent_%s' % amino_acid)

  print('Generate dipeptide features (%f)...' % (time.time() - start))
  dipeptide_features = set()
  for amino_acid1, mass in MASSES.items():
    for amino_acid2, mass in MASSES.items():
      pair = '%s%s' % (amino_acid1, amino_acid2)
      data['percent_%s' % pair] = [percent(pair, s) for s in sequences]
      dipeptide_features.add('percent_%s' % pair)

  experiments = dict()
  experiments['Garbage input'] = ['garbage']
  input_columns = [ 'sequence_len', 'mass']
  experiments['Simple Features'] = copy.copy(input_columns)
  input_columns.extend(physicochemical_features)
  experiments['Simple Features + Physicochemical'] = copy.copy(input_columns)
  input_columns.extend(amino_acid_features)
  experiments['Simple Features + Physicochemical + Single Amino Acids'] = copy.copy(input_columns)
  input_columns.extend(dipeptide_features)
  experiments['Simple Features + Physicochemical + Single Amino Acids + Dipeptide'] = copy.copy(input_columns)
  return experiments, input_columns, data

if __name__ == '__main__':
  start = time.time()
  sequences, sequence_locs = load_data()
  experiments, input_columns, data = generate_features_and_experiments(start, sequences, sequence_locs)

  for experiment_key in [sorted(experiments)[-1]]:
    print('Run experiment with: %s (%f)' % (experiment_key, time.time() - start))
    experiment_columns = experiments[experiment_key]
    input = data.as_matrix(experiment_columns)
    output = np.squeeze(data.as_matrix(['locations']))

    print('\tTrain Logistic Regression model...')
    model = LogisticRegressionCV(multi_class='multinomial')
    accuracy = cv_train_model(model, input, output)
    print('\tAccuracy: %f (%fs)' % (accuracy, time.time() - start))

    print('\tTrain Gradient Boosting Classifier model...')
    model = GradientBoostingClassifier(max_depth=4)
    accuracy = cv_train_model(model, input, output)
    print('\tAccuracy: %f (%fs)' % (accuracy, time.time() - start))
    with open(os.path.join('models', 'gb_model'), 'wb') as f:
      joblib.dump(model, f)

    print('\tTrain K-Nearest Neighbors model...')
    model = KNeighborsClassifier(n_neighbors=3, metric='canberra')
    accuracy = cv_train_model(model, input, output)
    print('\tAccuracy: %f (%fs)' % (accuracy, time.time() - start))

  print('Done! (%f)' % (time.time() - start))
