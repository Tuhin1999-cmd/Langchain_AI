import os

from dotenv import load_dotenv


def main():
    load_dotenv()
    print(os.environ.get("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
