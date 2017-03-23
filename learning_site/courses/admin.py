from django.contrib import admin

from .models import Course, Text, Quiz, Query


class TextInline(admin.StackedInline):
    model = Text

    
class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline,]



admin.site.register(Course, CourseAdmin)
admin.site.register(Text)
admin.site.register(Quiz)
admin.site.register(Query)