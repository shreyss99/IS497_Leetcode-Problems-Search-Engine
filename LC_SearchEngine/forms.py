from django import forms


class QueryForm(forms.Form):

    DIFFICULTY_OPTIONS = [('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')]
    IS_PREMIUM_OPTIONS = [(True, 'Yes'), (False, 'No')]
    ASKED_BY_FAANG_OPTIONS = [(True, 'Yes'), (False, 'No')]

    title = forms.CharField(label='Title', max_length=100, required=True)
    is_premium = forms.ChoiceField(label='Is Premium Question?', choices=IS_PREMIUM_OPTIONS,
                                   widget=forms.RadioSelect, required=True)
    difficulty = forms.ChoiceField(label='Difficulty Level', choices=DIFFICULTY_OPTIONS,
                                   widget=forms.RadioSelect, required=True)
    companies = forms.CharField(max_length=100, required=True)
    related_topics = forms.CharField(max_length=100, required=True)
    asked_by_faang = forms.ChoiceField(label='Asked By FAANG?', choices=ASKED_BY_FAANG_OPTIONS,
                                       widget=forms.RadioSelect, required=True)
