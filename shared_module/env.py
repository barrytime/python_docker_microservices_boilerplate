import os

from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__))

ENVIRONMENTS = {
    "dev": ".env",
    "docker": ".env.docker",
}


def load_environment():
    current_env = ENVIRONMENTS.get(os.getenv("PROJECT_ENV"))

    dotenv_path = os.path.join(APP_ROOT, current_env or ".env")
    load_dotenv(dotenv_path)
