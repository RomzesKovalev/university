import os

def load_words(filename='words.txt'):
  try:
    with open(filename, "r", encoding="utf-8") as f:
       words = [line.strip().lower() for line in f if line.strip()] # отсеиваем пустые строки
       return words
  except FileNotFoundError:
      print("Файл со словами не найден.")
      return []
  except Exception as e:
      print(f"Ошибка при чтении файла: {e}")
      return []

def save_record(record, filename="records.txt"):
  try:
      with open(filename, "w") as f:
          f.write(str(record))
  except Exception as e:
        print(f"Ошибка при записи рекорда: {e}")

def load_record(filename="records.txt"):
    try:
        if not os.path.exists(filename):
            return 0
        with open(filename, "r") as f:
            return int(f.readline())
    except FileNotFoundError:
         return 0
    except Exception:
        return 0