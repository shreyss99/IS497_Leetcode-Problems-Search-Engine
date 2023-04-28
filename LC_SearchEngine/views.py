from django.contrib import messages
from django.db import connection
from django.db.models import Q
from django.shortcuts import render, redirect
from LC_SearchEngine.database import get_data
from LC_SearchEngine.forms import QueryForm
from LC_SearchEngine.models import LeetcodeData
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "LC_SearchEngine/home.html")


def about_us(request):
    return render(request, "LC_SearchEngine/about_us.html")


@login_required()
def data_view(request):

    fetched_data = get_data()
    context = {"fetched_lc_data": {obj.id: obj for obj in fetched_data}}
    return render(request, "LC_SearchEngine/data.html", context)


@login_required()
def query_and_display(request):

    form = QueryForm()

    if request.method == 'POST':
        form = QueryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            is_premium = form.cleaned_data.get('is_premium')
            difficulty = form.cleaned_data.get('difficulty')
            companies = form.cleaned_data.get('companies')
            related_topics = form.cleaned_data.get('related_topics')
            asked_by_faang = form.cleaned_data.get('asked_by_faang')

            with connection.cursor() as cursor:
                cursor.execute(f""" SELECT id, title, url FROM "LC_SearchEngine_leetcodedata" WHERE 
                                    title LIKE '%{title}%' AND
                                    is_premium = {is_premium} AND
                                    difficulty = '{difficulty}' AND
                                    companies LIKE '%{companies}%' AND
                                    related_topics LIKE '%{related_topics}%' AND
                                    asked_by_faang = {asked_by_faang} """)

                fetched_lc_data = cursor.fetchall()

            context = {"form": form, "fetched_lc_data": fetched_lc_data}
            return render(request, "LC_SearchEngine/data.html", context)

    context = {"form": form}
    return render(request, "LC_SearchEngine/forms.html", context)
