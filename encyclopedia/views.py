from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .form import *
from . import util
import random


def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            page = form.cleaned_data["page"]
            if page in util.list_entries():
                return HttpResponseRedirect(reverse('get_page',
                       args=(form.cleaned_data['page'],)))
            else:
                return HttpResponseRedirect(reverse('search_result',
                       args=(form.cleaned_data['page'],)))
    else:
        form = SearchForm()

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": form
    })

def get_page(request, entry):
    return render(request, "encyclopedia/entry.html",{
        "entry": entry,
        "content": util.get_entry(entry)
    })

def search(request, sub):
    if "words" not in request.session:
        request.session["words"] = []
    for word in util.list_entries():
        if sub in word:
            request.session["words"] += [word]
    return request.session["words"]

def search_result(request, sub):
    result = search(request, sub)
    del request.session['words']
    return render(request, "encyclopedia/search_result.html", {
        "results": result
    })

def create_new_page(request):
    if request.method == "POST":
        new_page = CreatePage(request.POST)
        if new_page.is_valid():
            title = new_page.cleaned_data["title"]
            content = new_page.cleaned_data["content"]
            if title not in util.list_entries():
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('get_page',
                       args=(new_page.cleaned_data['title'],)))
            else:
                messages.error(request, 'This entry already exists')
    else:
        new_page = CreatePage()
    return render(request, "encyclopedia/new_page.html",{
        "new_page": new_page
    })

def edit_page(request, entry):
    if request.method == "POST":
        edit = Edit(request.POST, initial={'new_content': util.get_entry(entry)})
        if edit.is_valid():
            new_content = edit.cleaned_data["new_content"]
            util.save_entry(entry, new_content)
            return HttpResponseRedirect(reverse('get_page',
                   args=(entry,)))
        else:
            print(edit.errors)
    else:
        edit = Edit(initial={'new_content': util.get_entry(entry)})
    return render(request, "encyclopedia/edit.html", {
        "entry": entry,
        "edit": edit
    })

def random_page(request):
    randomp = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse('get_page',
           args=(randomp,)))
