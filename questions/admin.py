from django.contrib import admin
from questions.models import *


class AnswersInline(admin.TabularInline):
    model = Answers
    max_num = 5
    extra = 5
    fields = ['response', 'is_correct']


class QuestionsAdmin(admin.ModelAdmin):
    fields = ['category', 'question', 'text', 'radio_answers']
    inlines = [AnswersInline]
    list_display = ['question', 'category', 'active']

admin.site.register(Categories)
admin.site.register(Questions, QuestionsAdmin)