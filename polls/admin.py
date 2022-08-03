from django.contrib import admin
from . models import Question, Choice, Comment

# Register your models here.


@admin.register(Question) 
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'user' , 'created', 'updated', 'updated_by']

    def updated_by(self , obj):
        return obj.updated_by.updated

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['option', 'question', 'vote', 'created', 'updated', 'updated_by']

    def question(self , obj):
        return obj.question.question
    def updated_by(self , obj):
        return obj.updated_by.updated_by


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['commenter', 'body', 'created', 'updated', 'updated_by']

    def updated_by(self , obj):
        return obj.updated_by.updated_by
    

# admin.site.register(Question)
# admin.site.register(Choice)
# admin.site.register(Comment)