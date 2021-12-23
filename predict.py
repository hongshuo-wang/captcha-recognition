import os
# os.environ["CUDA_VISIBLE_DEVICES"] = '1' 
from torch.utils.data import DataLoader
from mydataset import my_dataset
import onehot
import torch
import common
from model import MyModel
from PIL import Image
from torchvision import transforms
from prehandle import prehandle
from config import MyConfig

def detect_accuracy(path):
    test_dataset = my_dataset(path)
    test_dataloader = DataLoader(test_dataset, batch_size=1, shuffle=True)
    # model = torch.load("model.pth")
    # model = torch.load("models/model.pth").cuda()
    model = torch.load(MyConfig.MODEL.value).cuda()


    correct = 0
    test_len = len(test_dataset)
    model.eval()
    for i, (images, labels) in enumerate(test_dataloader):
        images = images.cuda()
        labels = labels.cuda()
        labels = labels.view(-1, len(common.captcha_array))
        # print(labels.shape)     # torch.Size([4, 36])
        label_text = onehot.vec2Text(labels)
        output = model(images)  # 预测
        output = output.view(-1, len(common.captcha_array))
        # print(output.shape)     # torch.Size([4, 36])
        output_text = onehot.vec2Text(output)
        if label_text == output_text:
            correct += 1
            # print("正确值：{}  预测值:{}".format(label_text, output_text))
    return correct / test_len * 100

def detect_single(path):
    image = Image.open(path)
    trans = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((60, 160))
    ])
    image_tensor = trans(image).cuda()
    image_tensor = image_tensor.reshape((1, 3, 60, 160))
    # m = torch.load("captcha/model.pth").cuda()
    # m = torch.load("models/model.pth").cuda()
    m = torch.load(MyConfig.MODEL.value).cuda()
    m.eval()
    output = m(image_tensor)
    output = output.view(-1, len(common.captcha_array))
    output_label = onehot.vec2Text(output)
    print("预测结果：", output_label)


if __name__ == "__main__":
    result = detect_accuracy("datasets/test/")
    print(result)
    # detect_single("captcha/datasets/test/0qbk_1640146200.png")
    # detect_single("datasets/validate/1GKS_1640249598.png")

