# pymorphy2/3 не переводили у меня текст на английский, я взял гугл переводчик, он помедленнее

import re
from collections import Counter
from googletrans import Translator


def process_dialogue(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        return
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return

    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    translator = Translator()

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for word, count in sorted_words:
                try:
                    translation = translator.translate(word, dest='en').text
                    f.write(f"{word} | {translation} | {count}\n")
                except Exception as e:
                    print(f"Ошибка перевода слова '{word}': {e}")
                    f.write(f"{word} |  | {count}\n")

    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")
        return

    print("Перевод завершен и записан в 'output_file'")


if __name__ == "__main__":
    input_file = "dialogue.txt"
    output_file = "output.txt"
    process_dialogue(input_file, output_file)