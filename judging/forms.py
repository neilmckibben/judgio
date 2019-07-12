from django import forms
from django.contrib.auth.models import User

from .models import Judge
from .models import Team

# new form for judges so we can auto-generate users on save
class JudgeForm(forms.ModelForm):

    class Meta:
        model = Judge
        # form fill-in fields
        fields = ('first_name',
                  'last_name',
                  'email',
                  'organization',
                  'job_title',
                  'sponsor_judge',
                  'checked_in',
                  'active')

    # creates username for judges
    # username for judges is firstnamelastname all lowercase
    def generate_username(self, judge):
        return (judge.first_name + judge.last_name).lower()

    # create users concurrently to adding judges
    def save(self, commit=True):
        # get all the input judge information
        judge = super(JudgeForm, self).save(commit=False)

        username = self.generate_username(judge)

        # check is there is a user; if noen create, else update username
        if judge.user_id is None:
            # TODO: handle username is not unique
            # TODO: password
            new_user = User.objects.create_user(username, judge.email, 'password')
            judge.user_id = new_user.id
        else:
            user = User.objects.get(id=judge.user_id)
            user.username = username
            user.save()

        # save and commit judge info
        if commit:
            judge.save()

        return judge

# new form for teams so we can auto-generate users on save
class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('team_name', 'member_one_name', 'member_one_email',
                'member_two_name','member_two_email', 'member_three_name',
                'member_three_email', 'member_four_name', 'member_four_email',
                'new_hackers', 'project_description')
