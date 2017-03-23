from django.db import models
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse



class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    


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



    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id
        })

    def __unicode__(self):
        return unicode(self.content) or u''




class Quiz(Step):
    total_questions = models.IntegerField(default=3)



    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id
        })



        def __unicode__(self):
            return unicode(self.total_questions) or u''

class Query(models.Model):
    times = models.IntegerField(default = 0, null=True)
    feedback = models.CharField(max_length=255, null=True)
    course = models.ForeignKey(Course)
    step = models.ForeignKey(Text)

    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.step.id
        })


    def __unicode__(self):
        return unicode(self.times) or u''













