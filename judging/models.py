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

    #using size constant bc it is the easiest way to enforce min/max values
    #without writing new validators
    TEAM_SIZE = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
        )
    team_name = models.CharField(max_length=100, unique=True)
    project_name = models.CharField(max_length=50, )
    number_of_members = models.CharField(choices=TEAM_SIZE, max_length=1)
    member_one_name = models.CharField(max_length=50, default='invalid')
    member_one_email = models.EmailField(default='invalid')
    member_two_name = models.CharField(max_length=50, default='invalid')
    member_two_email = models.EmailField(default='invalid')
    member_three_name = models.CharField(max_length=50, default='invalid')
    member_three_email = models.EmailField(default='invalid')
    member_four_name = models.CharField(max_length=50, default='invalid')
    member_four_email = models.EmailField(default='invalid')
    new_hackers = models.CharField(choices=TEAM_SIZE, max_length=1)
    project_description = models.TextField(blank=True)

# make migration commands
# python manage.py makemigrations judging
# python manage.py sqlmigrate judging 0001
# python manage.py migrate
