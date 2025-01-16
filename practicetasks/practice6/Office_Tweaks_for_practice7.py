import PySimpleGUI as sg
import os
import sys
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def change_directory():
    layout = [[sg.Text("Укажите путь к рабочему каталогу:")],
              [sg.Input(key="-FOLDER-"), sg.FolderBrowse()],
              [sg.Button("OK", button_color='black'), sg.Button("Cancel", button_color='black')]]
    window = sg.Window("Смена каталога", layout, background_color='white')
    event, values = window.read()
    window.close()
    if event == "OK":
        new_path = values["-FOLDER-"]
        if os.path.isdir(new_path):
            os.chdir(new_path)
            return os.getcwd()
        else:
            sg.popup_error("Некорректный путь.", background_color='white', text_color='black')
            return None
    return None


def convert_pdf_to_docx(files_pdf):
    if not files_pdf:
        sg.popup_no_buttons("Нет pdf файлов для конвертации.", title='Преобразование PDF', background_color='white',
                            text_color='black')
        return
    layout = [[sg.Text("Список файлов с расширением .pdf в данном каталоге:")],
              [sg.Listbox(values=files_pdf, key="-PDF-FILES-", size=(40, len(files_pdf)), enable_events=True)],
              [sg.Button("Преобразовать все", button_color='black'),
               sg.Button("Преобразовать выбранный", button_color='black'),
               sg.Button("Отмена", button_color='black')]]
    window = sg.Window("Преобразование PDF в DOCX", layout, background_color='white')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Отмена"):
            window.close()
            break
        if event == "Преобразовать все":
            for pdf_file in files_pdf:
                try:
                    docx_file = pdf_file.replace(".pdf", ".docx")
                    sg.popup(f"Преобразовываем файл: {pdf_file} в {docx_file}...", title='Преобразование',
                             background_color='white', text_color='black')
                    parse(pdf_file, docx_file)
                    sg.popup(f"Успешно преобразован {pdf_file}!", title='Преобразование', background_color='white',
                             text_color='black')
                except Exception as e:
                    sg.popup_error(f"Ошибка при преобразовании файла {pdf_file}: {e}", title='Преобразование',
                                   background_color='white', text_color='black')
            window.close()
            break
        if event == "Преобразовать выбранный":
            if values["-PDF-FILES-"]:
                pdf_file = values["-PDF-FILES-"][0]
                try:
                    docx_file = pdf_file.replace(".pdf", ".docx")
                    sg.popup(f"Преобразовываем файл: {pdf_file} в {docx_file}...", title='Преобразование',
                             background_color='white', text_color='black')
                    parse(pdf_file, docx_file)
                    sg.popup(f"Успешно преобразован {pdf_file}!", title='Преобразование', background_color='white',
                             text_color='black')
                    window.close()
                    break
                except Exception as e:
                    sg.popup_error(f"Ошибка при преобразовании файла {pdf_file}: {e}", title='Преобразование',
                                   background_color='white', text_color='black')
            else:
                sg.popup_error("Выберите файл для преобразования.", title='Преобразование', background_color='white',
                               text_color='black')


