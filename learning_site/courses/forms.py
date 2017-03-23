from django import forms

from . import models

#create quiz form


class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',



        ]


class QueryForm(forms.ModelForm):
    class Meta:
        model = models.Query
        fields = [

            'times',
            'feedback',

        ]


