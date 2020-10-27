#!/usr/bin/env python3

import sys,os
import requests
from bs4 import BeautifulSoup
import re

"""
Return all text in body tag
"""
def scrap_words(source):
    soup = BeautifulSoup(source, "lxml")
    text = soup.find('body').text
    return text

"""
Create wordlist from text
"""
def create_wordlist(text):
    text = text.replace("\r"," ").replace("\n"," ").replace(".", "").replace(",", "").replace(";", "")
    words = text.split(" ")
    wordlist = []
    for word in words:
        if word and word not in wordlist:
            wordlist.append(word)
    return wordlist

"""
Write list of words in the file given in argument
Duplicates are not added
"""
def write_wordlist(wordlist, output, write_mode):
    f = open(output, write_mode)
    for word in wordlist:
        word = word + "\n"
        if not is_duplication(word, get_existant_wordlist(output)):
            f.write(word)
    f.close()

"""
Check if word exists in list
"""
def is_duplication(word, wordlist):
    return word in wordlist

"""
Return the content of the file given in agument as a list
"""
def get_existant_wordlist(file):
    f = open(output, "r")
    wordlist = f.readlines()
    f.close()
    return wordlist

tool_desc = """This tool create a wordlist from a given website """
usage = """
Usage: scraper_wordlist.py <url> [-a|-w] <output>
    <url>: source to scrap (ie. https://www.python.org/)
    <output>: file to write scrapped data as a wordlist (ie. my_wordlist.txt)

    [-a|-w]: those are optionnals
        -a : append to a file
        -w : write to a file (this option erase the file content)
    By default, it appends to file
"""
if __name__ == '__main__':
    print(tool_desc)
    if len(sys.argv) == 4:
        output = sys.argv[3]
        if sys.argv[2] in ["-a", "-w"]:
            write_mode = sys.argv[2].replace("-", "")
    elif len(sys.argv) == 3 and sys.argv[2] not in ["-a", "-w"]:
        output = sys.argv[2]
        write_mode = "a"
    else:
        print(usage)
        sys.exit()
    source = requests.get(sys.argv[1]).text
    body_text = scrap_words(source)
    wordlist = create_wordlist(body_text)
    write_wordlist(wordlist, output, write_mode)
