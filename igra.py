import random
import time


def print_delay(text):
    print(text)
    time.sleep(1)


inventory = []


def start_game():
    print_delay("Добро пожаловать в текстовую игру про Шрека!")
    print_delay("Ты Шрек и находишься на болоте. Тебе нужно найти свою любимую,Фиону, которую похитил злобный Лорд Фарквад!")
    print_delay("Шрек, ты готов к приключениям?")
    input("Нажми Enter, чтобы начать...")
    level_one()


def level_one():
    print_delay("\nУровень 1: Ты видишь три пути:")
    paths = ("Лес", "Река", "Горы")

    print(f"Куда ты пойдешь?")
    for path in paths:
        print(f"- {path}")

    choice = input("Введите путь: ").strip().lower()

    if choice in [p.lower() for p in paths]:
        if choice == "лес":
            print_delay("Ты встретил осла! Он хочет помочь тебе.")
            print_delay("\nОсел: Привет, Шрек! Я Осел, самый умный и смешной осел в этом болоте!")
            print_delay("Шрек: (грубо) Осел, мне нужно найти Фиону! Ты можешь помочь?")
            print_delay(
                "Осел: Конечно, Шрек! Я всегда рад помочь! Но прежде, чем мы пойдем дальше, я должен проверить твои знания...")
            level_two()
        elif choice == "река":
            print_delay("Ты нашел сокровище! Но его охраняет монстр.")
            level_three()
        elif choice == "горы":
            print_delay("Ты нашел красивый вид, но ты потерял время.")
            print_delay("Осел(где-то в лесу): Эй, Шрек! Ты куда? Подойди ко мне!")
            level_one()
    else:
        print_delay("Неверный выбор, попробуй снова.")
        level_one()


def level_two():
    print_delay("\nУровень 2: Осел предлагает тебе загадку.")
    zagadka = "Идет то в гору, то с горы, но остается на месте"
    print(zagadka)
    answer = input("Ваш ответ: ")

    if answer.lower() == "дорога":
        print_delay("Правильно! Ты проходишь далее.")
        print_delay("Осел: Молодец, Шрек! Ты настоящий герой!")
        print_delay("\nПроходя дальше в лес ты слышишь крик")
        print_delay("Осёл: Шрек, вдруг это Фиона, давай проверим")
        razvilka = int(input("Пойти на крик - 1. Идти дальше - 2: "))
        if razvilka == 1:
            level_three()
        elif razvilka == 2:
            level_four()
        else:
            print_delay("Введите предложенный вариант")
            level_two()
    else:
        print_delay("Неправильно. Осел уходит.")
        print_delay("Осел: Ты слишком тупой для этого, Шрек! Прощай!")
        level_one()


def level_three():
    print_delay("\nУровень 3: Ты наткнулся на монстра!")
    monster_health = 30
    player_health = 30

    while monster_health > 0 and player_health > 0:
        print_delay(f"\nСостояние здоровья: Ты – {player_health}, Монстр – {monster_health}")
        action = input("Что ты будешь делать? (атака/бежать) ").strip().lower()

        if action == "атака":
            damage = random.randint(5, 15)
            monster_health -= damage
            print_delay(f"Ты атакуешь монстра и наносишь {damage} урона.")
        elif action == "бежать":
            print_delay("Ты бежишь от монстра и возвращаешься обратно.")
            print_delay("Осел: Шрек, не трусь! Ты должен сражаться!")
            level_one()
            return
        else:
            print_delay("Неверный выбор, попробуй снова.")

            # Монстр атакует
        damage = random.randint(5, 10)
        player_health -= damage
        print_delay(f"Монстр атакует тебя и наносит {damage} урона.")

    if player_health <= 0:
        print_delay("Ты был побежден монстром. Игра окончена.")
        play_again()
    else:

        inventory.append("Зелье невидимости")
        print_delay("Ты победил монстра!")
        print_delay("Осел: Ура! Ты сделал это, Шрек!")
        print_delay("Победив монстра, вы заметиили выпавшее зелье невидимости")
        print_delay("У вас в инвентаре теперь есть зелье невидимости")
        level_four()


