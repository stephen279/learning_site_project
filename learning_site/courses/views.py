from django.shortcuts import get_object_or_404, render

from .models import Course, Step, Text, Query, Quiz
from itertools import chain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import logging
from django.http import HttpResponse

from . import forms
from . import models

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .static import fusioncharts





def course_list(request):
    courses = models.Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def test(request):
    return HttpResponse("You're looking at question %s.")



def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                   key=lambda step: step.order)
    return render(request, 'courses/course_detail.html', {
            'course': course,
            'steps': steps})



def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)

    print(step.id)   #Quiz id

    #now get the question id

    question_id = models.Question.objects.filter(quiz_id=step.id).values("id")
    print(question_id) # question_id

    steps = models.Answer.objects.filter(question_id=question_id, text_version='1')
    steps_version2 = models.Answer.objects.filter(question_id=question_id, text_version='2')
    steps_wrong = models.Answer.objects.filter(question_id=question_id,correct='0')



    order = models.Answer.objects.filter(question_id=question_id).values("order")
    print(order)  # orders

    correct = models.Answer.objects.filter(question_id=question_id).values("correct")
    print(correct)  # orders

    #    step_order = get_object_or_404(models.Answer, question_id = question_id)


    #now get the question id
    form = forms.SelectedForm()  #create blank form

    steps_version2 = models.Answer.objects.filter(question_id=question_id).values("text_version")
    steps_versions = list(steps_version2)[0]['text_version']

    print("steps_version2",steps_versions)
    answer_correct_order = models.Answer.objects.filter(correct="1", question_id=question_id)




    if request.method == 'POST':
         form = forms.SelectedForm(request.POST)
         if form.is_valid():

             percentage_count = models.Answer.objects.filter(question_id=question_id, order='0').values("count")

             check_count = list(percentage_count)[0]['count']
             print("order",check_count)

             percentage_count1 = models.Answer.objects.filter(question_id=question_id, order='1').values("count")
             check_count1 = list(percentage_count1)[0]['count']
             print("order1",check_count1)

             percentage_count2 = models.Answer.objects.filter(question_id=question_id, order='2').values("count")
             check_count2 = list(percentage_count2)[0]['count']
             print("order2",check_count2)

             percentage_count3 = models.Answer.objects.filter(question_id=question_id, order='3').values("count")
             check_count3 = list(percentage_count3)[0]['count']
             print("order3", check_count3)

             add_counts = check_count + check_count1 + check_count2 + check_count3
             print("add count", add_counts)







             select = form.save(commit=False)  # dont put anything in daabase make model quiz instance

             question_idn = models.Question.objects.filter(quiz_id=step.id).values("id")



             print(question_idn.values())
             #the following is uded to extract the id pair value
             ids = list(question_idn)[0]['id']



             #update = models.Answer.objects.get(id=step_pk)  # get correct column from dtabase
             select.question_id = ids

             #get form selected field that you write in

             form_value = select.selected

             select = models.Answer()  # instance of Bactime model
             select.question_id = ids
             models.Answer.objects.filter(question_id=question_id,order=form_value).update(selected="1")

             check = models.Answer.objects.filter(question_id=question_id,order=form_value).values("id")




             check_selected = list(check)[0]['id']
             print(check_selected)

             check1 = models.Answer.objects.filter(question_id=question_id,id=check).values("correct")
             count1 = models.Answer.objects.filter(question_id=question_id, id=check).values("count")
             check_correct = list(check1)[0]['correct']
             print(check_correct)

            # compare = check_selected == check_correct
             #print(compare)
             check1_count = list(count1)[0]['count']

             print(check1_count)

             print("Max count", add_counts)

             def percentage(part, whole):
                 return 100 * float(part) / float(whole)

             # percentage(check1_count, add_counts)
             percentage_send = percentage(check1_count, add_counts)
             print ("percentage ", percentage(check1_count, add_counts))
             previous_version_percentage = models.Answer.objects.filter(question_id=question_id, correct='1').values("previous_version_percentage")
             check_previous_version = list(previous_version_percentage)[0]['previous_version_percentage']
             print ("check_previous_version",check_previous_version)



             if (steps_versions == 2) & (check_previous_version == 0):
                 print("steps_version is 2")
                 models.Answer.objects.filter(question_id=question_id, correct='1').update(
                 previous_version_percentage=percentage_send)
                 print("changed previous version percentage to ",percentage_send)

             pass

             if  check_correct == 1:
                 print("the answer count number is",count1)
                 check1_count = list(count1)[0]['count']

                 print(check1_count)

                 print("Max count", add_counts)



                 def percentage(part, whole):
                     return 100 * float(part) / float(whole)

                 #percentage(check1_count, add_counts)
                 percentage_send = percentage(check1_count, add_counts)
                 print ("percentage " ,percentage(check1_count, add_counts))



                 messages.add_message(request, messages.SUCCESS,
                                      "CORRECT! WELL DONE")
                 # get count value the add 1
                 count = models.Answer.objects.filter(question_id=question_id, order=form_value).values("count")



                 check_count = list(count)[0]['count']
                 print(check_count)

                 count = check_count + 1
                 print(count)

                 models.Answer.objects.filter(question_id=question_id, order=form_value).update(count=count)

                 answer_correct_order = models.Answer.objects.filter(correct="1", question_id=question_id)
                 percentage_save = models.Answer.objects.filter(correct="1", question_id=question_id).update(percentage_correct=percentage_send)  # instance of Answers model
                # select.percentage_correct = "2"
                # print("select.percentage_correct",select.percentage_correct)


             else:

                 messages.add_message(request, messages.SUCCESS,
                                      "WRONG! SORRY")



                 #get count value the add 1
                 count = models.Answer.objects.filter(question_id=question_id, order=form_value).values("count")

                 check_count = list(count)[0]['count']
                 print(check_count)

                 count = check_count + 1
                 print(count)

                 models.Answer.objects.filter(question_id=question_id, order=form_value).update(count=count)

                 answer_correct_order = models.Answer.objects.filter(correct="1",question_id=question_id)



                 print(answer_correct_order)
                 form = forms.SelectedForm()

            #now compare order value sent from form vs anwser_correct_order


             form = forms.SelectedForm()

            # return HttpResponseRedirect(quiz.get_absolute_url())





    return render(request, 'courses/quiz_detail.html', {
        'step': step,
        'form':form,
        'question_id':question_id,
        'steps':steps,
        'steps_version2':steps_version2,
        'steps_wrong':steps_wrong,

        'answer_correct_order':answer_correct_order,






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


def text_details(request, course_pk, step_pk, ):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    steps = models.Query.objects.filter(step_id=step_pk )

    times = models.BackTime.objects.filter(step_id=step_pk, textversion='1')
    timesvers = models.BackTime.objects.filter(step_id=step_pk, textversion='2')

    stepsvers = models.Query.objects.filter(step_id=step_pk, textversion='1')
    stepsversion = models.Query.objects.filter(step_id=step_pk, textversion ='2' )



    form = forms.BackTime()  # create blank form
    print("form create")


    if request.method == 'POST':
         form = forms.BackTime(request.POST)
         if form.is_valid():

             stepv = Text.objects.get(id=step_pk) #get correct column from dtabase
             stepv = stepv.version    # choose the version field
             print stepv


             timeForm = form.save(commit=False)  #dont put anything in daabase make model quiz instance
             timeForm.step = step
             timeForm.textversion = stepv


             timeForm.save()

             #back = models.BackTime()  # instance of Bactime model
             #back.backtimes = "3"

             #back.textversion = stepv  # change textversion field(BackTime model) to the textversion value in Text model
             #back.save()



             # messages.success(request, 'Your password was updated successfully!')
             print("Success")
             messages.add_message(request, messages.SUCCESS,
                               "time Added!")
           #  return HttpResponseRedirect(timeForm.get_absolute_url())




    return render(request, 'courses/text_details.html', {
        'form':form,
        'steps':steps,
        'times':times,
         'step':step,
        'stepsversion':stepsversion,
        'stepsvers': stepsvers,
        'timesvers': timesvers,

          })



def query_create(request, course_pk,step_pk):   #what course this quiz belongs to
    step = get_object_or_404(models.Text, course_id = course_pk, pk=step_pk)
    form = forms.QueryForm()  #create blank form

    if request.method == 'POST':


         form = forms.QueryForm(request.POST)
         if form.is_valid():
             query = form.save(commit=False)  #dont put anything in daabase make model quiz instance
             #query.course = course
             stepv = Text.objects.get(id=step_pk)  # get correct column from dtabase
             stepv = stepv.version  # choose the version field
             print stepv

             query.step = step
             query.textversion = stepv
             query.save()
             print("Query Success save")


             messages.add_message(request, messages.SUCCESS,
                                 "Feedback Sent! Thank You for your input!!!!!!")
       #      return HttpResponseRedirect(query.get_absolute_url())
    return render (request,'courses/query_form.html', {'form':form , 'step':step })

def create_question(request, quiz_pk, question_type):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk)

    if question_type == 'mc':
        form_class = forms.MultipleChoiceQuestionForm

    else:

         form_class = forms.MultipleChoiceQuestionForm

    form = form_class()
    if request.method == 'POST':

        form = form_class(request.POST)
        if form.is_valid():
             question = form.save(commit=False)
             question.quiz = quiz
             question.save()
           #  messages.success(request, "Added_question")
    #return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/question_form.html', {'quiz': quiz, 'form': form})


def answer_form(request, question_pk):

   question = get_object_or_404(models.Question, pk=question_pk)


   form = forms.AnswersForm()

   if request.method == "POST":
        form = forms.AnswersForm(request.POST)
        if form.is_valid():
           answer = form.save(commit=False)
           answer.question = question
           answer.save()
        #   messages.success(request,"Answer Added")
        #   return HttpResponseRedirect(question.get_absolute_url())
   return render(request, "courses/answer_form.html",{
        'question':question,
        'form':form,
       })


def select_form(request, question_pk):

   question = get_object_or_404(models.Question, pk=question_pk)

   form = forms.SelectedForm()

   if request.method == "POST":

        form = forms.SelectedForm(request.POST)
        messages.success(request, "Selection choiced")
        if form.is_valid():
           answer = form.save(commit=False)
           answer.question = question
           answer.save()
           messages.success(request,"Selection Added")
        #   return HttpResponseRedirect(question.get_absolute_url())
   return render(request, "courses/slect_form.html",{
        'question':question,
        'form':form,
       })