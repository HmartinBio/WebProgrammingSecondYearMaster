from django.db import models

# Create your models here.

''' Class: User
This class allows to initialise user table in the database'''

class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    mailAddress = models.EmailField()
    password = models.CharField(max_length=50)
    score = models.IntegerField(null=True)
    gameActive = models.IntegerField(null=True)


''' Class: Images
This class allows to initialise images table in the database'''



class Images(models.Model):
    image_id = models.IntegerField()
    image_name = models.IntegerField()
    description = models.TextField()
    microscopy = models.CharField(max_length=60)
    cell_type = models.CharField(max_length=60)
    component = models.CharField(max_length=60)
    doi = models.CharField(max_length=60)
    organism = models.CharField(max_length=60)
    url = models.CharField(max_length=60)


''' Class: Question
This class allows to initialise question table in the database'''



class Question(models.Model):
    question_id = models.IntegerField()
    question = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    imageField = models.CharField(max_length=60)
    points = models.IntegerField()
    n_answer = models.IntegerField()
    n_image = models.IntegerField()


''' Class: Answers
This class allows to initialise answers table in the database'''

class Answers(models.Model):
    answerId = models.IntegerField()
    questionId = models.IntegerField()
    answer = models.CharField(max_length=60)
    definition = models.TextField()


''' Class: AnswersToTheQuizz
This class allows to initialise answerstothequizz 
table in the database'''


class AnswerToTheQuizz(models.Model):
    usernamePlusQuestion = models.CharField(max_length=120)
    goodAnswerId = models.IntegerField()
