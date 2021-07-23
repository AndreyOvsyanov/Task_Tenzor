import re as Regex

s = """
<div class="random_class">
    Какой-то текст
</div>

<div href="https://" class="dada" id="da">
    text_after
    <div class="ad">
        text
    </div>
    text_before
</div>
"""

class Example():

    #Текст
    s: str = ""
    #Изменённый текст
    rS: str = ""


    def __init__(self, s):
        self.s = s


    def without_div(self):
        self.rS = Regex.sub(
            r'<div.*>|</div>', #Поиск всех divов, в которых присутствуют классы, id и т.д
            '', #Заменяющий символ
            self.rS #Строка для поиска
        )

    def without_doctype(self):
        self.rS = self.s[self.s.index("<body"):]


    def title_text(self):
        self.title = Regex.findall(r'<title>.*</title>', self.s)
        self.title = Regex.sub(r'<title>|</title>', '', self.title[0])
        return self.title


    def print_rS(self):
        print(self.rS)


    def without_tab(self):
        for s in self.rS.splitlines():
            s = Regex.sub(r'    ', '', s)
            s = Regex.sub(r'\n', '', s)
            print(s)


#example = Example(s)
#example.without_div()
#example.print_rS()
#example.without_tab()

def without_tag(stroka):

    stroka = stroka[stroka.index("<body"):stroka.index("</body>")]
    return stroka

def without_d(stroka):
    stroka = Regex.findall(
        r'<body.*>|</body>',
        stroka
    )



#print(stroka)
#print(without_tag(stroka))