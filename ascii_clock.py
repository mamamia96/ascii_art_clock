from os import system  
import platform
import time


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def load_characters():
    line_list = [[] for i in range(10)]

    for i in range(10):
        with open('C:\\Users\\matthewabbott\\Documents\\programming_files\\python\\ascii_lib\\' + str(i) + '.txt','r') as file:
            for line in file:
                line_list[i].append(line.replace('\n',''))

    return line_list

def print_ascii(a_list,t_list):
    tm_str = ''
    for i in range(20):
        print(a_list[t_list[0]][i],end='')
        print(" " * 5,end='')
        print(a_list[t_list[1]][i],end='')
        print(" " * 15,end='')
        print(a_list[t_list[2]][i],end='')
        print(" " * 5,end='')
        print(a_list[t_list[3]][i],end='')
        print(" " * 15,end='')
        print(a_list[t_list[4]][i],end='')
        print(" " * 5,end='')
        print(a_list[t_list[5]][i],end='')
        print()

def list_maker():
    curr = []
    h = time.localtime()[3]
    m = time.localtime()[4]
    s = time.localtime()[5]
    if len(str(h)) == 1:
        curr.append(0)
        curr.append(h)
    else:
        curr.append(int(str(h)[0]))
        curr.append(int(str(h)[1]))

    
    if len(str(m)) == 1:
        curr.append(0)
        curr.append(m)
    else:
        curr.append(int(str(m)[0]))
        curr.append(int(str(m)[1]))

    if len(str(s)) == 1:
        curr.append(0)
        curr.append(s)
    else:
        curr.append(int(str(s)[0]))
        curr.append(int(str(s)[1]))
    
    return curr



ascii_lib = load_characters()



i = 30

curr = list_maker()
while i > 0:
    tmp = list_maker()
    if tmp != curr:
        clean()
        print_ascii(ascii_lib, curr)
        curr = list_maker()
        