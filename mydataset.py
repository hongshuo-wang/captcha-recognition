import os
import onehot

from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter
from prehandle import prehandle


class my_dataset(Dataset):
    def __init__(self, root_dir):
        super(my_dataset, self).__init__()
        self.image_path = [os.path.join(root_dir, image_name) for image_name in os.listdir(root_dir)]
        self.transforms = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Resize((60, 160))
            ]
        )

    def __len__(self):
        return self.image_path.__len__()

    def __getitem__(self, index):
        image_path = self.image_path[index]
        image = self.transforms(Image.open(image_path))
        label = image_path.split("/")[-1]  # captcha/datasets/train/012r_2342934729.png
        label = label.split("_")[0]    # 012r
        label_tensor = onehot.text2Vec(label)
        label_tensor = label_tensor.view(1, -1)[0]  # 把4行62列的数组变成1行248列的数组
        return image, label_tensor

if __name__ == "__main__":
    writer = SummaryWriter("logs/log")
    train_data = my_dataset("datasets/train/")
    image, label = train_data[0]
    print(label)
    writer.add_image("image", image, 1)
    writer.close()