def level_four():
    print_delay("\nУровень 4: Ты достиг замка Фионы.")
    print_delay("Ты видишь стражника перед замком, используй зелье невидимости, чтобы избежать встречи с ним.")
    if "Зелье невидимости" in inventory:
        print_delay("У тебя есть зелье невидимости! Хочешь использовать его?")
        choice = input("Использовать (да/нет)? ").lower()
        if choice == "да":
            print_delay("Ты выпиваешь зелье невидимости и становишься невидимым!")
            print_delay("Ты пробираешься мимо стражника и попадаешь в замок.")
            inventory.remove("Зелье невидимости")
            level_five()
        elif choice == "нет":
            print_delay("\nСтражник: А ну стоять! Сегодня я добрый, поэтому если ты угадаешь какое я загадал число от 1 до 10, я отпущу вас ")
            ugadaika = random.randint(1, 10)

            attempts = 3
            while attempts > 0:
                print_delay(f"У тебя осталось {attempts} попыток.")
                dovod = int(input("Угадайте число от 1 до 10: "))
                if dovod == ugadaika:
                    print_delay(f"Ты угадал число это было {ugadaika}!")
                    print_delay("Стражник: Ладно, так уж и быть, идите дальше")
                    level_five()

                else:
                    print_delay(f"Ха-ха тупой орк, это не то число!")
                    attempts -= 1

            print_delay("Ты не угадал мою число, вперёд, в темницу!")
            print_delay("Осел: Мы проиграли, Шрек...")
            print_delay("Фиона: Спаси меня от Фаркуада, Шрек!!!!!")
            play_again()
        else:
            print_delay("Неверный выбор, попробуй снова.")
            level_four()
    else:
        print_delay("\nУ тебя нет зелья невидимости, поэтому стражник замечает тебя")
        print_delay("Стражник: А ну стоять! Сегодня я добрый, поэтому если ты угадаешь какое я загадал число от 1 до 10, я отпущу вас ")
        ugadaika = random.randint(1, 10)

        attempts = 3
        while attempts > 0:
            print_delay(f"У тебя осталось {attempts} попыток.")
            dovod = int(input("Угадайте число от 1 до 10: "))
            if dovod == ugadaika:
                print_delay(f"Ты угадал число это было {ugadaika}!")
                print_delay("Стражник: Ладно, так уж и быть, идите дальше")
                level_five()

            else:
                print_delay(f"Ха-ха тупой орк, это не то число!")
                attempts -= 1

        print_delay("Ты не угадал мою число, вперёд, в темницу!")
        print_delay("Осел: Мы проиграли, Шрек...")
        print_delay("Фиона: Спаси меня от Фаркуада, Шрек!!!!!")
        play_again()


def level_five():
    print_delay("Перед тобой три двери:")
    print_delay("1. Дверь из красного дерева")
    print_delay("2. Дверь из дуба")
    print_delay("3. Дверь из железа")

    choice = input("Какую дверь ты выберешь? (1/2/3): ")

    if choice == "1":
        print_delay("Ты открыл дверь и за ней... пустота!")
        print_delay("Осел: Ну, вот и провал! Может, попробуем другую?")
        print_delay("Шрек: Осел, смотри здесь вовсе не пусто, я вижу какой-то свисток на полу!")
        print_delay("Осел: Точно! Это драконий свисток, с помощью него можно призвать дракона!")
        inventory.append("Свисток")
        level_five()
    elif choice == "2":
        print_delay("Ты открыл дверь и за ней... комната с зеркалом!")
        print_delay("В зеркале отражается Лорд Фарквад, который держит Фиону.")
        print_delay("Осел: Вот черт! Он заманил нас в ловушку!")
        level_six()
    elif choice == "3":
        print_delay("Ты открыл дверь и за ней... ловушка!")
        print_delay("На тебя падает клетка, и тебя выводят стражники!")
        print_delay("Осел: Шрек, ты сможешь, попробуй ещё раз!")
        level_one()
    else:
        print_delay("Неверный выбор. Попробуй снова.")
        level_five()


def level_six():
    print_delay("\nУровень 5: Войдя в зеркало ты оказываешься в большой комнате, где Лорд Фарквад держит Фиону.")
    print_delay("Чтобы освободить Фиону, тебе нужно найти ключ, который спрятан в комнате.")
    print_delay("Осел: Шрек, будь осторожен! Лорд Фарквад очень хитер!")

    hiding_places = ["сундук", "под коврами", "за картиной", "в шкафу", "под столом"]
    key_location = random.choice(hiding_places)

    attempts = 3
    while attempts > 0:
        print_delay(f"У тебя осталось {attempts} попыток.")
        place = input("Где ты будешь искать ключ? (сундук/под коврами/за картиной/в шкафу/под столом): ").lower()

        if place == key_location:
            print_delay(f"Ты нашел ключ! Он был спрятан {key_location}!")
            print_delay("Шрек: (радостно) Фиона, я нашел ключ!")
            level_seven()
        else:
            print_delay(f"Ключа там нет... Попробуй другое место.")
            attempts -= 1

    print_delay("Ты не нашел ключ! Лорд Фарквад уходит с Фионой!")
    print_delay("Осел: Мы проиграли, Шрек...")
    play_again()


