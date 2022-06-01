'''
The Author is a program that auto-fills the readme with links to all the files in this repo.
It uses the file_locas.py file (which isn't in this repo) to find the solutions and the readme.
the file only contains the two varibles, folder_loca and readme, which are both strings of the paths
to the solutions and readme respectively.
'''
from file_locas import folder_loca, readme
from alive_progress import alive_bar
from collections import namedtuple
import timeit
import sys
import re
import os


def grab_title(filename) -> str:
    with open(folder_loca+'\\'+filename, 'r') as file:
        return re.match(r"TITLE = '(?P<title>.+)'", file.readline()).group('title')

def replace_zeros_with_spaces(string) -> str:
    result = ''
    while string.startswith('0'):
        result += '_'
        string = string[1:]
    return result + string

def get_files():
    leet_files = []
    for dirName, subDir, fileList in os.walk(folder_loca):
        for fname in fileList:
            if fname.startswith('leet'):
                leet_files.append(fname)
    return leet_files

def update_readme() -> None:
    leet_files = sorted(get_files())

    with open(readme, 'w') as file:
        file.write(f'# Leet-Results  -  ({len(leet_files)}) solutions\n\n\n')
        for idx, leet in enumerate(leet_files):
            title = grab_title(leet)
            file.write(f'{idx+1}. [{replace_zeros_with_spaces(leet[5:-3])} - {title.title()}](https://github.com/ROTBOW/leetcode-results/blob/main/solutions/{leet})\n')
    print(f'Author: done. You\'ve completed {len(leet_files)} problems')

def check_files() -> None:
    leet_files = get_files()
    invalid_files = dict()
    for fname in leet_files:
        with open(folder_loca+'\\'+fname, 'r') as file:
            file_content = file.read().lower()
            issues = []
            if 'title = ' not in file_content:
                issues.append('Is missing a TITLE!')
            if 'time:' not in file_content:
                issues.append('Is missing TIME!')
            if 'space:' not in file_content:
                issues.append('Is missing SPACE!')
            if 'results:' not in file_content:
                issues.append('Is missing RESULTS!')
            if len(issues) > 0:
                invalid_files[fname] = issues
    for v, k in invalid_files.items():
        print('Author:', v, k)
    print(f'Author: Total ({len(invalid_files)}) files are missing stuff')
                


def add_zeros(num) -> str:
    num = str(int(num))
    return '0000'[:abs(4 - len(num))] + num
    

def create_new_leet() -> None:
    print('Author: Okay boy, whats the title and number? separate then with a comma now.')
    data = input('-> ')
    data = data.split(',')
    with open(folder_loca+'\\'+f'leet_{add_zeros(data[1])}.py', 'w') as file:
        file.write(f"TITLE = '{data[0]}'\n")
        file.write('\'\'\'\ntime: BigO()\nspace: BigO()\n\n')
        file.write('Results:\n\n\n\'\'\'\n')
    print('Author: There you go boy.')

# the commented out code is for the self timing feature that I don't think would work.

# def get_soluion_for_time():
#     files = get_files()
#     answer = ''
#     while True:
#         answer = input('Enter Problem number: ')
#         if answer.isdigit() and 0 <= int(answer) <= 9999:
#             break

#     for file in files:
#         num = file[5:-3]
#         if num == answer:
#             answer = file

#     file_context = ''
#     with open(folder_loca+'\\'+answer) as file:
#         file_context = file.read()

#     timer(file_context, grab_title(answer))

# def timer(funcStr, funcName):
#     count = 1000
#     total_time = 0.0
#     with alive_bar(count) as bar:
#         for _ in range(count):
#             total_time += timeit.timeit(stmt=funcStr)
#             # print(timeit.timeit(stmt=funcStr))
#             bar()
#     print(f'{funcName} - {count} runs has an average time of {round(total_time / count, 2)}')

if __name__ == '__main__':
    if sys.argv == ['the_author.py']:
        update_readme()
    elif 'newfile' in sys.argv:
        create_new_leet()
        update_readme()
    elif 'check' in sys.argv:
        check_files()
    # elif 'timeit' in sys.argv:
    #     get_soluion_for_time()