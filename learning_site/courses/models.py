from django.core.urlresolvers import reverse
from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



FEEDBACK_OPTIONS = (
    ('BADLY EXPLAINED', 'Badly Explained'),
    ('TO COMPLICATED', 'To Complicated'),
    ('NOT INTERESTED', 'Not interesting'),
    ('LOVED IT', 'Loved It!!!'),
    ('WELL TAUGHT', 'Well Taught'),
    ('GOOD MATERIAL', 'Good Material'),

)

class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    feeder = models.IntegerField(default=0);
    


    def __unicode__(self):
        return unicode(self.title) or u''


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField( null=True)
   # content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0, null=True)

    course = models.ForeignKey(Course)







    #clickTime = models.IntegerField()
    
    class Meta:
        abstract = [True]
        ordering = ['order',]

    def __unicode__(self):
        return unicode(self.title) or u''

class Text(Step):
    content = models.TextField(blank=True, default='', null=True)
    video = models.FileField( null=True)
    #video = EmbedVideoField()

    time = models.IntegerField(default = 10, null=True)
    version = models.IntegerField(default=1, null=True)
    new = models.TextField(default="Noting new", null=True)
    textversion = models.TextField(default=1, null=True)




    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id,

        })


def __unicode__(self):
    return unicode(self.content) or u''



class Quiz(Step):
    total_questions = models.IntegerField(default=3)
    total_answers = models.IntegerField(default=4)
    correct = models.BooleanField(default=False)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)



    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id
        })



        def __unicode__(self):
            return unicode(self.total_questions) or u''

class Query(models.Model):
    rating = models.IntegerField(default = 0, null=True)
    feedback = models.CharField(max_length=15, choices=FEEDBACK_OPTIONS)
    course = models.ForeignKey(Course)
    step = models.ForeignKey(Text)
    textversion = models.IntegerField(default=0, null=True)


    def get_absolute_url(self):
        return reverse('courses:query', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.step.id
        })


    def __unicode__(self):
        return unicode(self.rating) or u''





class BackTime(models.Model):
    backtimes = models.IntegerField(default = 0, null=True)
    topic = models.CharField(max_length=255, null=True)
    course = models.ForeignKey(Course)
    step = models.ForeignKey(Text)
    textversion = models.IntegerField(default=0,null=True)


    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.step.id,


        })

    def __unicode__(self):
        return unicode(self.backtimes) or u''

class Question(models.Model):
     quiz = models.ForeignKey(Quiz)
     order = models.IntegerField(default=0)
     prompt = models.TextField()

     class Meta:
         ordering = ['order']



     def get_absolute_url(self):
         return self.quiz.get_absolute_url()

     def __str__(self):
         return self.prompt


class MultipleChoiceQuestion(Question):
    shuffle_answers = models.BooleanField(default=False)


class TrueFalseQuestion(Question):
    pass


class Answer(models.Model):
    question = models.ForeignKey(Question)
    order = models.IntegerField(default=0 )
    text = models.CharField(max_length=255)
    correct = models.IntegerField(default=0)
    selected = models.IntegerField(default=0,validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ])
    count = models.IntegerField(default=0)
    text_version= models.IntegerField(default=1)
    percentage_correct = models.IntegerField(default=0)
    previous_version_percentage =  models.IntegerField(default=0)


    class Meta:
        ordering = ['order']

    def _str__(self):
        return self.text

























