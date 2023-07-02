from django.forms import ModelForm, CharField, TextInput
from django import forms
from .models import Tag, Note, Quote


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class NoteForm(ModelForm):

    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Note
        fields = ['name', 'description']
        exclude = ['tags']



# class QuoteForm(forms.ModelForm):
#
#     class Meta:
#         model = Quote
#         fields = ['title', 'description', 'price']



class RawQuoteForm(forms.Form):

    title = forms.CharField(label='Title ', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Your description",
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "rows": 20,
            "cols": 12
        }
        )
    )
    price = forms.DecimalField(initial=199.99)
