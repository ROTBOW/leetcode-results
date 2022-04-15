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



for dirName, subDir, fileList in os.walk(folder_loca):
    for fname in fileList:
        if fname.startswith('leet'):
            leet_files.append(fname)
leet_files.sort()

with open(readme, 'w') as file:
    file.write('# leet-results\n\n\n')
    for leet in leet_files:
        title = grab_title(leet)
        file.write(f'* [{title.title()}](https://github.com/ROTBOW/leetcode-results/blob/main/{leet})\n')