"""Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список."""





"""Используем int тк есть условие кратности 50"""


import decimal
def bank()->bool:
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
        print(f"Ваши операции:{operations}")
        flag=0
    else:
        print("Введите 1,2 или 3")
        bank()
    return flag

def question()->int:
    operation = input("Введите номер действия 1-пополнить, 2-снять, 3-выйти: ")
    return operation

def give_cash(cash:decimal,score:decimal,count:int)->decimal:
    global operations
    persent=give_cash_persent(cash)
    flag=proverka(cash,score,persent)
    if count%MAX_COUNT==0:
        tmp=score*EXTRA_PERSENT
        score_new=score+tmp
        minus=cash+persent
        score=score_new-minus
        operations.append(f"-{cash}")
    else:
        score = score - cash-persent
        operations.append(f"-{cash}")

    print(score)
    return score
def give_cash_persent(cash:decimal)->decimal:
    tmp_persent=cash*PERSENT
    if tmp_persent<=MIN_CASH:
        persent=MIN_CASH
    elif tmp_persent>=MAX_CASH:
        persent=MAX_CASH
    else:
        persent=tmp_persent
    return persent

def add_cash(cash:decimal,score:decimal,count:int)->decimal:
    global operations
    if count%MAX_COUNT==0:
        tmp=score*EXTRA_PERSENT
        score=score+tmp+cash
        operations.append(f"+{cash}")
    else:
        score = score + cash
        operations.append(f"+{cash}")

    print(score)
    return score

def cash_check()->decimal:
    while True:
        temp=int(input("Введите сумму: "))
        if not temp%MULT==0:
            print("Сумма должна быть кратна 50! ")
        else:
            cash=temp
            break
    return cash

def Million(score:decimal)->decimal:
    if score>MAX_SCORE:
        tmp=score-(score*RICH_PERSENT)
    else:
        tmp=score
    return tmp

def proverka(cash:decimal,score:int,persent:decimal)->bool:
    if score< (cash+persent):
        print("Нельзя снять больше,чем на карте!")
        global COUNT
        COUNT=COUNT-1
        bank()
    else:
        return True


if __name__=='__main__':
    global MULT
    MULT = 50
    global MIN_CASH
    MIN_CASH = 30
    global MAX_CASH
    MAX_CASH = 600
    global MAX_COUNT
    MAX_COUNT = 3
    global PERSENT
    PERSENT = 0.015
    global EXTRA_PERSENT
    EXTRA_PERSENT = 0.03
    global RICH_PERSENT
    RICH_PERSENT = 0.1
    global MAX_SCORE
    MAX_SCORE = 5_000_000
    COUNT = 0
    global SCORE
    SCORE = 0
    global operations
    operations=[]



    bank_q = bank()
    while bank_q != 0:
        bank()
        bank_q = bank()
    if bank_q == 0:
        print("сумма= " + str(SCORE))