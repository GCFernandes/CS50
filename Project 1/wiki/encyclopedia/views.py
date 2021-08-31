from django.shortcuts import render

from . import util
from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, slug):
    file = open("entries/" + slug + ".md", "r")
    markdowner = Markdown()
    html = markdowner.convert(file.read())
    return render(request, "encyclopedia/entries.html", {
        "entry": html
    })