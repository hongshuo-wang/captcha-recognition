import torch
from torch import nn
import common

# Batch Normalization强行将数据拉回到均值为0，方差为1的正太分布上，一方面使得数据分布一致，另一方面避免梯度消失。

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU()
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU()
        )
        self.layer3 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU()
        )
        self.layer4 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU()
        )
        self.layer5 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU()
        )
        self.layer6 = nn.Sequential(
            nn.Conv2d(in_channels=512, out_channels=1024, kernel_size=3, padding=1),
            nn.BatchNorm2d(1024),
            nn.ReLU()
        )
        self.layer7 = nn.Sequential(
            nn.Flatten(),
            nn.BatchNorm1d(5120),
            nn.Linear(in_features=5120, out_features=4096),
            nn.Dropout(0.5),
            nn.ReLU(),
            nn.Linear(in_features=4096, out_features=common.captcha_size*len(common.captcha_array))
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        x = self.layer6(x)
        x = self.layer7(x)
        return x

if __name__ == "__main__":
    data = torch.ones(64, 3, 60, 160)
    model = MyModel()
    x = model(data)
    print(x.shape)