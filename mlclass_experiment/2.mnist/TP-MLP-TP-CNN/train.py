import time
import copy
import torch
import torchvision
import torchvision.transforms as transforms

import numpy as np

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def train_proc(model, dataloaders, model_param, train_param, debug=True):
	nn = model(**model_param).to(DEVICE)

	criterion = train_param["cost_func"]
	optimizer = train_param["optimizer"](nn.parameters(), **train_param["opt_param"])

	trainloader = dataloaders["train"]
	validationloader = dataloaders["validation"]
	testloader = dataloaders["test"]

	best_val_loss = np.inf
	best_epoch = -1
	best_model = None
	accuracy = None

	running_loss = 0
	nb_used_sample = 0

	nEpochs = train_param["max_epochs"]

	# Train on the entire dataset for N epochs
	for epoch in range(nEpochs):
		start_time = time.time()
		for i, data in enumerate(trainloader, 0):
			# get the inputs
			inputs, labels = data
			inputs, labels = inputs.to(DEVICE), labels.to(DEVICE) # if possible, move them to GPU

			# set to zeros gradient of model's parameter
			optimizer.zero_grad()

			# forward pass
			outputs = nn(inputs)
			# compute loss
			loss = criterion(outputs, labels)
			# backward pass
			loss.backward()
			# optimize model's parameters
			optimizer.step()

			# count how many samples have been used during the training
			nb_used_sample += len(inputs)

			running_loss += loss.item()

			# print/save statistics (every 1000 samples)
			if nb_used_sample % (1e3) == 0:
				train_err = (running_loss / (1000 * len(inputs)))
				print("{}Epoch {:d} batch {:d}".format(" "*2, epoch + 1, i + 1))
				print("{}Train loss : {:.3f}".format(" "*4, train_err))

				running_loss = 0

				#evaluation on validation set
				val_loss = 0
				# no_grad means that no gradient will be computed on the validation passes
				with torch.no_grad():
					val_accuracy = 0
					nVal_samples = 0
					for data in validationloader:
						images, labels = data
						images, labels = images.to(DEVICE), labels.to(DEVICE)
						outputs = nn(images)
						loss = criterion(outputs, labels)
						val_loss += loss.item()

						val_accuracy += torch.eq(torch.argmax(outputs, dim=1), labels).sum().item()
						nVal_samples += len(labels)

				val_err = val_loss / nVal_samples
				val_accuracy = val_accuracy / nVal_samples

				print("{}Validation loss mean : {:.3f}".format(" "*4, val_err))
				print("{}Validation accuracy mean : {:.3%}".format(" "*4, val_accuracy))

				# save the model only when loss is better
				if best_val_loss > val_loss:
					best_val_loss = val_loss
					best_model =  copy.deepcopy(nn)
					best_epoch = epoch+1
					accuracy = val_accuracy

		print("{}Epoch {} of {} took {:.3f}s\n".format(" "*2, epoch + 1, nEpochs, time.time() - start_time))

	return best_epoch, accuracy, best_val_loss, best_model
