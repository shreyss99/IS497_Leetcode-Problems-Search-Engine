from django import forms
from .models import LeetcodeData


class QueryForm(forms.Form):

    DIFFICULTY_OPTIONS = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')]
    IS_PREMIUM_OPTIONS = [(1, 'Yes'), (0, 'No')]
    ASKED_BY_FAANG_OPTIONS = [(1, 'Yes'), (0, 'No')]

    title = forms.CharField(label='Title', max_length=100, required=False)
    is_premium = forms.ChoiceField(label='Is Premium Question?', choices=IS_PREMIUM_OPTIONS,
                                   widget=forms.RadioSelect, required=False)
    difficulty = forms.ChoiceField(label='Difficulty Level', choices=DIFFICULTY_OPTIONS,
                                   widget=forms.CheckboxSelectMultiple, required=False)
    companies = forms.CharField(max_length=100, required=False)
    related_topics = forms.CharField(max_length=100, required=False)
    asked_by_faang = forms.ChoiceField(label='Asked By FAANG?', choices=ASKED_BY_FAANG_OPTIONS,
                                       widget=forms.RadioSelect, required=False)
