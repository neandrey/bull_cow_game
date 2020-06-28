import random

def notRepeatRandomNumber(L1: list, num: int) -> bool:
    """Проверка повторяющихся значений в числе"""
    for i in L1:
        if i == num:
            return False
    return True


def notRepeatInputNumber(L1: list) -> bool:
    """Проверка повтора числа в воде пользователя"""
    while L1:
        num = L1[:1]
        L1 = L1[1:]
        for h in L1:
            if h == num:
                return False
    return True


def randomNumber():
    """программа загадывает 4-x значное число Без повторов!!!"""
    #randList = [random.randint(0, 9) for num in range(0, 4)]
    randList = []
    Flag = False
    randList.append(random.randint(0, 9))
    while True:
        Flag = True
        randNum = random.randint(0, 9)
        # for i in randList:
        #     if i == randNum:
        #         Flag = False
        Flag = notRepeatRandomNumber(randList, randNum)

        if Flag:
            randList.append(randNum)

        if len(randList) == 4:
            break

    print('программа загадала 4-x значное число')
    #print(randList)
    return randList

def inputData():
    """ввод данных"""
    strNumber = input('введите 4-х значаное число или х для выхода: ')
    #print(strNumber)
    return strNumber

def inputCorrect(strInput):
    """проверка данных на корректность"""
    Flag = True
    if len(strInput) != 4 and not (strInput.isdigit()):
        print("Длина числа не соответствует 4-м и сторока состоит не только из цифр.")
        Flag = False

    elif len(strInput) != 4:
        print("Длин числа не соответствует 4-м.")
        Flag = False

    elif not strInput.isdigit():
        print("Строка состоит не только из цифр")
        Flag = False

    elif not notRepeatInputNumber(strInput):
        print("Строка имеет повторяющиеся значения в числе ввода")
        Flag = False

    return Flag


def strToList(strInput):
    """строка в текст"""
    userList = []
    for n in strInput:
        userList.append(int(n))
    return userList


def bullCow(randNum, inputNum):
    """подсчет коров и быков"""
    cow, bull = 0, 0
    tempRandNum = randNum[:] #создаем клон переменной
    removeBull = [];

    if tempRandNum == inputNum:
        print("Вы угадали число")
        return True
    #счетаем число быков:
    for i in  range(0, 4):
        if tempRandNum[i] == inputNum[i]:
            removeBull.append(i);
            bull += 1
            #print("removedBull ", removeBull)
    #удаляем быков
    if(bull != 0):
        lengthBull = len(removeBull)
        while lengthBull:
            delIndex = removeBull.pop()
            del tempRandNum[delIndex]
            del inputNum[delIndex]
            lengthBull -= 1;
    #счетаем коров
    for g in tempRandNum:
        for h in inputNum:
            if h == g:
                cow += 1;

    print("{} бык., {} кор.".format(bull, cow))
    return False

def main():
    #Основное тело программв
    #1 `игра загадывает число
    randNum = randomNumber()
    #Для ведения статистики
    #statistGame = dict();
    # бесконечный цикл
    while True:
        #услови для выхода
        strInput = inputData()
        if strInput== 'x':
            print("игра окончена")
            break
        if not inputCorrect(strInput):
            continue
        listInput = strToList(strInput)
        endGame = bullCow(randNum, listInput)
        if endGame:
            print("игра закончена!")
            break

    
if __name__ == "__main__":
    main()

    assert main()
