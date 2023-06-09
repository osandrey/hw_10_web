from django.forms import (
    ModelForm,
    CharField,
    TextInput,
    ValidationError,
    ModelMultipleChoiceField,
    SelectMultiple,
    Textarea,
    ModelChoiceField,
    Select,
                          )
from .models import Quote, Author, Tag


# class CreateQuoteForm(ModelForm):
#     quote = CharField(max_length=30, required=True, widget=TextInput())
#     tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), required=True, widget=SelectMultiple())
#     author = CharField(max_length=30, required=True, widget=TextInput())
#
#
#     class Mete:
#         model = Quote
#         fields = ['quote', 'tags', 'author']
#         # exclude = ['tags']


class QuoteModelForm(ModelForm):

    quote = CharField(widget=Textarea)
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"), required=True, widget=SelectMultiple)
    author = ModelChoiceField(queryset=Author.objects.all().order_by("fullname"), widget=Select())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].label_from_instance = lambda obj: obj.fullname
        self.fields['tags'].label_from_instance = lambda obj: obj.name

    class Meta:
        model = Quote
        fields = [
            'quote', 'tags', 'author',
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'fuck':
            raise ValidationError("This is not a valid title")
        return title


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput())
    born_date = CharField(max_length=50, widget=TextInput())
    born_location = CharField(max_length=150, widget=TextInput())
    bio = CharField(widget=Textarea)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'bio']


class TagForm(ModelForm):
    name = CharField(max_length=50, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']