from django.db import models

class Quiz(models.Model):
    text = models.CharField(max_length=40)

    def __str__(self):
        return self.text

class Question(models.Model):
    question = models.ForeignKey(Quiz,related_name='questions',on_delete=models.CASCADE)
    text = models.CharField(max_length=120)

    def __str__(self):
        return self.text

class Answer(models.Model):
    answer = models.ForeignKey(Question,related_name='answers',on_delete=models.CASCADE)
    text = models.CharField(max_length=120)

    def __str__(self):
        return self.text

