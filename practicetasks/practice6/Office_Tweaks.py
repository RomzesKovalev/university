import os
import sys
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def change_directory():
    while True:
        try:
            new_path = input("Укажите корректный путь к рабочему каталогу: ").strip()
            if os.path.isdir(new_path):
                os.chdir(new_path)
                break
            else:
                print("Некорректный путь. Попробуйте еще раз.")
        except Exception as e:
            print(f"Ошибка при смене каталога: {e}. Попробуйте еще раз.")


def convert_pdf_to_docx(files_pdf):
    if not files_pdf:
        print("Нет pdf файлов для конвертации.")
        return
    while True:
        try:
            print("Список файлов с расширением .pdf в данном каталоге:")
            for i, file in enumerate(files_pdf):
                print(f"{i + 1}. {file}")
            file_index = input(
                "Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): "
            )
            if not file_index:
                continue
            file_index = int(file_index)
            if file_index == 0:
                for pdf_file in files_pdf:
                    try:
                        docx_file = pdf_file.replace(".pdf", ".docx")
                        print(f"Преобразовываем файл: {pdf_file} в {docx_file}...")
                        parse(pdf_file, docx_file)
                        print("Успешно преобразован!")
                    except Exception as e:
                        print(f"Ошибка при преобразовании файла {pdf_file}: {e}")
                break
            elif 1 <= file_index <= len(files_pdf):
                pdf_file = files_pdf[file_index - 1]
                docx_file = pdf_file.replace(".pdf", ".docx")
                print(f"Преобразовываем файл: {pdf_file} в {docx_file}...")
                parse(pdf_file, docx_file)
                print("Успешно преобразован!")
                break

            else:
                print("Некорректный номер файла. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод номера файла. Попробуйте еще раз.")
        except Exception as e:
            print(f"Ошибка при преобразовании PDF в DOCX: {e}. Попробуйте еще раз.")


def convert_docx_to_pdf(files_docx):
    if not files_docx:
        print("Нет docx файлов для конвертации.")
        return
    while True:
        try:
            print("Список файлов с расширением .docx в данном каталоге:")
            for i, file in enumerate(files_docx):
                print(f"{i + 1}. {file}")

            file_index = input(
                "Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): "
            )
            if not file_index:
                continue
            file_index = int(file_index)
            if file_index == 0:
                for docx_file in files_docx:
                    try:
                        pdf_file = docx_file.replace(".docx", ".pdf")
                        print(f"Преобразовываем файл: {docx_file} в {pdf_file}...")
                        convert(docx_file, pdf_file)
                        print("Успешно преобразован!")
                    except Exception as e:
                        print(f"Ошибка при преобразовании файла {docx_file}: {e}")
                break
            elif 1 <= file_index <= len(files_docx):
                docx_file = files_docx[file_index - 1]
                pdf_file = docx_file.replace(".docx", ".pdf")
                print(f"Преобразовываем файл: {docx_file} в {pdf_file}...")
                convert(docx_file, pdf_file)
                print("Успешно преобразован!")
                break
            else:
                print("Некорректный номер файла. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод номера файла. Попробуйте еще раз.")
        except Exception as e:
            print(f"Ошибка при преобразовании DOCX в PDF: {e}. Попробуйте еще раз.")


