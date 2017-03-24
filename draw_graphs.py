import os
import time
import numpy as np

from sklearn.externals import joblib
from sklearn.ensemble import *
from train import *
from confusion_matrix import *

# Plot confusion matrices
start = time.time()
sequences, sequence_locs = load_data()
experiments, input_columns, data = generate_features_and_experiments(start, sequences, sequence_locs)
experiment_columns = experiments['Simple Features + Physicochemical + Single Amino Acids + Dipeptide']

indices = np.random.permutation(data.shape[0])
input = data.as_matrix(experiment_columns)
output = np.squeeze(data.as_matrix(['locations']))

start = 5000
end = 6000
train_input = np.vstack([input[indices[:start],:], input[indices[end:],:]])
train_output = np.hstack([output[indices[:start]], output[indices[end:]]])
validate_input = input[indices[start:end],:]
validate_output = output[indices[start:end]]

class_names = ['cyto', 'mito', 'nucleus', 'secreted']
model = joblib.load(os.path.join('models', 'gb_model'))
model = GradientBoostingClassifier(max_depth=4)
model.fit(train_input, train_output)
predictions = model.predict(validate_input)
print('Accuracy: %f (%f)' % (sum(predictions == validate_output) / predictions.shape[0], time.time() - start))
confusion_matrix_display(validate_output, predictions, class_names, 'Gradient Boosting Trees', 'report/confusion.png')
