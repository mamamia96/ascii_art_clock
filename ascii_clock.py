from os import system  
import platform
import time
import os
import sys
import random

ASCII_HEIGHT = 18
DIGIT_NUM = 8
CLOCK_W = 134
CLOCK_H = 22

os.system('mode con: cols=150 lines=50')

TERM_W, TERM_H = os.get_terminal_size()
print("TW: ",TERM_W)
print("TH: ",TERM_H)
input()

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
    line_list = [[] for i in range(11)]
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for i in range(10):
        with open(dir_path + '\\ascii_lib\\' + str(i) + '.txt','r') as file:
            for line in file:
                line_list[i].append(line.replace('\n',''))
        
    with open(dir_path + '\\ascii_lib\\colon.txt','r') as f:
        for line in f:
            line_list[len(line_list) - 1].append(line.replace('\n',''))
    
    ans = input('random characters for clock?: (y/n) ')
    if ans == 'n':
        return line_list
    elif ans == 'uwu':
        alph = 'uwu'
    elif ans == 'owo':
        alph = 'owo'
    else:
        #alph = 'abcdefghijklmnopqrstuvwxyz'
        alph = '1234567890'

    for li in range(len(line_list)):
        for i in range(len(line_list[li])):
            tmp = ''
            j = 0

            for char in line_list[li][i]:
                if char != ' ':
                    if len(alph) < 5:
                        j += 1
                        if j > len(alph) - 1:
                            j = 0
                        tmp += alph[j]
                        
                    else:
                        tmp += alph[random.randint(0,len(alph) - 1)]
                else:
                    tmp += ' '
            line_list[li][i] = tmp

    return line_list

def print_ascii(a_list,t_list,h_move_count,v_move_count):
    for v in range(v_move_count):
        print()
    for i in range(ASCII_HEIGHT):
        for j in range(DIGIT_NUM):
            if j == 0: print(" " * h_move_count,end='')
            if str.isdigit(str(t_list[j])):
                
                print(a_list[t_list[j]][i],end='')

            else:
                print(a_list[len(a_list) - 1][i],end='')

            #print(" " * 5,end='')

        print()


        
def list_maker():
    curr = []
    h = time.localtime()[3]
    m = time.localtime()[4]
    s = time.localtime()[5]
    if h > 12:
        h = h - 12

    if len(str(h)) == 1:
        curr.append(0)
        curr.append(h)
    else:
        curr.append(int(str(h)[0]))
        curr.append(int(str(h)[1]))

    curr.append(':')
    
    if len(str(m)) == 1:
        curr.append(0)
        curr.append(m)
    else:
        curr.append(int(str(m)[0]))
        curr.append(int(str(m)[1]))

    curr.append(':')

    if len(str(s)) == 1:
        curr.append(0)
        curr.append(s)
    else:
        curr.append(int(str(s)[0]))
        curr.append(int(str(s)[1]))

    return curr

ascii_lib = load_characters()
#quick and dirty cause im lazy

i = 30
h_move = 0
h_move_val = 1
v_move = 0
v_move_val = 1
curr = list_maker()
while i > 0:
    tmp = list_maker()
    if tmp != curr:
        clean()
        if h_move + CLOCK_W > TERM_W:
            h_move = h_move - 2
            h_move_val *= -1
        elif h_move  < 1:
            h_move += 2
            h_move_val *= -1
        
        if v_move + CLOCK_H > TERM_H:
            v_move = v_move - v_move_val - 1
            v_move_val *= -1
        elif v_move  < 2:
            v_move = v_move + v_move_val + 1
            v_move_val *= -1
        v_move += v_move_val
        h_move += h_move_val
        print_ascii(ascii_lib, curr,h_move, v_move)
        curr = list_maker()
 
        
        
