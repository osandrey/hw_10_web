from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    View,

)

from .models import Author, Quote, Tag
from .forms import AuthorForm, TagForm, QuoteModelForm

# Create your views here.


def main(request, page=1):
    # db = get_mongo_db()
    # quotes = db.quote.find()

    quotes = Quote.objects.all()
    top_tags = Tag.get_top_ten_tags()
    # print(top_tags)
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', {"quotes": quotes_on_page, 'top_tags': top_tags})


def about_author(request, _id):

    author = Author.objects.get(pk=_id)
    return render(request, "quotes/author.html", {"author": author})



def top_tags_view(request):
    top_tags = Tag.get_top_ten_tags()
    context = {'top_tags': top_tags}
    return render(request, 'quotes/top_ten.html', context)




class TagbjectMixin(object):
    model = Tag
    def get_object(self):
        name = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, name=name)
        return obj


# def view_tags(request, tag_name):
#     tag = TagbjectMixin()
#     print(tag)
#     data = tag.get_data()
#     print(data)
#     return render(request, "quotes/view_tag.html", {"all_tag": tag})

class TagView(TagbjectMixin, View):
    template_name = "quotes/view_tag.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        tag = self.get_object()
        quotes = Quote.objects.filter(tags=tag)

        # GET method
        context = {'tag': tag, 'quotes': quotes}
        return render(request, self.template_name, context)



class QuoteCreateView(View):
    template_name = "quotes/add_quote.html" # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = QuoteModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = QuoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = QuoteModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)



class AuthorCreateView(View):
    template_name = "quotes/add_author.html" # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = AuthorForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            form = AuthorForm()
        context = {"form": form}
        return render(request, self.template_name, context)



class TagCreateView(View):
    template_name = "quotes/add_tag.html" # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = TagForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            form = TagForm()
        context = {"form": form}
        return render(request, self.template_name, context)