def copy_line(source_file, destination_file, line_number):
    with open(source_file, 'r') as source:
        lines = source.readlines()
        if line_number < 1 or line_number > len(lines):
            print("Некорректный номер строки")
            return
        line_to_copy = lines[line_number - 1]
        with open(destination_file, 'a') as destination:
            destination.write(line_to_copy)
        print("Строка успешно скопирована")
source_file = "source.txt"  
destination_file = "destination.txt"  

line_number = int(input("Введите номер строки для копирования: "))

copy_line(source_file, destination_file, line_number)        