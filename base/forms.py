from django import forms
from .models import Contact, Live_Chat


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"
        
class LiveChatForm(forms.ModelForm):

    class Meta:
        model = Live_Chat
        fields = "__all__"