def compress_images(files_img):
    if not files_img:
        print("Нет изображений для сжатия.")
        return
    while True:
        try:
            print(
                "Список файлов с расширением ('.jpeg', '.gif', '.png', '.jpg') в данном каталоге:"
            )
            for i, file in enumerate(files_img):
                print(f"{i + 1}. {file}")
            file_index = input(
                "Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): "
            )
            if not file_index:
                continue
            file_index = int(file_index)
            if file_index == 0:
                compression_rate = input("Введите параметры сжатия (от 0 до 100%): ")
                if not compression_rate:
                    continue
                compression_rate = int(compression_rate)
                if not (0 <= compression_rate <= 100):
                    print("Некорректный параметр сжатия. Введите значение от 0 до 100.")
                    continue
                for img_file in files_img:
                    try:
                        print(f"Сжимаем файл: {img_file}...")
                        image = Image.open(img_file)
                        image.save(img_file, quality=compression_rate)
                        print(f"Успешно сжат {img_file}!")
                    except Exception as e:
                        print(f"Ошибка при сжатии файла {img_file}: {e}")
                break
            elif 1 <= file_index <= len(files_img):
                compression_rate = input("Введите параметры сжатия (от 0 до 100%): ")
                if not compression_rate:
                    continue
                compression_rate = int(compression_rate)
                if not (0 <= compression_rate <= 100):
                    print("Некорректный параметр сжатия. Введите значение от 0 до 100.")
                    continue
                img_file = files_img[file_index - 1]
                print(f"Сжимаем файл: {img_file}...")
                image = Image.open(img_file)
                image.save(img_file, quality=compression_rate)
                print(f"Успешно сжат {img_file}!")
                break
            else:
                print("Некорректный номер файла. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод номера файла. Попробуйте еще раз.")
        except Exception as e:
            print(f"Ошибка при сжатии изображения: {e}. Попробуйте еще раз.")


def delete_files(files_all):
    if not files_all:
        print("Нет файлов для удаления.")
        return
    while True:
        try:
            print("Выберите действие:")
            print("1. Удалить все файлы начинающиеся на определенную подстроку")
            print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
            print("3. Удалить все файлы содержащие определенную подстроку")
            print("4. Удалить все файлы по расширению")

            action = input("Введите номер действия: ")
            if not action:
                continue
            action = int(action)
            if action not in range(1, 5):
                print("Некорректный номер действия. Попробуйте еще раз.")
                continue
            substring = input("Введите подстроку: ")
            if not substring:
                continue

            deleted_files = []
            if action == 1:  # Начинающиеся
                for file in files_all:
                    if file.lower().startswith(substring.lower()):
                        os.remove(file)
                        deleted_files.append(file)
            elif action == 2:  # Заканчивающиеся
                for file in files_all:
                    if file.lower().endswith(substring.lower()):
                        os.remove(file)
                        deleted_files.append(file)
            elif action == 3:  # Содержащие
                for file in files_all:
                    if substring.lower() in file.lower():
                        os.remove(file)
                        deleted_files.append(file)
            elif action == 4:  # по расширению
                for file in files_all:
                    if file.lower().endswith(f".{substring.lower()}"):
                        os.remove(file)
                        deleted_files.append(file)

            if deleted_files:
                print(f"Успешно удалены файлы:")
                for file in deleted_files:
                    print(file)
            else:
                print(f"Нет файлов, удовлетворяющих условию")
            break
        except ValueError:
            print("Некорректный ввод номера действия. Попробуйте еще раз.")
        except Exception as e:
            print(f"Ошибка при удалении файлов: {e}. Попробуйте еще раз.")


def get_files_with_extension(extensions):
    files_list = []
    for file in os.listdir():
        if any(file.lower().endswith(ext) for ext in extensions):
            files_list.append(file)
    return files_list


def main():
    while True:
        try:
            print(f"Текущий каталог: {os.getcwd()}")
            print("Выберите действие:")
            print("0. Сменить рабочий каталог")
            print("1. Преобразовать PDF в Docx")
            print("2. Преобразовать Docx в PDF")
            print("3. Произвести сжатие изображений")
            print("4. Удалить группу файлов")
            print("5. Выход")
            choice = input("Ваш выбор: ")
            if not choice:
                continue
            choice = int(choice)
            if choice == 0:
                change_directory()
            elif choice == 1:
                files_pdf = get_files_with_extension((".pdf",))
                convert_pdf_to_docx(files_pdf)
            elif choice == 2:
                files_docx = get_files_with_extension((".docx",))
                convert_docx_to_pdf(files_docx)
            elif choice == 3:
                files_img = get_files_with_extension((".jpeg", ".gif", ".png", ".jpg"))
                compress_images(files_img)
            elif choice == 4:
                files_all = os.listdir()
                delete_files(files_all)
            elif choice == 5:
                print("Выход.")
                break
            else:
                print("Некорректный выбор. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}. Попробуйте еще раз.")


if __name__ == "__main__":
    main()