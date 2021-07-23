#-*-coding:utf8-*-
import re

s = """<p>Da</p></div><p 
style="text-align: justify;">В обществе пока считают, что электромобиль просто не может быть удобным и быстрым. Но <strong>Tesla Model S Signature Perfomance</strong> полностью ломает любые стереотипы. Запас хода этого автомобиля 480 км, его<strong> максимальная скорость 209 км/ч</strong>. Удивляет и <strong>разгон машины за 4,4 секунды до 100 км/ч</strong>! Полностью заряжается за 5 часов от 220 В. <br
/> Но на особых станциях<strong> машину можно зарядить и за 30 минут.</strong> Сегодня Tesla Model S - самый безопасный серийным автомобиль, который когда либо создавался человеком. <br
/> Также автомобиль был удостоен по всем тестам 5 звездам NCAP. Самое приятное то, что все эти плюсы при нулевом выбросе CO2. <br
/><br
/><br
/> Лялюк Анна</p>
<div
class="addtoany_container"><span
class="a2a_kit a2a_kit_size_32 addtoany_list" data-a2a-url="https://russianyellowpages.us/ru/articles/interesting-short-articles/4972-luchshij-jelektromobil-tesla-model-s-signature-perfomance.html" data-a2a-title="Лучший электромобиль Tesla Model S Signature Perfomance">
<a
class="a2a_button_facebook"></a>
<a
class="a2a_button_twitter"></a>
<a
class="a2a_button_google_plus"></a>
<a
class="a2a_dd" href="https://www.addtoany.com/share"></a>
</span></div>
"""


def get_text(s):

    stroka = s[s.index("<p"):s.index("</p>")]

    stroka = re.sub(
        r'\n',
        '',
        stroka
    )

    stroka = re.sub(
        r'<p.*">|<p>',
        '',
        stroka
    )

    stroka = re.sub(r'\n', '', stroka)
    st = re.sub(r'<br/>', '\n', stroka)
    st = re.sub(r'<strong>|</strong>', '', st)

    text: str = ""

    for splitln in st.splitlines():
        words = splitln.split(' ')
        if '' in words:
            words.remove('')
        lines: str = ""
        line: str = "\t"
        for word in words:
            if len(line) + len(word) > 80:
                lines += line + '\n'
                line = ""
            else:
                line += word + " "
        lines += line + "\n"

        text += lines







    return text

def without_tag(s):
    st = re.sub(
        r'<.*>|</.*>',
        '',
        s
    )
    return st

#get_text(s)
#s = s[s.index("</p>") + 4:len(s)]
#print(s)
#get_text(s)