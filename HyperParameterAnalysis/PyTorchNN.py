import h5py as h5
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

path = "/u/sciteam/zhang10/Projects/DNNCalorimeter/SubmissionScripts/PyTorchNN/Output/2017-10-19_Downsampled/EleChPi/"

scanPoints = glob.glob(path+"*")
columns=['learning_rate','decay_rate','dropout_prob','hidden_layer_neurons','n_hidden_layers','test_accuracy']
accuracies = pd.DataFrame(columns=columns, index=np.arange(0, len(scanPoints)))
for i, scanPoint in enumerate(scanPoints):
    # parse scan point
    parameters = scanPoint.split('/')[-1]
    parameters = parameters.split('_')
    parameters = [float(p) for p in parameters]
    # save final test accuracy
    data = h5.File(scanPoint+"/Results.h5")
    parameters.append(data['test_accuracy'][0])
    accuracies.loc[i] = parameters

print "Max accuracy:"
print np.amax(accuracies)

accuracies = accuracies.loc[accuracies['learning_rate']==0.001].loc[accuracies['decay_rate']==0.01].loc[accuracies['dropout_prob']==0]
accuracies = accuracies[accuracies.columns].astype(float)

test_accuracy = accuracies['test_accuracy']
nhl = accuracies['n_hidden_layers']
hln = accuracies['hidden_layer_neurons']
accuracy_data = pd.DataFrame({'n_hidden_layers': nhl, 'neurons_per_hidden_layer': hln, 'test_accuracy': test_accuracy})
accuracy_data = accuracy_data.pivot('neurons_per_hidden_layer', 'n_hidden_layers', 'test_accuracy')

# fig = plt.figure(figsize=(10, 8))
fig = plt.figure()
sns.heatmap(accuracy_data, annot=True)
plt.title('Accuracy (%)')
fig.show()
