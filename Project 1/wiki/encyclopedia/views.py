from django.shortcuts import render

from . import util
from markdown2 import Markdown
from django.http import HttpResponseNotFound
from random import randrange

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
            "entry": entry,
            "page_name": slug
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

def editor(request, slug):
    if(request.method == 'POST'):
        content = request.POST.get("entry_content")
        title = content.split('\n')[0]
        title = title.replace("#", "")
        title = title.replace(" ", "")
        title = title.replace("\r", "")

        util.save_entry(title, content)

    entry = util.get_entry(slug)
    if(entry == None):
        entry = ""
    return render(request, "encyclopedia/editor.html", {
        "entry": entry
    })

def new_page(request):
    return editor(request, None)

def random_page(request):
    all_entries = util.list_entries()
    selected = all_entries[randrange(len(all_entries))]
    return(entries(request, selected))
