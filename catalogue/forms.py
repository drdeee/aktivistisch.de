from django import forms

class ContactForm(forms.Form):
    template_name = "catalogue/contact.html"

    name = forms.CharField(max_length=100, label="Dein Name", required=False)
    contact = forms.CharField(max_length=100, label="Kontaktmöglichkeit", required=False)
    message = forms.CharField(widget=forms.Textarea, label="Deine Nachricht")