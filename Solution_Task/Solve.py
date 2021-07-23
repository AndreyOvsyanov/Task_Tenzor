#-*-coding:utf8-*-
import sys
import requests
from requests.exceptions import HTTPError
from Solution_Task.Example import Example
from Solution_Task.Operation import get_text, without_tag

url = sys.argv[1] if len(sys.argv) > 1 else input()

try:
    res = requests.get(url)
    if res.status_code == 200:
        print("Connection successful")

        print(len(res.text))
        #print(res.text)

        text = res.text

        example = Example(text)

        with open('file.txt', 'wt') as file:
            file.write("\t" + example.title_text() + "\n\n")


            while "</p>" in text:
                file.write(without_tag(get_text(text)))
                text = text[text.index("</p>") + 4:len(text)]

        print("Файл в директории перезаписан")

        #example = Example(res.text)
        #print("="*50)
        #print(example.title_text())
        #example.without_doctype()
        #example.print_rS()
        #print(len(example.rS))







    

except HTTPError:
    print(f'HTTP error occerred: {HTTPError}')
except ConnectionError:
    print(f'Connection if failed: {ConnectionError}')
except Exception as err:
    print(f'Unknown error: {err}')
