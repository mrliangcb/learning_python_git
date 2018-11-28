import torch
import torchvision
import torchvision.transforms as transforms


def loadData(minibatchsize):
	transform = transforms.Compose(
	    [transforms.Pad(2),
	     transforms.ToTensor(),
	     transforms.Normalize((0.5,), (0.5,))])

	fulltrainset = torchvision.datasets.MNIST(root='./data', train=True,
	                                        download=True, transform=transform)

	#split the full train part as train and validation (10K samples, some can be ignored):
	trainset, validationset, _ignored_part = torch.utils.data.random_split(fulltrainset, [20000,10000, 30000])

	trainloader = torch.utils.data.DataLoader(trainset, batch_size=minibatchsize,
	                                          shuffle=True, num_workers=0)

	validationloader = torch.utils.data.DataLoader(validationset, batch_size=minibatchsize,
	                                          shuffle=False, num_workers=0)

	testset = torchvision.datasets.MNIST(root='./data', train=False,
	                                       download=True, transform=transform)
	testloader = torch.utils.data.DataLoader(testset, batch_size=minibatchsize,
	                                         shuffle=False, num_workers=0)

	return {"train": trainloader, "validation": validationloader, "test": testloader}