from django.db import models

# Create your models here.


from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=30)
    zcode = models.CharField(max_length=30)

class Question(models.Model):
    userinfo = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text