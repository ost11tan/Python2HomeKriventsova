#Задание №6
#Напишите программу банкомат.
#✔ Начальная сумма равна нулю
#✔ Допустимые действия: пополнить, снять, выйти
#✔ Сумма пополнения и снятия кратны 50 у.е.
#✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
#✔ Нельзя снять больше, чем на счёте
#✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#операцией, даже ошибочной
#✔ Любое действие выводит сумму денег

global MULT
MULT=50
global MIN_CASH
MIN_CASH=30
global MAX_CASH
MAX_CASH=600
global MAX_COUNT
MAX_COUNT=3
global PERSENT
PERSENT=0.015
global EXTRA_PERSENT
EXTRA_PERSENT=0.03
global RICH_PERSENT
RICH_PERSENT=0.1
global MAX_SCORE
MAX_SCORE=5_000_000
COUNT = 0
SCORE=0
def main():
    global SCORE

    bank_q=bank()
    while bank_q!=0:
        bank()
        bank_q = bank()
    if bank_q==0:
        print("сумма= "+str(SCORE))


def bank():
    flag=1

    global SCORE
    tmp_score=SCORE
    global COUNT
    COUNT+=1
    print("Операция №: "+ str(COUNT))
    tmp_score=Million(tmp_score)
    operation = question()

    if operation == "1":
        cash = cash_check()
        SCORE=add_cash(cash,tmp_score,COUNT)
        flag=1

    elif operation == "2":
        cash = cash_check()
        SCORE=give_cash(cash,SCORE,COUNT)
        flag=1
    elif operation == "3":
        flag=0
    else:
        print("Введите 1,2 или 3")
        bank()
    return flag

def question():
    operation = input("Введите номер действия 1-пополнить, 2-снять, 3-выйти: ")
    return operation

def give_cash(cash,score,count):
    persent=give_cash_persent(cash)
    flag=proverka(cash,score,persent)
    if count%MAX_COUNT==0:
        tmp=score*EXTRA_PERSENT
        score_new=score+tmp
        minus=cash+persent
        score=score_new-minus

    else:
        score = score - cash-persent

    print(score)
    return score
def give_cash_persent(cash):
    tmp_persent=cash*PERSENT
    if tmp_persent<=MIN_CASH:
        persent=MIN_CASH
    elif tmp_persent>=MAX_CASH:
        persent=MAX_CASH
    else:
        persent=tmp_persent
    return persent

def add_cash(cash,score,count):
    if count%MAX_COUNT==0:
        tmp=score*EXTRA_PERSENT
        score=score+tmp+cash
    else:
        score = score + cash

    print(score)
    return score


def cash_check():
    temp=int(input("Введите сумму: "))
    if temp%MULT==0:
        cash=temp
    else:
        print("Сумма должна быть кратна 50! ")
        cash_check()
    return cash
def Million(score):
    if score>MAX_SCORE:
        tmp=score-(score*RICH_PERSENT)
    else:
        tmp=score
    return tmp

def proverka(cash,score,persent):
    if score< (cash+persent):
        print("Нельзя снять больше,чем на карте!")
        global COUNT
        COUNT=COUNT-1
        bank()
    else:
        return True
