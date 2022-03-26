from django import forms


class NewMessageForm(forms.Form):
    recipient = forms.CharField(label='Recipient name', max_length=100)
    content = forms.CharField(label='Content info', max_length=100)
    subject = forms.CharField(label='subject', max_length=100)