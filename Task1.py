import os.path
import glob
import shutil
mylist = ['/MainFolder',
        '/MainFolder/Folder1',
        '/MainFolder/Folder1/SubFolder1',
        'MainFolder/Folder1/SubFolder1/File_01.txt',
        '/MainFolder/Folder2', '/MainFolder/Folder2/SubFolder2',
        'MainFolder/Folder2/SubFolder2/File_02.txt',
        '/MainFolder/Folder3', '/MainFolder/Folder3/SubFolder3',
        'MainFolder/Folder3/SubFolder3/File_03.txt',
        '/MainFolder/Folder4', '/MainFolder/Folder4/SubFolder4',
        'MainFolder/Folder4/SubFolder4/File_04.txt']
def f_init():
    print('/h - показать меню (хелп)')
    print('/f - поиск файла или директории')
    print('/d - удаление файла или директории')
    print('/r - изменить название файла или директории')
    print('/c - изменить директорию')
    print('/q - выход')
    print('--create - создать иерархию каталогов')
    print('--search [имя файла или директории] - поиск файла или директории')
    print('--del [имя файла или директории] - удаление файла или директории')
    print('--rename [старое имя/новое имя] - переименовать файл/директорию')

def f_search(fname,recurse):
    arr = glob.glob('**{0}*{1}'.format(slash,fname), recursive=recurse)
    if (len(arr) == 0):
        print('Ничего не найдено('.format(fname))
    else:
        print('найдено {0}'.format(len(arr)))
        for elem in arr:
            print(elem)

def f_delete(fname):
    slashindex = fname.rfind(slash,0)
    dirpath = fname[0:slashindex+1]
    filename =fname[slashindex + 1:]
    if (os.path.exists(fname)):
        if (os.path.isfile(fname)):
            try:
                os.remove(fname)
                print('{0} успешно удалено '.format(filename) +
                      'в этой директории {0}'.format(currdir + dirpath))
            except IOError as e:
                print('Удаление не удалось {0}'.format(filename))
            for elem in os.listdir(currdir+dirpath):
                print(elem)
        elif (os.path.isdir(fname)):
            try:
                os.rmdir(fname)
                print('{0} успешно удалено'.format(fname))
            except IOError as e:
                print('{0} не пусто'.format(fname))
                harddelete = input('Уверены что хотите это удалить? (y/n): ')
                if (harddelete == 'y'):
                    shutil.rmtree(fname)
    else:
        print('{0} не найдено'.format(fname))
    if os.path.exists(fnames[0]):
        try:
            os.rename(fnames[0], fnames[1])
        except IOError as e:
            print('Невозможно переименовать {0}'.format(fnames[0]))
    else:
        print('{0} не найдено.'.format(fnames[0]))

if (os.name == 'nt'):
    slash = '\\'
    mylist[:] = [elem.replace('/', '\\') for elem in mylist]
else:
    slash = '/'
def f_start():
    print('Привет!')
    f_init()
f_start()
while True:
    currdir = os.path.normcase(os.getcwd()) + slash
    str = input('[' + currdir + ']$: ')
    if (str == '/h'):
        print('ХЕЛП')
        f_init()
    elif (str == '/f'):
        print('Поиск файла/директории')
        print('Введите имя файла/директории:')
        fd = input('$: ')
        arr = glob.glob('**{0}*{1}'.format(slash, fd), recursive=True)
        if (len(arr) == 0):
            print('Ничего не найдено :('.format(fd))
        else:
            print('найдено {0} совпадений:'.format(len(arr)))
            for elem in arr:
                print(elem)
    elif (str == '/d'):
        print('Удаление файла/директории')
        print('Введите имя:')
        fd = input('$: ')
        slashindex = fd.rfind(slash, 0)
        dirpath = fd[0:slashindex + 1]
        filename = fd[slashindex + 1:]
        if (os.path.exists(fd)):
            if (os.path.isfile(fd)):
                try:
                    os.remove(fd)
                    print('{0} успешно удалено '.format(filename) +
                          'в директории/ {0}'.format(currdir + dirpath))
                except IOError as e:
                    print('удалить нельзя {0}'.format(filename))
                print('Директория:')
                for elem in os.listdir(currdir + dirpath):
                    print(elem)
            elif (os.path.isdir(fd)):
                try:
                    os.rmdir(fd)
                    print('{0} успешно удалено'.format(fd))
                except IOError as e:
                    print('{0} упс, тут не пусто.'.format(fd))
                    harddelete = input('Удалить даже если не пустой? y/n : ')
                    if (harddelete == 'y'):
                        shutil.rmtree(fd)
        else:
             print('{0} не найдено'.format(fd))
    elif (str == '/r'):
        print('изменить название файла или директории')
        print('введите имя директории/файла:')
        fnames = input('$: ').split()
        if os.path.exists(fnames[0]):
            try:
                os.rename(fnames[0], fnames[1])
            except IOError as e:
                print('невозможно переименовать {0}'.format(fnames[0]))
        else:
            print('{0} не найдено'.format(fnames[0]))
    elif (str == '/c'):
        print('сменить директорию')
        print('введите имя директории:')
        fd = input('$: ')
        if (os.path.exists(fd)):
            os.chdir(fd)
        else:
            print('директория {0} не существует'.format(fd))
    elif (str == '/q'):
        print('Завершение программы...')
        break