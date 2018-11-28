from train import train_proc

import numpy as np

def crossval_proc(nRun, model, dataloaders, model_param, train_param):

	model_logs = []

	for iRun in range(nRun):
		print("Run {:>4}/{}".format(iRun+1, nRun))
		nn_epochs, nn_acc, nn_loss, nn_best = train_proc(model, dataloaders, model_param, train_param)

		model_logs.append({"nE": nn_epochs, "acc": nn_acc,
						   "nL": nn_loss, "model": nn_best})

	# Retrieve accuracy of each model
	accuracies = [v["acc"] for v in model_logs]
	# Retrieve best epoch of each model
	epochs = [v["nE"] for v in model_logs]

	# Get index of models with the highest accuracy
	best_model_idx = np.argmax(accuracies)
	# Get best model
	best_model = model_logs[best_model_idx]["model"]
	# Add some properties to the model class
	setattr(best_model, "iRun", best_model_idx)
	setattr(best_model, "nEpoch", model_logs[best_model_idx]["nE"])
	setattr(best_model, "accuracy", model_logs[best_model_idx]["acc"])

	return accuracies, best_model, epochs