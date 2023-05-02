def fileSorterAndJoiner(file_name_list):
    files_list = [] # формируем удобный список для сортировки встроенной функцией sorted
    for file in file_name_list:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.readlines()
            files_list.append([file, len(content), content])
    
    sorted_files_list = sorted(files_list, key=lambda x:  x[1]) # сортируем по второму элементу - количеству строк в файле

    with open('result.txt', 'w', encoding='utf-8') as f: 
        for file in sorted_files_list: # построчно запихиваем отсортированный список в результирующий файл
            # служебная информация
            f.write(file[0] + '\n') # имя
            f.write(str(file[1]) + '\n') # количество строк
            for line in file[2]: # содержимое файла
                f.write(line)
            f.write('\n')# оставит лишнюю строку в конце результирующего файла, но ... И  ТАААК СОЙДЕЕЕЕТ!


fileSorterAndJoiner(['file_1.txt', 'file_2.txt', 'file_3.txt'])