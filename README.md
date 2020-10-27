# Scrapper Wordlist

## Presentation

This tool scraps a specified website and creates wordlist from its content.

## Usage

    scrapper_wordlist.py <url> [-a|-w] <output>

* url: source to scrap (ie. https://www.python.org/)
* output: file to write scrapped data as a wordlist (ie. my_wordlist.txt)

* [-a|-w]: those are optionnals :
  * -a : append to a file
  * -w : write to a file (this option erase the file content)

By default it appends to file.

## Examples

### Without any arguments

    scrapper_wordlist.py https://www.python.org/ my_wordlist.txt

This commands will append the new content to the file. Duplicates will not be added. If the file does not exist then it will be created.

### With -a argument

    scrapper_wordlist.py https://www.python.org/ -a my_wordlist.txt

Equivalent to above command.

### With -w argument

    scrapper_wordlist.py https://www.python.org/ -w my_wordlist.txt

This command will write content to the file. If the file exists then the content will be erased.

# Notes

This tool has been developped during my free time.

Feel free to copy, modify and share !
