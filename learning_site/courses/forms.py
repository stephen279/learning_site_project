from django import forms

from . import models

#create quiz form


class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',

            'total_answers',



        ]

class FormQuiz(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [

            'answer_1',
            'answer_2',


        ]


class QueryForm(forms.ModelForm):
    class Meta:
        model = models.Query
        fields = [

            'rating',
            'feedback',



        ]

class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [

            'order',
            'prompt',





        ]




class BackTime(forms.ModelForm):
    class Meta:
        model = models.BackTime
        fields = [

            'backtimes',

        ]



class AnswersForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'order',
            'text',
            'correct',


        ]

class SelectedForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'selected',

        ]


