s = """
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script></head><body
class=" fixed  top-bar top-menu off-canvas-right"><div
id="jm-allpage"><div
id="jm-page"><div
id="jm-offcanvas"><div
"""


def without_doctype(s):
    s = s[s.index("<body"):]
    return s

print(without_doctype(s))

print(len("Но Tesla Model S Signature Perfomance полностью ломает любые стереотипы. Запас"))