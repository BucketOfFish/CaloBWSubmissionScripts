import h5py as h5
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

path = "/u/sciteam/zhang10/Projects/DNNCalorimeter/SubmissionScripts/BDT/Output/2017-10-19_Downsampled/EleChPi/"

scanPoints = glob.glob(path+"*.txt")
columns=['max_depth','n_estimators','learning_rate','test_accuracy']
accuracies = pd.DataFrame(columns=columns, index=np.arange(0, len(scanPoints)))
for i, scanPoint in enumerate(scanPoints):
    # parse scan point
    parameters = scanPoint.split('/')[-1]
    parameters = parameters.split('_')
    parameters[-1] = parameters[-1][:-4] # remove ".txt"
    parameters = [float(p) for p in parameters]
    # save final test accuracy
    with open(scanPoint) as f:
        for line in f:
            if "ROC" in line:
                accuracy = line.split(' ')[-1]
                parameters.append(accuracy)
    accuracies.loc[i] = parameters

print "Max accuracy:"
print np.amax(accuracies)

accuracies = accuracies.loc[accuracies['learning_rate']==0.5]
accuracies = accuracies[accuracies.columns].astype(float)

test_accuracy = accuracies['test_accuracy']
max_depth = accuracies['max_depth']
n_estimators = accuracies['n_estimators']
accuracy_data = pd.DataFrame({'n_estimators': n_estimators, 'max_depth': max_depth, 'test_accuracy': test_accuracy})
accuracy_data = accuracy_data.pivot('n_estimators', 'max_depth', 'test_accuracy')

# fig = plt.figure(figsize=(10, 8))
fig = plt.figure()
sns.heatmap(accuracy_data, annot=True)
plt.title('Accuracy')
fig.show()
