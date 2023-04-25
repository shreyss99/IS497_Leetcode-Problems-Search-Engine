from django.shortcuts import render
from LC_SearchEngine.database import get_data
from LC_SearchEngine.forms import QueryForm
from LC_SearchEngine.models import LeetcodeData


def home(request):
    return render(request, "LC_SearchEngine/home.html")


def about_us(request):
    return render(request, "LC_SearchEngine/about_us.html")


def display_query_form(request):
    form = QueryForm()
    context = {'form': form}
    return render(request, "LC_SearchEngine/forms.html", context)


def data_view(request):

    fetched_data = get_data()
    context = {"fetched_lc_data": {obj.id: obj for obj in fetched_data}}
    return render(request, "LC_SearchEngine/data.html", context)
