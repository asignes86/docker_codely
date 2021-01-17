from loguru import logger
from time import sleep


def print_hi(name):
    while True:
        print(f'Holaaaaa, {name}')
        logger.info("Sleep 😴")
        sleep(3)


if __name__ == '__main__':
    print_hi('PyCharm')