def level_seven():
    print_delay("\nУровень 6: Вы с Фионой оказались в замке Лорда Фарквада.")
    print_delay("Лорд Фарквад приказал своим стражникам поймать вас и заточить в темницу.")
    print_delay("Осел: Шрек, нам нужно бежать! За нами гонятся!")

    castle_map = {
        "Тронный зал": ["Спальня", "Библиотека", "Бальный зал"],
        "Спальня": ["Тронный зал", "Тайный ход", "Оружейная"],
        "Библиотека": ["Тронный зал", "Кухня", "Оружейная"],
        "Кухня": ["Библиотека", "Подвал"],
        "Тайный ход": ["Спальня", "Сад", "Подвал"],
        "Сад": ["Тайный ход", "Выход из замка"],
        "Подвал": ["Кухня", "Темница"],
        "Бальный зал": ["Тронный зал", "Гостевая комната"],
        "Оружейная": ["Библиотека", "Спальня"],
        "Гостевая комната": ["Бальный зал", ]
    }

    current_room = "Тронный зал"

    while True:
        print_delay(f"\nВы находитесь в {current_room}.")
        print("Доступные выходы:", ", ".join(castle_map[current_room]))

        choice = input("Куда вы пойдете? ")

        if choice in castle_map[current_room]:
            current_room = choice

            if current_room == "Выход из замка":
                print_delay("\nВы с Фионой сбежали из замка!")
                print_delay("Осел: Ура! Мы сделали это, Шрек!")
                level_eight()

            elif current_room == "Оружейная":
                print_delay("Ты находишь и забираешь себе меч")
                inventory.append("меч")

            elif current_room == "Сад":
                print_delay(
                    "\nК вам навстречу идёт стражник, попробуйте спрятаться(Шанс 50%) или сразите его мечом(если есть)")
                if "меч" in inventory:
                    print_delay("Вы сразили стражника мечом, теперь вам ничего не угрожает")
                    inventory.remove('меч')
                else:
                    nahod = random.randint(1, 2)
                    if nahod == 1:
                        print_delay("\nВам повезло, Стражник не заметил вас")
                    else:
                        print_delay("\nВам не повезло, Стражник увидел вас и заточил в темницу")
                        play_again()

            elif current_room == "Темница":
                print_delay("\nВас поймали и заточили в темницу!")
                print_delay("Осел: Вот черт! Мы проиграли...")
                play_again()
                return

        else:
            print_delay("Неверный выбор. Попробуй снова.")


def level_eight():
    print_delay("Выйди из замка, вы встречаете гвардию стражников")
    if "меч" in inventory:
        print_delay("У тебя есть меч! Ты сражаешься со стражниками и побеждаешь!")
        print_delay("Осел: Ура! Мы победили, Шрек!")
        end_game(True)
    elif "Свисток" in inventory:
        print_delay("У тебя есть свисток! Ты свистишь, и дракон прилетает!")
        print_delay("Дракон: (рычит) Шрек, ты звал? Ну, садись!")
        print_delay("Ты садишься на дракона и улетаете!")
        print_delay("Осел: Шрек, мы спаслись! Фиона, ты будешь в безопасности!")
        end_game(True)
    else:
        print_delay("У тебя нет меча или свистка. Ты не можешь пройти мимо стражников.")
        print_delay("Стражники хватают тебя, и ты попадаешь обратно в замок...")
        play_again()


def end_game(success):
    if success:
        print_delay("\nПоздравляю! Вы выбрались из замка и ты спас свою любимую!")
        print_delay("Шрек: Фиона! (обнимает Фиону)")
        print_delay("Фиона: Шрек! Я так рада, что мы снова вместе!")
    else:
        print_delay("\nК сожалению, ты не смог найти Фиону. Попробуй снова.")
        print_delay("Осел: Не сдавайся, Шрек! Мы найдем Фиону!")
    play_again()


def play_again():
    again = input("Хотите сыграть снова? (да/нет) ").strip().lower()
    if again == "да":
        start_game()
    else:
        print_delay("Спасибо за игру!")


if __name__ == "__main__":
    start_game()
