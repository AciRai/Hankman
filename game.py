import random
import os
from time import sleep

# Отступы  ##########################

ots1 = '---------------------\n'
ots2 = '\n---------------------'

# Меню  #############################
clear = lambda: os.system('clear')

print(ots1, "Выберите сложность:", ots2)
dific = input("\n1. Легко \n2. Нормально \n3. Сложно \n4. HAHAHAHAHAHAHAHA...\n")
if dific == "1": attempt = 20
elif dific == "2": attempt = 10
elif dific == "3": attempt = 5
elif dific == "4": attempt = 1
print(ots1, "Чтобы выйти из игры напишите - exit\n\nБонусы:\nЧтобы использовать аптечку напишите - health", ots2)
###############
usedln = ""
win = []
# Список  #####################
with open('wordsgame.txt', 'r') as w:
    for i in w:
        openFile = open(w)
        listFile = list(openFile)
        randomWord = random.choice(listFile)

d1 = "".join(c for c in randomWord if c.isalpha())
randomWord = randomWord.rstrip('\n')
d1 = randomWord
d2 = len(d1)
print("слово: ", d1)
# диапозон ##########
for i in range(len(randomWord)):
    win += "_"

iAttemts = True
while d2 != 0 and attempt != 0:
    test = False
# Введите слово ##############
    while True:
        let = input("Введите букву ")
# Выход из игры ##############
        if let == "exit":
            clear()
            print(ots1, "Вы успешно ВЫШЛИ из игры.", ots2)
            sleep(1)
            clear()
            quit()
# Аптечка ########################
        if let == "health":
            clear()
            if iAttemts == True:
                print(ots1, "Вы использовали аптечку!!!", ots2)
                attempt += 3
                iAttemts = False
            elif iAttemts == False:
                print(ots1, "Вы УЖЕ использовали аптечку!!!", ots2)
# Символы  ########################
        if let != "health":
            if let in usedln or len(let) > 1:
                clear()
                print("Не больше одного символа, попробуйте снова!\nИспользованные буквы:", ' , '.join(usedln),ots2)
            else:
                usedln += let
                break
# Попытки  ########################
    count = 0

    for i in randomWord:
        if let in i:
            d2 -= 1
            test = True
            win[count] = let
        count += 1

    clear()

    if not test:
        attempt -= 1
        print(ots1, "Неверно\nИспользованные буквы:", ' , '.join(usedln), ots2)
        win1 = ' '.join(win)
        print('[', win1, ']')
    else:
        win1 = ' '.join(win)
        print(ots1, "Верно\nИспользованные буквы:", ' , '.join(usedln), ots2)
        print('[', win1, ']')
    print("Ваше здоровье = ", attempt)
if(d2 == 0):
    clear()
    print(ots1,"ВЫ ПОБЕДИЛИ!!! \n Слово было", d1.upper(), ots2)
    sleep(1)
else:
    clear()
    print(ots1,"ВЫ ПРОИГРАЛИ! ПОПРОБУЙТЕ СНОВА!", "\n слово было: ", d1.upper(), ots2)
    sleep(1)
