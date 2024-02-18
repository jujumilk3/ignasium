import os

ENV = os.environ.get("ENV", "test")


class BaseConfigs:
    ENV = ENV
    PROJECT_NAME = "ignasium public_api"
    ROOT_API_PREFIX = "ignasium"

    DATABASE_ADDRESS = ""
    DATABASE_SYNC_ADAPTER = "sqlite"
    DATABASE_ASYNC_ADAPTER = "sqlite+aiosqlite"

    CORS_ALLOW_ORIGINS = [
        "*",
    ]


class TestConfigs(BaseConfigs):
    ...


class DevConfigs(BaseConfigs):
    ...


class StageConfigs(BaseConfigs):
    ...


class ProdConfigs(BaseConfigs):
    ...


# def get_configs_closure():
#     config_by_env_dict = {
#         "test": TestConfigs,
#         "develop": DevConfigs,
#         "stage": StageConfigs,
#         "prod": ProdConfigs,
#     }

#     def _get_configs():
#         print("asd")
#         return config_by_env_dict[ENV]()

#     return _get_configs


# configs: BaseConfigs = get_configs_closure()()

if ENV == "test":
    configs = TestConfigs
elif ENV == "develop":
    configs = DevConfigs
elif ENV == "stage":
    configs = StageConfigs
elif ENV == "prod":
    configs = ProdConfigs
else:
    raise ValueError("Unknown ENV")


if __name__ == "__main__":
    print(configs)