def convert_docx_to_pdf(files_docx):
    if not files_docx:
        sg.popup_no_buttons("Нет docx файлов для конвертации.", title='Преобразование DOCX', background_color='white',
                            text_color='black')
        return
    layout = [[sg.Text("Список файлов с расширением .docx в данном каталоге:")],
              [sg.Listbox(values=files_docx, key="-DOCX-FILES-", size=(40, len(files_docx)), enable_events=True)],
              [sg.Button("Преобразовать все", button_color='black'),
               sg.Button("Преобразовать выбранный", button_color='black'),
               sg.Button("Отмена", button_color='black')]]
    window = sg.Window("Преобразование DOCX в PDF", layout, background_color='white')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Отмена"):
            window.close()
            break
        if event == "Преобразовать все":
            for docx_file in files_docx:
                try:
                    pdf_file = docx_file.replace(".docx", ".pdf")
                    sg.popup(f"Преобразовываем файл: {docx_file} в {pdf_file}...", title='Преобразование',
                             background_color='white', text_color='black')
                    convert(docx_file, pdf_file)
                    sg.popup(f"Успешно преобразован {docx_file}!", title='Преобразование', background_color='white',
                             text_color='black')
                except Exception as e:
                    sg.popup_error(f"Ошибка при преобразовании файла {docx_file}: {e}", title='Преобразование',
                                   background_color='white', text_color='black')
            window.close()
            break
        if event == "Преобразовать выбранный":
            if values["-DOCX-FILES-"]:
                docx_file = values["-DOCX-FILES-"][0]
                try:
                    pdf_file = docx_file.replace(".docx", ".pdf")
                    sg.popup(f"Преобразовываем файл: {docx_file} в {pdf_file}...", title='Преобразование',
                             background_color='white', text_color='black')
                    convert(docx_file, pdf_file)
                    sg.popup(f"Успешно преобразован {docx_file}!", title='Преобразование', background_color='white',
                             text_color='black')
                    window.close()
                    break
                except Exception as e:
                    sg.popup_error(f"Ошибка при преобразовании файла {docx_file}: {e}", title='Преобразование',
                                   background_color='white', text_color='black')
            else:
                sg.popup_error("Выберите файл для преобразования.", title='Преобразование', background_color='white',
                               text_color='black')


def compress_images(files_img):
    if not files_img:
        sg.popup_no_buttons("Нет изображений для сжатия.", title='Сжатие изображений', background_color='white',
                            text_color='black')
        return
    layout = [[sg.Text("Список файлов с расширением ('.jpeg', '.gif', '.png', '.jpg') в данном каталоге:")],
              [sg.Listbox(values=files_img, key="-IMG-FILES-", size=(40, len(files_img)), enable_events=True)],
              [sg.Input(key="-QUALITY-", size=(5), default_text="80"), sg.Text("Качество (0-100)")],
              [sg.Button("Сжать все", button_color='black'), sg.Button("Сжать выбранный", button_color='black'),
               sg.Button("Отмена", button_color='black')]]
    window = sg.Window("Сжатие изображений", layout, background_color='white')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Отмена"):
            window.close()
            break
        try:
            quality = int(values["-QUALITY-"])
            if not (0 <= quality <= 100):
                raise ValueError("Качество должно быть от 0 до 100.")
        except ValueError as e:
            sg.popup_error(f"Ошибка ввода качества: {e}", title='Сжатие изображений', background_color='white',
                           text_color='black')
            continue
        if event == "Сжать все":
            for img_file in files_img:
                try:
                    sg.popup(f"Сжимаем файл: {img_file}...", title='Сжатие', background_color='white',
                             text_color='black')
                    image = Image.open(img_file)
                    image.save(img_file, quality=quality)
                    sg.popup(f"Успешно сжат {img_file}!", title='Сжатие', background_color='white', text_color='black')
                except Exception as e:
                    sg.popup_error(f"Ошибка при сжатии файла {img_file}: {e}", title='Сжатие', background_color='white',
                                   text_color='black')
            window.close()
            break
        if event == "Сжать выбранный":
            if values["-IMG-FILES-"]:
                img_file = values["-IMG-FILES-"][0]
                try:
                    sg.popup(f"Сжимаем файл: {img_file}...", title='Сжатие', background_color='white',
                             text_color='black')
                    image = Image.open(img_file)
                    image.save(img_file, quality=quality)
                    sg.popup(f"Успешно сжат {img_file}!", title='Сжатие', background_color='white', text_color='black')
                    window.close()
                    break
                except Exception as e:
                    sg.popup_error(f"Ошибка при сжатии файла {img_file}: {e}", title='Сжатие', background_color='white',
                                   text_color='black')
            else:
                sg.popup_error("Выберите файл для сжатия.", title='Сжатие', background_color='white',
                               text_color='black')


