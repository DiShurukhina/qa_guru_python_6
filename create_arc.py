from zipfile import ZipFile
import os

'''
– Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv;
– Положить его в ресурсы;
– Реализовать чтение и проверку содержимого каждого файла из архива в виде тестов
'''

# определение пути к папкам files, resourses и архиву
current_dir = os.path.dirname(os.path.abspath(__file__))
files = os.path.join(current_dir, 'files')
res = os.path.join(current_dir, 'resourses')
zip_path = os.path.join(res, 'archive.zip')
files_dir = os.listdir(files)


# очистка папки resourses перед созданием архива
def delete_arc():
    if os.path.exists(zip_path):
        os.remove(zip_path)


# создание архива
def create_arc():
    with ZipFile(zip_path, 'w') as arc:
        for file in files_dir:
            filename = os.path.join(files, file)
            arc.write(filename, file)
