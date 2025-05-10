from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import translation


def index(request):
    """
    Render the landing page for La Petite Académie.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered index page.
    """
    return render(request, "daycare/index.html")


def set_language(request, lang_code):
    """
    Set the user's language preference and redirect to the referring page.

    Args:
        request: The HTTP request object.
        lang_code (str): The language code to set (e.g., 'fr', 'en').

    Returns:
        HttpResponseRedirect: Redirect to the referring page or home.
    """
    if lang_code in dict(request.LANGUAGES).keys():
        translation.activate(lang_code)
        response = redirect(request.META.get("HTTP_REFERER", reverse("index")))
        response.set_cookie("django_language", lang_code)
        return response
    return redirect("index") 
