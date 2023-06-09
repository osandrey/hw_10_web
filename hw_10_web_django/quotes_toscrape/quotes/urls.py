
from django.urls import path
from .views import main, about_author, QuoteCreateView, AuthorCreateView, TagCreateView, TagView, top_tags_view


app_name = "quotes"
urlpatterns = [
    path('', main, name="root"),
    path('<int:page>', main, name="root_paginate"),
    path('author/<int:_id>', about_author, name='about_author'),
    path('create/', QuoteCreateView.as_view(), name='quote-create'),
    path('addauthor/', AuthorCreateView.as_view(), name='add-author'),
    path('addtag/', TagCreateView.as_view(), name='add-tag'),
    path('tag/<str:id>', TagView.as_view(), name='TagView'),
    path('top/', top_tags_view, name='top_tags_view')
]