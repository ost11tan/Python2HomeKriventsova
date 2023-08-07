import logging
import argparse

logging.basicConfig(level=logging.INFO, filename='home.log', encoding='utf-8')
logger = logging.getLogger(__name__)

def febb(amount:int):
    a, b = 0, 1
    for __ in range(amount):
        yield a
        a, b = b, a + b

def Parser():
    parser = argparse.ArgumentParser(description='Введите количество элементов')
    parser.add_argument('-LEN', type=int , default=0)
    args = parser.parse_args()
    return args.LEN

if __name__ =="__main__":
    LEN=str(Parser())
    if not LEN.isnumeric():
        logger.error(f"{LEN} не является числом")
        raise TypeError
    elif not int(LEN)>0:
        logger.error(f"{LEN} не является положительным  числом ")
        raise ValueError

    else:
        fibList=[]
        for item in febb(int(LEN)):
            fibList.append(item)
        print(fibList)
        logger.info(f"успешно.Последовательность из {LEN} элементов= {fibList}")
