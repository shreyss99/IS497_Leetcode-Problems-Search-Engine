from django import forms


class QueryForm(forms.Form):

    DIFFICULTY_OPTIONS = [('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')]
    IS_PREMIUM_OPTIONS = [(True, 'Yes'), (False, 'No')]
    ASKED_BY_FAANG_OPTIONS = [(True, 'Yes'), (False, 'No')]

    is_premium = forms.ChoiceField(label='Is Premium?', choices=IS_PREMIUM_OPTIONS,
                                   widget=forms.RadioSelect, required=True)
    title = forms.CharField(label='Title', max_length=100, required=True)

    difficulty = forms.ChoiceField(label='Difficulty Level', choices=DIFFICULTY_OPTIONS,
                                   widget=forms.RadioSelect, required=True)
    companies = forms.CharField(max_length=100, required=True)
    related_topics = forms.CharField(max_length=100, required=True)
    asked_by_faang = forms.ChoiceField(label='Asked By FAANG?', choices=ASKED_BY_FAANG_OPTIONS,
                                       widget=forms.RadioSelect, required=True)


class ProblemSubmitForm(forms.Form):

    DIFFICULTY_OPTIONS = [('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')]
    IS_PREMIUM_OPTIONS = [(True, 'Yes'), (False, 'No')]
    ASKED_BY_FAANG_OPTIONS = [(True, 'Yes'), (False, 'No')]

    title = forms.CharField(label='Title', max_length=100, required=True)
    description = forms.CharField(widget=forms.TextInput, required=True)
    is_premium = forms.ChoiceField(label='Is Premium?', choices=IS_PREMIUM_OPTIONS,
                                   widget=forms.RadioSelect, required=True)
    difficulty = forms.ChoiceField(label='Difficulty Level', choices=DIFFICULTY_OPTIONS,
                                   widget=forms.RadioSelect, required=True)
    solution_link = forms.CharField(label='Solution Link', max_length=200, required=False)
    acceptance_rate = forms.FloatField(label='Acceptance Rate', required=True)
    frequency = forms.FloatField(label='Frequency', required=True)
    url = forms.CharField(label='Solution URL', max_length=200, required=True)
    discuss_count = forms.IntegerField(label='Discuss Count', required=True)
    accepted = forms.CharField(label='Accepted', max_length=10, required=True)
    submissions = forms.CharField(label='Submissions', max_length=10, required=True)
    companies = forms.CharField(label='Companies', max_length=100, required=True)
    related_topics = forms.CharField(label='Related Topics', max_length=300, required=False)
    likes = forms.IntegerField(label='Likes', required=True)
    dislikes = forms.IntegerField(label='Dislikes', required=True)
    asked_by_faang = forms.ChoiceField(label='Asked By FAANG?', choices=ASKED_BY_FAANG_OPTIONS,
                                       widget=forms.RadioSelect, required=True)
    similar_questions = forms.CharField(label='Similar Questions', widget=forms.TextInput, required=False)
