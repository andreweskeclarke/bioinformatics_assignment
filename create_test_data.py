import os
import time
import numpy as np

from sklearn.externals import joblib
from sklearn.ensemble import *
from train import *
from confusion_matrix import *
from Bio import SeqIO

# Plot confusion matrices
start = time.time()
sequences, sequence_locs = load_data()
experiments, input_columns, data = generate_features_and_experiments(start, sequences, sequence_locs)
experiment_columns = experiments['Simple Features + Physicochemical + Single Amino Acids + Dipeptide']
categories = ['Cyto', 'Mito', 'Nucl', 'Secr']
indices = np.random.permutation(data.shape[0])
input = data.as_matrix(experiment_columns)
output = np.squeeze(data.as_matrix(['locations']))
model = GradientBoostingClassifier(max_depth=4)
model.fit(input[indices], output[indices])

input_file = os.path.abspath(os.path.join('data','blind.fasta'))
test_seq_no = [str(fasta_record.id) for fasta_record in SeqIO.parse(open(input_file),'fasta')]
test_sequences = [str(fasta_record.seq) for fasta_record in SeqIO.parse(open(input_file),'fasta')]
test_experiments, test_input_columns, test_data = generate_features_and_experiments(start, test_sequences, ['blind']*len(test_sequences))
test_columns = test_experiments['Simple Features + Physicochemical + Single Amino Acids + Dipeptide']
test_input = test_data.as_matrix(test_columns)
predictions = model.predict(test_input)
probabilities = model.predict_proba(test_input)
for i in range(0, len(predictions)):
  print('%s %s Confidence %s%%' % (test_seq_no[i], categories[predictions[i]], '{:.0f}'.format(100*np.max(probabilities[i]))))

