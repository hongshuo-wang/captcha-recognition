from enum import Enum

class MyConfig(Enum):
    # MODEL
    MODEL = "models/model.pth"
    MODEL_SAVE = "models/model.pth"

    # DATASETS
    DATASETS_TRAIN = "datasets/train/"
    DATASETS_TEST = "datasets/test/"
    DATASETS_VALIDATE = "datasets/validate/"

    # LOGS
    LOGS = "logs/log"



