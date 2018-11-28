
"""
Load data
Load NN
loops
	crossval
output mean/sd
save best model parameters
"""

import torch
import zoo

import numpy as np

from dataset import loadData
from crossvalidation import crossval_proc

minibatchsize = 64
NcrossVal = 5

# trainloader, validationloader, testloader
dataloaders = loadData(minibatchsize)

nn = zoo.CNN_class

model_param = {
	#"nClass": 10,
	"hiddenCells": 25
}

train_param = {
	# Adam optimizer
	# "optimizer": torch.optim.Adam,
	# "opt_param": {"lr": 0.001},

	# Stochastic Gradient Descent Optimizer
	"optimizer": torch.optim.SGD,
	"opt_param": {"lr": 0.001, "momentum": 0.9},

	"cost_func": torch.nn.CrossEntropyLoss(),

	"max_epochs": 5,
}

accuracies, best, epochs = crossval_proc(NcrossVal, nn, dataloaders, model_param, train_param)

print("""\nModel {} was trained successfuly on {} runs ({} per run).
Mean accuracy is {:.2%} (standard deviation: {:.2%}).
Early-stopping: average per run is epoch {:.0f} (std: {:.2f}).
The model reached its peak accuracy on run {} at epoch {}: {:.2%}.
""".format(
	nn.__class__.__name__, NcrossVal, train_param["max_epochs"],
	np.mean(accuracies), np.std(accuracies),
	np.mean(epochs), np.std(epochs),
	best.iRun+1, best.nEpoch, best.accuracy
	))

# run best model on test dataset