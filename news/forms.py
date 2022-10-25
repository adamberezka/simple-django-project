from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['topic', 'text']

# topic
# text
# author
# create_time
# last_edit_time