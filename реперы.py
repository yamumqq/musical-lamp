
rapers = {
    'Гуф': {'песня': 'Гуф умер', 'бонус': 'Получен автограф от Гуфа и глоток Да Хун Пао.',},
    'Баста': {'песня': 'Медлячок','бонус': 'Получено VIP-приглашение на концерт Басты на арене ЦСКА.',},
    'ОГ Буда': {'песня': 'Сердце </3 Время','бонус': 'Получена фирменная футболка FRERIO.',},
    'Кай Энджел': {'песня': 'Lipstick','бонус': 'Получены рик овенсы Кай Энджела.',}
}


def zdarova():
    print("Здарова бро ты попал в реперский мир!")
    print("Вы готовы стать частью этого мира? (Да/Нет)")
    otvet = input().lower()
    return otvet == 'да'

def choise():
    print("Выберите своего любимого репера:")
    for raper in rapers:
        print(f"- {raper}")
    choise = input()
    return choise 

def vivod(raper):
    song = rapers[raper]['песня']
    print(f"Вы встретили репера {raper}! Он исполнил свою песню '{song}' для вас.")
    print(f"Поздравляем! {rapers[raper]['бонус']}")

def paka():
    print("До свидания, возвращайся реп король)")

def game():
    if not zdarova():
        paka()
        return

    while True:
        chosenrap = choise()

        if chosenrap in rapers:
            vivod(chosenrap)
        else:
            print("Извините, такого репера нет в нашей игре. Попробуйте снова.")

        print("Хотите продолжить игру? (Да/Нет)")
        otvet = input().lower()
        if otvet != 'да':
            paka()
            break

game()