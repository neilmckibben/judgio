from django.db import models
from django.contrib.auth.models import User

# Add organization and job title atributes to users who are Judges
class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    organization = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    sponsor_judge = models.BooleanField(default=False)
    checked_in = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def name(self):
        return self.first_name + ' ' + self.last_name

    def username(self):
        return self.user.username

    def __str__(self):
        return self.name()


#Add teams and team attributes to users who are a teams
class Team(models.Model):
    #idk how long to make the max length
    team_name = models.CharField(max_length=100)
    member_names = models.CharField(max_length=100)
    member_emails = models.EmailField()
    new_hackers = models.CharField(max_length=100)
    project_name = models.CharField(max_length=50)
    project_description = models.TextField(blank=True)

# make migration commands
# python manage.py makemigrations judging
# python manage.py sqlmigrate judging 0001
# python manage.py migrate