def delete_files(files_all):
    if not files_all:
        sg.popup_no_buttons("Нет файлов для удаления.", title='Удаление файлов', background_color='white',
                            text_color='black')
        return

    radio_style = {'font': ('black', 'white'), 'border_width': 1, 'background_color': 'white'}

    layout = [[sg.Text("Выберите действие:")],
              [sg.Radio("Удалить все файлы, начинающиеся на подстроку", "RADIO1", key="-START-", **radio_style)],
              [sg.Radio("Удалить все файлы, заканчивающиеся на подстроку", "RADIO1", key="-END-", **radio_style)],
              [sg.Radio("Удалить все файлы, содержащие подстроку", "RADIO1", key="-CONTAIN-", **radio_style)],
              [sg.Radio("Удалить все файлы по расширению", "RADIO1", key="-EXT-", **radio_style)],
              [sg.Input(key="-SUBSTRING-", do_not_clear=False)],
              [sg.Button("Удалить", button_color='black'), sg.Button("Отмена", button_color='black')]]

    window = sg.Window("Удаление файлов", layout, background_color='white')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Отмена"):
            window.close()
            break
        if event == "Удалить":
            substring = values["-SUBSTRING-"]
            if not substring:
                sg.popup_error("Введите подстроку!", title='Удаление файлов', background_color='white',
                               text_color='black')
                continue

            deleted_files = []
            if values["-START-"]:
                for file in files_all:
                    if file.lower().startswith(substring.lower()):
                        os.remove(file)
                        deleted_files.append(file)
            elif values["-END-"]:
                for file in files_all:
                    if file.lower().endswith(substring.lower()):
                        os.remove(file)
                        deleted_files.append(file)
            elif values["-CONTAIN-"]:
                for file in files_all:
                    if substring.lower() in file.lower():
                        os.remove(file)
                        deleted_files.append(file)
            elif values["-EXT-"]:
                for file in files_all:
                    if file.lower().endswith(f".{substring.lower()}"):
                        os.remove(file)
                        deleted_files.append(file)

            if deleted_files:
                sg.popup(f"Успешно удалены файлы:\n{'\n'.join(deleted_files)}", title='Удаление файлов',
                         background_color='white', text_color='black')
            else:
                sg.popup(f"Нет файлов, удовлетворяющих условию", title='Удаление файлов', background_color='white',
                         text_color='black')
            window.close()
            break


def get_files_with_extension(extensions):
    files_list = []
    for file in os.listdir():
        if any(file.lower().endswith(ext) for ext in extensions):
            files_list.append(file)
    return files_list


def main():
    sg.theme("LightGrey1")
    button_style = {'button_color': ('black', 'white'), 'border_width': 1, 'font': ('Helvetica', 12)}

    layout = [[sg.Text("Менеджер файлов", font=("Helvetica", 20), text_color='black')],
              [sg.Button("Сменить каталог", **button_style), sg.Button("Преобразовать PDF в DOCX", **button_style),
               sg.Button("Преобразовать DOCX в PDF", **button_style), sg.Button("Сжать изображения", **button_style),
               sg.Button("Удалить файлы", **button_style)],
              [sg.Button("Выход", **button_style)]]
    window = sg.Window("Менеджер файлов", layout, background_color='white')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Выход"):
            break
        try:
            if event == "Сменить каталог":
                new_path = change_directory()
                if new_path:
                    sg.popup(f"Рабочий каталог изменён на: {new_path}", title='Изменение каталога',
                             background_color='white', text_color='black')
            elif event == "Преобразовать PDF в DOCX":
                files_pdf = get_files_with_extension((".pdf",))
                convert_pdf_to_docx(files_pdf)
            elif event == "Преобразовать DOCX в PDF":
                files_docx = get_files_with_extension((".docx",))
                convert_docx_to_pdf(files_docx)
            elif event == "Сжать изображения":
                files_img = get_files_with_extension((".jpeg", ".gif", ".png", ".jpg"))
                compress_images(files_img)
            elif event == "Удалить файлы":
                files_all = os.listdir()
                delete_files(files_all)
        except Exception as e:
            sg.popup_error(f"Произошла непредвиденная ошибка: {e}", background_color='white', text_color='black')
    window.close()


if __name__ == "__main__":
    main()