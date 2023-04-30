from django.contrib import messages
from django.db import connection
from django.shortcuts import render, redirect
from LC_SearchEngine.forms import QueryForm, ProblemSubmitForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "LC_SearchEngine/home.html")


def about_us(request):
    return render(request, "LC_SearchEngine/about_us.html")


@login_required()
def query_and_display(request):

    q_form = QueryForm()

    if request.method == 'POST':
        q_form = QueryForm(request.POST)

        if q_form.is_valid():
            title = q_form.cleaned_data.get('title')
            is_premium = q_form.cleaned_data.get('is_premium')
            difficulty = q_form.cleaned_data.get('difficulty')
            companies = q_form.cleaned_data.get('companies')
            related_topics = q_form.cleaned_data.get('related_topics')
            asked_by_faang = q_form.cleaned_data.get('asked_by_faang')

            with connection.cursor() as cursor:
                if (not title) or (not difficulty) or (not companies) or (not related_topics) or (not asked_by_faang):
                    cursor.execute(f""" SELECT id, title, url FROM "LC_SearchEngine_leetcodedata" WHERE 
                                                        is_premium = {is_premium} """)

                else:
                    cursor.execute(f""" SELECT id, title, url FROM "LC_SearchEngine_leetcodedata" WHERE 
                                    is_premium = {is_premium} AND 
                                    title LIKE '%{title}%' AND
                                    difficulty = '{difficulty}' AND
                                    companies LIKE '%{companies}%' AND
                                    related_topics LIKE '%{related_topics}%' AND
                                    asked_by_faang = {asked_by_faang} """)

                fetched_lc_data = cursor.fetchall()

            context = {"form": q_form, "fetched_lc_data": fetched_lc_data}
            return render(request, "LC_SearchEngine/data.html", context)

    context = {"form": q_form}
    return render(request, "LC_SearchEngine/query_form.html", context)


@login_required()
def contribute(request):

    user = request.user
    username = user.username
    role = user.person.role

    ps_form = ProblemSubmitForm()

    if request.method == 'POST':
        if role == "contributor":

            ps_form = ProblemSubmitForm(request.POST)

            if ps_form.is_valid():
                title = ps_form.cleaned_data.get('title')
                description = ps_form.cleaned_data.get('description')
                is_premium = ps_form.cleaned_data.get('is_premium')
                difficulty = ps_form.cleaned_data.get('difficulty')
                solution_link = ps_form.cleaned_data.get('solution_link')
                acceptance_rate = ps_form.cleaned_data.get('acceptance_rate')
                frequency = ps_form.cleaned_data.get('frequency')
                url = ps_form.cleaned_data.get('url')
                discuss_count = ps_form.cleaned_data.get('discuss_count')
                accepted = ps_form.cleaned_data.get('accepted')
                submissions = ps_form.cleaned_data.get('submissions')
                companies = ps_form.cleaned_data.get('companies')
                related_topics = ps_form.cleaned_data.get('related_topics')
                likes = ps_form.cleaned_data.get('likes')
                dislikes = ps_form.cleaned_data.get('dislikes')
                rating = round((likes / (likes + dislikes) * 100))
                asked_by_faang = ps_form.cleaned_data.get('asked_by_faang')
                similar_questions = ps_form.cleaned_data.get('similar_questions')

                with connection.cursor() as cursor:
                    cursor.execute(""" SELECT MAX(id) FROM "LC_SearchEngine_leetcodedata" """)
                    rows = cursor.fetchall()

                    for row in rows:
                        max_id = int(row[0])

                    cursor.execute(f""" INSERT INTO "LC_SearchEngine_leetcodedata" (id, title, description, 
                    is_premium, difficulty, solution_link, acceptance_rate, frequency, url, discuss_count, accepted, 
                    submissions, companies, related_topics, likes, dislikes, rating, asked_by_faang, similar_questions) 
                    VALUES ({max_id+1}, '{title}', '{description}', {is_premium}, '{difficulty}', '{solution_link}', 
                    {acceptance_rate}, {frequency}, '{url}', {discuss_count}, '{accepted}', '{submissions}', '{companies}',
                    '{related_topics}', {likes}, {dislikes}, {rating}, {asked_by_faang}, '{similar_questions}') """)

                context = {"ps_form": ps_form}
                return render(request, "users/thanks.html", context)

        else:
            messages.warning(request, f"{username} does not have the privileges of a contributor")
            return render(request, "LC_SearchEngine/home.html")

    context = {"ps_form": ps_form}
    return render(request, "users/contributor.html", context)


def thank(request):
    return render(request, "users/thanks.html")
