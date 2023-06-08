import os
import django

from pymongo import MongoClient


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_toscrape.settings")
django.setup()

from quotes.models import Quote, Tag, Author    # noqa

uri = "mongodb+srv://osandreyman:1111@firstcluster.g6svumr.mongodb.net/hw?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.hw

authors = db.author.find()

for author in authors:
    Author.objects.get_or_create(
    fullname = author['fullname'],
    born_date = author['born_date'],
    born_location = author['born_location'],
    bio = author['bio'],

)

quotes = db.quote.find()

for quot in quotes:
    tags = []
    for tag in quot['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quot['quote'])))

    if not exist_quote:
        author = db.author.find_one({"_id": quot['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote=quot['quote'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)

