from django.shortcuts import render

from . import util
from markdown2 import Markdown
from django.http import HttpResponseNotFound

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, slug):
    markdowner = Markdown()
    entry = util.get_entry(slug)
    
    if(entry != None):
        entry = markdowner.convert(entry)
        return render(request, "encyclopedia/entries.html", {
            "entry": entry
        })
    else:
        return HttpResponseNotFound('<h1>Error 404: Page not found</h1>')

def search(request):
    query = request.GET.get('q')
    
    if query in util.list_entries():
        return(entries(request, query))

    results =  util.search_entries(query)
    return render(request, "encyclopedia/search.html", {
        "entries": results
    })