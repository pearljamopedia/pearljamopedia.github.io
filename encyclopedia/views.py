from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

import random
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Define a new Form for searching pages.
class SearchPageForm(forms.Form):
    q = forms.CharField(label='', min_length=1)


def search_page(request):
    if request.method == "POST":
        form = SearchPageForm(request.POST)
        results = list()

        if form.is_valid():
            title = form.cleaned_data["q"]

            entries = util.list_entries()
            results = [entry for entry in entries if title in entry]

            if len(results) == 1:
                if title == results[0]:
                    return get_page(request, results.pop())

        return render(request, "encyclopedia/search.html", {
            "entries": results
        })


def get_page(request, title):
    content = util.get_entry(title=title)
    if content is None:
        raise Http404("Requested page does not exist!")

    # title is present. Convert markdown content to HTML.
    md = Markdown()
    html_content = md.convert(content)

    return render(request, "encyclopedia/entry.html", {
        "entry_title": title,
        "entry_content": html_content
    })


def random_page(request):
    entries = util.list_entries()

    if entries:
        random_index = random.randint(0, len(entries)-1)
        random_title = entries[random_index]
        return HttpResponseRedirect(reverse("get_page",
            kwargs={"title": random_title}))
    else:
        raise Http404("No pages found!")


def new_page(request):
    return render(request, "encyclopedia/create.html")


# Define a new Form for creating a new page.
class CreatePageForm(forms.Form):
    page_title = forms.CharField(label='', min_length=1)
    page_content = forms.CharField(label='', min_length=1)


def create_page(request, operation):
    if request.method == "POST":
        if operation == "save":
            form = CreatePageForm(request.POST)

            if form.is_valid():
                page_title = form.cleaned_data["page_title"]
                page_content = form.cleaned_data["page_content"]

                if util.get_entry(page_title) is None:
                    util.save_entry(page_title, page_content)
                    return HttpResponseRedirect(reverse("get_page", kwargs={
                        "title": page_title
                    }))
                else:
                    raise Http404("Page with same title already exists!")
            else:
                message = ""
                for field in form.errors:
                    message += f"Field: {field}\nErrors: \n"
                    for error in form.errors[field]:
                        message += f"{error}\n"

                return render(request, "encyclopedia/error.html", {
                    "message": f"Invalid input.\n{message}"
                })
        else:
            return HttpResponseRedirect(reverse("index"))


def edit_page(request, title=''):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "page_title": title,
        "page_content": content
    })


# Define a new Form for updating edited page.
class EditPageForm(forms.Form):
    page_content = forms.CharField(label='', min_length=1)


def update_page(request, title, operation):
    if request.method == "POST":
        if operation == "save":
            form = EditPageForm(request.POST)

            if form.is_valid():
                page_content = form.cleaned_data["page_content"]

                util.save_entry(title, page_content)
        return HttpResponseRedirect(reverse("get_page", kwargs={
            "title": title
        }))
