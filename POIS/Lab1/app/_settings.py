from dotenv import load_dotenv


ENV_STATE_FILE = "LAB_STATE_FILE"

def load_settings(path: str) -> None:
    load_dotenv(dotenv_path=path)
