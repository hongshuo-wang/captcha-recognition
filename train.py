import os
# os.environ["CUDA_VISIBLE_DEVICES"] = '1' 
from mydataset import my_dataset
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torch import nn
from model import MyModel
from torch.optim import Adam
from predict import detect_accuracy
import torch
import time
from config import MyConfig

if __name__ == "__main__":
    train_dataset = my_dataset(MyConfig.DATASETS_TRAIN.value)
    train_dataloader = DataLoader(train_dataset, batch_size=128, shuffle=True)

    writer = SummaryWriter(MyConfig.LOGS.value)
    myModel = torch.load(MyConfig.MODEL.value).cuda()
    loss_fn = nn.MultiLabelSoftMarginLoss().cuda()  # 多标签交叉熵损失
    optim = Adam(myModel.parameters(), lr=0.001)  # 学习率

    total_step = 0
    start = time.time()   # 开始时间
    for epoch in range(1):
        for i, (images, lables) in enumerate(train_dataloader):
            myModel.train()
            images = images.cuda()
            lables = lables.cuda()
            outputs = myModel(images)  # 前向传播
            loss = loss_fn(outputs, lables)  # 计算损失
            optim.zero_grad()
            loss.backward()   # 反向传播
            optim.step()
            total_step += 1
            if i % 500 == 0:
                torch.save(myModel, MyConfig.MODEL_SAVE.value)
                accuracy = detect_accuracy(MyConfig.DATASETS_TEST.value)
                writer.add_scalar('loss', loss, total_step)
                writer.add_scalar('accuracy', accuracy, total_step)
                writer.add_graph(myModel, (images, ))
                print("epoch[{}]---训练次数[{}]---损失值[{}]---正确率[{}%]".format(epoch, i, loss.item(), accuracy))
    elapsed = (time.time() - start)
    print("训练用时：{}分钟".format(elapsed // 60))
