import random
from pole_chudes.utils import load_words, save_record, load_record


def play_game():
    try:
        words = load_words()
        if not words:
            print("Отсутствуют слова для игры!")
            return

        record = load_record()

        while True:
            word = random.choice(words)
            hidden_word = ["\u25A0"] * len(word)
            lives = select_difficulty()
            guessed_letters = set()

            print(" ".join(hidden_word))
            print(f"Количество жизней: {'♥' * lives}")

            while lives > 0 and "".join(hidden_word) != word:
                try:
                    guess = input("Назовите букву или слово целиком: ").lower()
                    if not guess:
                        continue

                    if len(guess) == 1:
                        if guess in guessed_letters:
                            print("Вы уже называли эту букву.")
                            continue

                        if guess in word:
                            guessed_letters.add(guess)
                            for i, letter in enumerate(word):
                                if letter == guess:
                                    hidden_word[i] = letter
                        else:
                            print("Неправильно. Вы теряете жизнь.")
                            lives -= 1
                    elif len(guess) > 1:
                        if guess == word:
                            hidden_word = list(word)
                        else:
                            print("Неправильно. Вы теряете жизнь.")
                            lives -= 1
                    else:
                        raise ValueError("Некорректный ввод.")

                    print(" ".join(hidden_word))
                    print(f"Количество жизней: {'♥' * lives}")
                except ValueError as e:
                    print(f"Ошибка ввода: {e}. Попробуйте еще раз.")
                except Exception as e:
                    print(f"Непредвиденная ошибка: {e}. Перезапустите игру.")
                    return
            if "".join(hidden_word) == word:
                print(f"Слово отгадано: {word}")
                print("Вы выиграли! Приз в студию!")
                record += 1
                save_record(record)
            else:
                print("Вы проиграли.")
                print(f"Правильное слово было: {word}")
            play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
            if play_again != "да":
                print(f"Вы отгадали {record} слов!")
                print("До свидания!")
                break
    except FileNotFoundError:
        print("Файл со словами не найден. Проверьте путь к файлу.")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}. Перезапустите игру.")


def select_difficulty():
    while True:
        try:
            level = input("Выберите уровень сложности (легкий/средний/сложный): ").lower()
            if level == "легкий" or level == "7":
                return 7
            elif level == "средний" or level == "5":
                return 5
            elif level == "сложный"or level == "3":
                return 3
            else:
                print("Некорректный уровень сложности. Попробуйте еще раз.")
        except Exception:
            print("Ошибка при выборе уровня сложности. Попробуйте еще раз.")


if __name__ == "__main__":
    play_game()