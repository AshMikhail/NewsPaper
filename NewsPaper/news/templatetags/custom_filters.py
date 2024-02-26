from django import template


register = template.Library()

@register.filter()
def censor(text):
    text = str(text)
    _dict = ["новость", "заглавие", "профессор"]
    for word in _dict:
        w = word.lower()
        text = text.replace(w, w[0]+'*'*(len(w)-1))
        text = text.replace(w.title(), w.title()[0]+'*'*(len(w)-1))
    return text