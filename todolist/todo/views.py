from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create list of tasks

# create a django form
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")


def index(request):
    # Check if there already exists a "tasks" key in our session
    if "tasks" not in request.session:
        # If not, create a new list
        request.session["tasks"] = []

    return render(request, "todo/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        #save the data user submitted in a variable form
        form = NewTaskForm(request.POST)
        #check if data is valid(server-side) and access task subbmited using 'cleaned' form data
        if form.is_valid():
            task = form.cleaned_data["task"]
            #add task to the list of tasks
            request.session["tasks"] += [task]
            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("todo:index"))
        # If the form is invalid, re-render the page passing in form info to show the errors made
        else:
            return render(request, "todo/add.html", {
                "form": form
            })

    # if user just Gets the page, render empty form   
    return render(request, "todo/add.html", {
        "form": NewTaskForm
    })