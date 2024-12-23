import os
from shared_module.module2 import farewell
from shared_module.env import load_environment
from dotenv import load_dotenv

load_dotenv()


def main():
    name = "Alice"
    message = farewell(name)
    print(message)


if __name__ == "__main__":
    main()
    print(os.getenv("TEST"))
