from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    day = "четверг"
    # template = loader.get_template("hello1/index.html")
    # text = template.render({'my_var': day})
    # return HttpResponse(text)
    return render(request, "hello1/index.html", {'my_var': day})


def news(request):
    return render(request, 'hello1/news.html')


def managment(request):
    return render(request, 'hello1/managment.html')


def about(request):
    return render(request, 'hello1/about.html')


def contacts(request):
    return render(request, 'hello1/contacts.html')


def page_not_found(request, exception=None):
    response = render(request, "hello1/404.html")
    response.status_code = 404
    return response

def branches(request, country_name=""):
    if country_name == "":
        country_name = "всех городах"
    return render(request, 'hello1/branches.html', {"country_name": country_name})

