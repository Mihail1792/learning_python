# Задача такая, есть 2 файла read_file.txt и write_file.txt
# Строки из файла read_file.txt нужно дописать в write_file.txt
# Скрипт должен запускаться из командной строки, первым позиционным аргументом мы указываем путь к файлу,
# из которого мы будем брать строки, вторым позиционным аргументом передается путь к файлу в который будем дописывать.
# сделать проверку на наличие файлов, если их нет по указаному пути, вывести в консоль оповещение о том что
# файл не найден и прекратить ход выполнения программы.
# Файл в который мы дописываем, нужно переименовать добавить флаг _updated,
# то есть в результате должно получиться: write_file_updated.txt
# библиотека os python почитать
# Дополнительное условие, предположим что write_file.txt весит 150 гигов, нужно дописывать в его так,
# что бы он весьне попал в оперативную память.
import sys
import os


files_dir = "files"

pathname = os.path.dirname(sys.argv[0])
script_path = os.path.abspath(pathname)

result_path = script_path + "/" + files_dir + "/"

if not os.path.isdir(files_dir):
    print(f'directory "{files_dir}" is not exist in path "{script_path}"')
    sys.exit(1)

if len(sys.argv) < 3:
    print("Not enough args")
    sys.exit(1)


input_file, output_file = sys.argv[1], sys.argv[2]

if not os.path.isfile(result_path + input_file) or not os.path.isfile(result_path + output_file):
    print('Один или оба файла не существуют')
    sys.exit(1)

result_file_name, file_extension = output_file.split('.')[0] + "_updated", output_file.split('.')[1]

write_file_data = open(result_path + output_file, 'a')

with open(result_path + input_file, 'r') as read_file_data:
    for line in read_file_data:
        write_file_data.write(line)

write_file_data.close()

os.rename(result_path + output_file, result_path + result_file_name + "." + file_extension)
sys.exit(0)
