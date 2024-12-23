from dotenv import load_dotenv
from shared_module.module1 import greet
from shared_module.env import load_environment

load_dotenv()


def main():
    name = "Alice"
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
