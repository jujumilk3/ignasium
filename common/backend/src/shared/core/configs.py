import os
import pathlib


class BaseConfig:
    # Base Config
    PROJECT_NAME = "ignasium"
    PROJECT_ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent.parent.parent.parent.parent
    CRONJOBS_DIR = PROJECT_ROOT_DIR.joinpath("projects").joinpath("cronjobs")


configs = BaseConfig()

if __name__ == "__main__":
    print(configs.PROJECT_ROOT_DIR)
    print(configs.CRONJOBS_DIR)
