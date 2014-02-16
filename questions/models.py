from django.db import models

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
            ans = []
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

