import random
intel = 0
harizma = 0
znania = 0
sila = 100
dney = 7
dostizhenie_gambler = False
print("Дарова! Это игра про сессию")
print("Готовься 7 дней")
while dney > 0:
    print(f"\n=== День {8-dney} ===")
    print(f"Интеллект: {intel}")
    print(f"Харизма: {harizma}") 
    print(f"Знания: {znania}")
    print(f"Силы: {sila}")   
    if sila < 20:
        print("Устал, значит на боковую на день")
        sila = 100
        dney = dney - 1
        continue
    deistvie = input("Выбирай\n1 - учить один предмет\n2 - учить все понемногу\n")
    if deistvie == "1":
        kakoi = input("Какой?\n1 - интеллект\n2 - харизма\n3 - знания\n")
        if kakoi == "1":
            intel = intel + 25
            if intel > 100:
                intel = 100
            print("Красава поумнел")
        elif kakoi == "2":
            harizma = harizma + 25
            if harizma > 100:
                harizma = 100
            print("+ харизма")
        elif kakoi == "3":
            znania = znania + 25
            if znania > 100:
                znania = 100
            print("Выучил что-то")
        sila = sila - 20
    elif deistvie == "2":
        intel = intel + 10
        harizma = harizma + 10
        znania = znania + 10
        if intel > 100:
            intel = 100
        if harizma > 100:
            harizma = 100
        if znania > 100:
            znania = 100
        print("Все понемногу подучил")
        sila = sila - 25  
    else:
        print("ЧЁ ТЫ КОД МНЕ ЛОМАЕШЬ, НАКАЗАНИЕ(ПРОПУСК ДЕНЬ)")
    dney = dney - 1
print("СЕССИЯ(СМЕРТЬ)")
shans_znania = (znania // 25) * 23
shans_harizma = (harizma // 25) * 7
ispolzovan_harizma = False
if shans_harizma > shans_znania:
    shans = shans_harizma
    ispolzovan_harizma = True
    print(f"Используется шанс от харизмы: {shans}%")
else:
    shans = shans_znania
    print(f"Используется шанс от знаний: {shans}%")
zagovorilsya = False
if harizma < 25:
    if random.randint(1, 100) <= 50:
        print("Не выговорил слово, не сдал")
        zagovorilsya = True
if not zagovorilsya:
    popitki = 1 + (intel // 25)
    print(f"Попыток: {popitki}")
    sdal = False
    for popitka in range(popitki):
        if random.randint(1, 100) <= shans:
            print("Сдал(еле как)")
            sdal = True
            if ispolzovan_harizma and sdal:
                dostizhenie_gambler = True
                print("★ Получено достижение: GAMBLER! ★")
            break
        else:
            print("Попытка провалилась")
    if not sdal:
        print("ОТЧИСЛЕН")
else:
    print("Не повезло с харизмой, ОТЧИСЛЕН")

