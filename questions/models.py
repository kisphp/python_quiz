from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    status = models.PositiveIntegerField(max_length=1, default=2)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'quiz_categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Questions(models.Model):
    status = models.PositiveIntegerField(max_length=1, default=2)
    category = models.ForeignKey(Categories)
    radio_answers = models.BooleanField(default=False)
    question = models.CharField(max_length=255)
    text = models.TextField()

    def active(self):
        return self.status == 2
    active.boolean = True

    def answers(self):
        try:
            ans = Answers.objects.filter(question=self.pk)
        except Answers.DoesNotExist:
            ans = ['aa']
        return ans

    def __unicode__(self):
        return self.question

    class Meta:
        db_table = 'quiz_questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class Answers(models.Model):
    status = models.PositiveIntegerField(max_length=1, default=2)
    question = models.ForeignKey(Questions)
    is_correct = models.BooleanField(default=False)
    response = models.CharField(max_length=255)

    def __unicode__(self):
        return self.response

    class Meta:
        db_table = 'quiz_answers'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


class Tests(models.Model):
    user = models.ForeignKey(User)
    questions = models.CommaSeparatedIntegerField(max_length=64)

    def __unicode__(self):
        return self.questions

    class Meta:
        db_table = 'quiz_tests'
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

class Responses(models.Model):
    test = models.ForeignKey(Tests)
    question = models.ForeignKey(Questions)
    answer = models.ForeignKey(Answers)

    def __unicode__(self):
        return u'%s %s' % (self.question, self.answer)

    class Meta:
        db_table = 'quiz_responses'
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'




















