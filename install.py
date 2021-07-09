import os

logo = print('''
--------------------------
|                        |
|                        |
| Nier Automata Ru Linux |
|                        |
|                        |
--------------------------
\n''')

menu= int(input('1. Автоматическое копирование,\n2. Ввести другой путь.\nВвод: '))

if menu == 1:
    name_user = input('Имя пользователя: ')
    wget = os.system('get https://github.com/AnilAntari/NierAutomataRuLinux/releases/download/1.0/generic.tar')
    tar = os.system('tar -xvf generic.tar')
    copy = 'cp -r generic/data/* /home/' + name_user + '/.local/share/Steam/steamapps/common/NieRAutomata/data'
    copying = os.system(copy)
    final = print('Файлы скопированы.')
elif menu == 2:
    way = str(input('Введите путь: '))
    wget = os.system('get https://github.com/AnilAntari/NierAutomataRuLinux/releases/download/1.0/generic.tar')
    tar = os.system('tar -xvf generic.tar')
    copy = 'cp -r generic/data/*' + ' ' + way
    copying = os.system(copy)
    final = print('Файлы скопированы.')
