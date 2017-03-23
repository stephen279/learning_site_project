from django.shortcuts import get_object_or_404, render

from .models import Course, Step, Text, Query, Quiz
from itertools import chain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import logging

from . import forms
from . import models

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .static import fusioncharts





def course_list(request):
    courses = models.Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                   key=lambda step: step.order)
    return render(request, 'courses/course_detail.html', {
            'course': course,
            'steps': steps})


def text_details(request, course_pk, step_pk):

    #steps = models.Step.objects.all()

    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    steps = models.Query.objects.all().filter(step_id=step_pk)

    return render(request, 'courses/text_details.html', {

          'steps':steps,
          'step':step})



def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)

  #  quizzes = sorted(chain(step.quiz_set.all(), step.quiz_set.all()),
  #                 key=lambda step: step.order)

    return render(request, 'courses/quiz_detail.html', {
        'step': step,
        })

def query_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Query, course_id=course_pk, pk=step_pk)



  #  quizzes = sorted(chain(step.quiz_set.all(), step.quiz_set.all()),
  #                 key=lambda step: step.order)

    return render(request, 'courses/query_detail.html', {
        'step': step,

        })


def quiz_create(request, course_pk):   #what course this quiz belongs to
    course = get_object_or_404(models.Course, pk=course_pk)
    form = forms.QuizForm()  #create blank form

    if request.method == 'POST':
         form = forms.QuizForm(request.POST)
         if form.is_valid():
             quiz = form.save(commit=False)  #dont put anything in daabase make model quiz instance
             quiz.course = course
             quiz.save()
             messages.add_message(request, messages.SUCCESS,
                                 "Quiz Added!")
             return HttpResponseRedirect(quiz.get_absolute_url())
    return render (request,'courses/quiz_form.html', {'form':form , 'course': course})


def query_create(request, course_pk,step_pk):   #what course this quiz belongs to
    text = get_object_or_404(models.Text, course_id = course_pk, pk=step_pk)



    form = forms.QueryForm()  #create blank form

    if request.method == 'POST':

         form = forms.QueryForm(request.POST)
         if form.is_valid():
             query = form.save(commit=False)  #dont put anything in daabase make model quiz instance
             #query.course = course



             query.step = text
             query.save()


             messages.add_message(request, messages.SUCCESS,
                                 "Quiz Added!")
          #   return HttpResponseRedirect(query.get_absolute_url())
    return render (request,'courses/query_form.html', {'form':form , 'step':text })


