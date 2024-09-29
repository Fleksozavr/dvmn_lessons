import random


LETTER_SCORES = {
    'А': 1,
    'Б': 3,
    'В': 1,
    'Г': 3,
    'Д': 2,
    'Е': 1,
    'Ё': 4,
    'Ж': 8,
    'З': 5,
    'И': 1,
    'Й': 4,
    'К': 2,
    'Л': 1,
    'М': 3,
    'Н': 1,
    'О': 1,
    'П': 2,
    'Р': 1,
    'С': 1,
    'Т': 1,
    'У': 2,
    'Ф': 6,
    'Х': 5,
    'Ц': 5,
    'Ч': 5,
    'Ш': 8,
    'Щ': 10,
    'Ъ': 8,
    'Э': 8,
    'Ю': 8,
    'Я': 3
}


def get_random_letter():
    return random.choice(list(LETTER_SCORES.keys()))


def get_word_with_letter(random_letter):
    while True:
        word = input(f'Введите слово на букву "{random_letter}": ').upper()
        if word[0] == random_letter:
            return word
        print(f'Слово должно начинаться с буквы "{random_letter}", попробуйте снова!')


def calculate_score(word):
    all_scores = []
    for letter in word:
        score = LETTER_SCORES.get(letter.upper(), 0)
        all_scores.append(score)
    return sum(all_scores)


def main():
    random_letter = get_random_letter()
    print('Начальная буква:', random_letter)

    print('Игрок 1')
    first_player_word = get_word_with_letter(random_letter)
    first_player_score = calculate_score(first_player_word)

    print('Игрок 2')
    second_player_word = get_word_with_letter(random_letter)
    second_player_score = calculate_score(second_player_word)

    print(f'Игрок 1 ввел слово "{first_player_word}" и набрал {first_player_score} очков.')
    print(f'Игрок 2 ввел слово "{second_player_word}" и набрал {second_player_score} очков.')

    if first_player_score > second_player_score:
        print('Игрок 1 победил!')

    elif first_player_score == second_player_score:
        print('Ничья!')

    else:
        print('Игрок2 победил!')


if __name__ == '__main__':
    main()