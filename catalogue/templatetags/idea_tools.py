from django import template

register = template.Library()

def to_percent(value):
    return round((value/5)*100)



def experience_to_text(value):
    if value == 1:
        return "keine"
    elif value == 2:
        return "wenig"
    elif value == 3:
        return "etwas"
    elif value == 4:
        return "viel"
    elif value == 5:
        return "sehr viel"
    else:
        return "unbekannt"

def effort_to_text(value):
    if value == 1:
        return "minimal"
    elif value == 2:
        return "wenig"
    elif value == 3:
        return "etwas"
    elif value == 4:
        return "viel"
    elif value == 5:
        return "sehr viel"
    else:
        return "unbekannt"

def people_span(value):
    min = value.min_required_people
    max = value.max_required_people
    if max is None:
        return f"min. {min}"
    else:
        return f"{min} bis {max}"


register.filter("to_percent", to_percent)
register.filter("experience_to_text", experience_to_text)
register.filter("effort_to_text", effort_to_text)
register.filter("people_span", people_span)