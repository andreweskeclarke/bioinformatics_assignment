import ipdb
import numpy as np
import matplotlib.pyplot as plt

results =  {
  'Garbage': [
        0.359357,
        0.345487,
        0.300246 ],
  'Simple Features': [
          0.344599,
          0.422152,
          0.390513 ],
  '+ Physicochemical': [
          0.527414,
          0.625990,
          0.506098 ],
  '+ Single Amino Acids': [
          0.532850,
          0.641846,
          0.537188 ],
  '+ Dipeptide': [
          0.537295,
          0.642724,
          0.583942 ]
}

width = 0.2
ind = np.arange(5)
fig, ax = plt.subplots()
log_regression = list()
gb_trees = list()
knearest_neighbors = list()
labels = ['Garbage', 'Simple Features', '+ Physicochemical', '+ Single Amino Acids', '+ Dipeptide']
for key in labels:
  log_regression.append(results[key][0])
  gb_trees.append(results[key][1])
  knearest_neighbors.append(results[key][2])

opacity = 0.5
log_regression_bars = ax.bar(ind, log_regression, width, color='r', alpha=opacity)
gb_trees_bars = ax.bar(ind+width, gb_trees, width, color='b', alpha=opacity)
knearest_neighbors_bars = ax.bar(ind+2*width, knearest_neighbors, width, color='g', alpha=opacity)

# add some text for labels, title and axes ticks
ax.set_ylabel('Accuracy')
ax.set_title('Accuracy by model and features')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels, rotation=10)

ax.legend((log_regression_bars[0], gb_trees_bars[0], knearest_neighbors_bars[0]), 
          ('Logistic Regression', 'Gradient Boosted Trees', 'K Nearest Neighbor'))
#plt.show()
plt.savefig('report/histogram.png')


