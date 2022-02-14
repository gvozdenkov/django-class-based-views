from dataclasses import field, fields
from django import forms

from hello.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        labels = {
            "username": "Enter your name",
            "message": "Enter your message"
        }