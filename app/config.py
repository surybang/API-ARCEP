import yaml


def load_config():
    with open("./config.yaml", "r") as f:
        return yaml.safe_load(f)


config = load_config()
DATABASE_PATH = config["database"]["path"]
HOST_PATH = config["api"]["host"]
PORT_PATH = config["api"]["port"]
