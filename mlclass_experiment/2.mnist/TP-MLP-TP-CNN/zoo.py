import torch.nn as nn
import torch.nn.functional as F

class MLP_class(nn.Module):
    def __init__(self, nClass=10, nHidden=100):
        super(MLP_class, self).__init__()
        self.fc1 = nn.Linear(32 * 32 , nHidden)
        self.fc2 = nn.Linear(nHidden, nClass)

    def forward(self, x):
        x = x.view(-1, 32 * 32)
        x = F.relu(self.fc1(x))
        x = F.softmax(self.fc2(x), dim=1)
        return x

class MLP_AE(nn.Module):
    def __init__(self, nHidden=100):
        super(MLP_AE, self).__init__()
        self.fc1 = nn.Linear(32 * 32 , nHidden)
        self.fc2 = nn.Linear(nHidden, 32 * 32)

    def forward(self, x):
        x = x.view(-1, 32 * 32)
        x = F.elu(self.fc1(x))
        x = F.elu(self.fc2(x))
        x = x.view(-1, 32, 32)

        return x

class CNN_class(nn.Module):
    def __init__(self, hiddenCells = 100):
        super(CNN_class, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.conv2 = nn.Conv2d(32,64, 5)
        self.conv3 = nn.Conv2d(16, 32, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear( 64 * 5 * 5, 1024)
        self.fc2 = nn.Linear(1024, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        #print('x形状1:',x.shape)#[64, 6, 14, 14]
        x = self.pool(F.relu(self.conv2(x)))
        #print('x形状2:',x.shape)#[64, 64, 5, 5]

        x = x.view(-1, 64 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.softmax(self.fc2(x), dim=1)
        return x