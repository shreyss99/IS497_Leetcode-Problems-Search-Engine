from django import forms
from .models import LeetcodeData


class QueryForm(forms.Form):

    DIFFICULTY_OPTIONS = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')]
    IS_PREMIUM_OPTIONS = [(1, 'Yes'), (0, 'No')]
    ASKED_BY_FAANG_OPTIONS = [(1, 'Yes'), (0, 'No')]

    title = forms.CharField(label='Title', max_length=100, required=False)
    is_premium = forms.ChoiceField(label='Is Premium Question?', choices=IS_PREMIUM_OPTIONS, widget=forms.RadioSelect,
                                   required=False)
    difficulty = forms.ChoiceField(label='Difficulty Level', choices=DIFFICULTY_OPTIONS,
                                   widget=forms.CheckboxSelectMultiple, required=False)
    acceptance_rate = forms.FloatField(required=False)
    frequency = forms.FloatField(required=False)
    discuss_count = forms.IntegerField(required=False)
    companies = forms.CharField(max_length=100, required=False)
    related_topics = forms.CharField(max_length=100, required=False)
    likes = forms.IntegerField(required=False)
    dislikes = forms.IntegerField(required=False)
    rating = forms.IntegerField(required=False)
    asked_by_faang = forms.ChoiceField(label='Asked By FAANG?', choices=ASKED_BY_FAANG_OPTIONS,
                                       widget=forms.RadioSelect, required=False)

    def search(self):
        # Get the cleaned data from the form
        title = self.cleaned_data.get('title')
        is_premium = self.cleaned_data.get('is_premium')
        difficulty = self.cleaned_data.get('difficulty')
        acceptance_rate = self.cleaned_data.get('acceptance_rate')
        frequency = self.cleaned_data.get('frequency')
        discuss_count = self.cleaned_data.get('discuss_count')
        companies = self.cleaned_data.get('companies')
        related_topics = self.cleaned_data.get('related_topics')
        likes = self.cleaned_data.get('likes')
        dislikes = self.cleaned_data.get('dislikes')
        rating = self.cleaned_data.get('rating')
        asked_by_faang = self.cleaned_data.get('asked_by_faang')


        # Query the database using the form data
        result = LeetcodeData.objects.all()

        if title:
            result = result.filter(title__icontains=title)
        if is_premium:
            result = result.filter(is_premium=is_premium)
        if difficulty:
            result = result.filter(difficulty__icontains=difficulty)
        if acceptance_rate:
            result = result.filter(acceptance_rate=acceptance_rate)
        if frequency:
            result = result.filter(frequency=frequency)
        if discuss_count:
            result = result.filter(discuss_count=discuss_count)
        if companies:
            result = result.filter(companies__icontains=companies)
        if related_topics:
            result = result.filter(related_topics__contains=related_topics)
        if likes:
            result = result.filter(likes=likes)
        if dislikes:
            result = result.filter(dislikes=dislikes)
        if rating:
            result = result.filter(rating=rating)
        if asked_by_faang:
            result = result.filter(asked_by_faang=asked_by_faang)

        return result
