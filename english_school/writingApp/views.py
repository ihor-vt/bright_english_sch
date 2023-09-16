from django.shortcuts import render

from .models import TextEditor


def homepage(request):
    """
    The homepage function is the first function that will be called
    when a user visits the website. It will render the homepage.html template,
    which contains all of our HTML code for our website's homepage.

    :param request: Get the request from the user
    :return: The homepage
    """
    text = TextEditor.objects.all()
    context = {
        'text': text
    }
    return render(request, "writingApp/homepage.html", context)
