from django import template

register = template.Library()

def to_percent(value):
    if value == 0:
        return 5
    return round((value/5)*100)

def people_span(value):
    min = value.min_required_people
    max = value.max_required_people
    if max is None:
        return f"min. {min}"
    else:
        return f"{min} bis {max}"


register.filter("to_percent", to_percent)
register.filter("people_span", people_span)