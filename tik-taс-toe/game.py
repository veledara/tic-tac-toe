class bcolors:
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


CROSS_SIGN = f"{bcolors.FAIL}X{bcolors.ENDC}"  # красный крестик
ZERO_SIGN = f"{bcolors.OKGREEN}0{bcolors.ENDC}"  # зеленый нолик


def main():
    mas = [i for i in range(1, 10)]
    print_mas(mas)
    game_cycle(mas, count=0)


def game_cycle(mas, count):
    while True:
        player_input = input(
            f"{bcolors.OKGREEN if count % 2 != 0 else bcolors.FAIL}Введите номер ячейки, на которой хотите разместить свой символ: {bcolors.ENDC}"
        )

        if not is_input_correct(player_input):
            print("Введено некорректное значение! Необходимо ввести число от 1 до 9 (номер ячейки).")
            continue

        turn = int(player_input) - 1

        if cell_is_busy(mas, turn):
            print("Ячейка уже занята!")
            continue

        count += 1
        turn_maker(mas, turn, count)
        print_mas(mas)
        if someone_win(mas):
            print(
                f"{bcolors.FAIL}Победили крестики!{bcolors.ENDC}"
            ) if count % 2 != 0 else print(
                f"{bcolors.OKGREEN}Победили нолики!{bcolors.ENDC}"
            )
            break

        if count == 9:
            print(f"{bcolors.OKBLUE}Ничья!{bcolors.ENDC}")
            break


def someone_win(mas):
    solution = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for comb in solution:
        if (
            mas[comb[0]] == mas[comb[1]] == mas[comb[2]] == CROSS_SIGN
            or mas[comb[0]] == mas[comb[1]] == mas[comb[2]] == ZERO_SIGN
        ):
            return True
    return False


def cell_is_busy(mas, turn):
    return mas[turn] == CROSS_SIGN or mas[turn] == ZERO_SIGN


def turn_maker(mas, turn, count):
    mas[turn] = CROSS_SIGN if count % 2 != 0 else ZERO_SIGN


def is_input_correct(input):
    return input.isnumeric() and (int(input) > 0 and int(input) < 10)


def print_mas(mas):
    print("\033[H\033[J")  # очистка консоли
    print("\n")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(*mas))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(*mas[3:6]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(*mas[6:9]))
    print("     |     |")
    print("\n")


if __name__ == "__main__":
    main()
