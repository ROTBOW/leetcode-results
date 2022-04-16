'''
The Author is a program that auto-fills the readme with links to all the files in this repo.
'''
from file_locas import folder_loca, readme
import re
import os

leet_files = []


def grab_title(filename):
    with open(folder_loca+'\\'+filename, 'r') as file:
        return re.match(r"TITLE = '(?P<title>.+)'", file.readline()).group('title')

def replace_zeros_with_spaces(string):
    result = ''
    while string.startswith('0'):
        result += '_'
        string = string[1:]
    return result + string


if __name__ == '__main__':
    for dirName, subDir, fileList in os.walk(folder_loca):
        for fname in fileList:
            if fname.startswith('leet'):
                leet_files.append(fname)
    leet_files.sort()

    with open(readme, 'w') as file:
        file.write(f'# leet-results  -  ({len(leet_files)}) solutions\n\n\n')
        for leet in leet_files:
            title = grab_title(leet)
            file.write(f'* [{replace_zeros_with_spaces(leet[5:-3])} - {title.title()}](https://github.com/ROTBOW/leetcode-results/blob/main/{leet})\n')
    print(f'Author: done. You\'ve completed {len(leet_files)} problems')