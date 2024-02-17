import os

ENV = os.environ.get("ENV", "test")


class BaseConfigs:
    ENV = ENV
    PROJECT_NAME = "ignasium public_api"
    ROOT_API_PREFIX = "/ignasium"

    DATABASE_ADDRESS = ""
    DATABASE_SYNC_ADAPTER = "sqlite"
    DATABASE_ASYNC_ADAPTER = "sqlite+aiosqlite"


class TestConfigs(BaseConfigs):
    ...


class DevConfigs(BaseConfigs):
    ...


class StageConfigs(BaseConfigs):
    ...


class ProdConfigs(BaseConfigs):
    ...


def get_configs_closure():
    config_by_env_dict = {
        "test": TestConfigs,
        "develop": DevConfigs,
        "stage": StageConfigs,
        "prod": ProdConfigs,
    }

    def _get_configs():
        return config_by_env_dict[ENV]()

    return _get_configs


configs: BaseConfigs = get_configs_closure()
