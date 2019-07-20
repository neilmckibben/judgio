<<<<<<< HEAD
from django.views.generic import CreateView
from .models import Team
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import TeamForm

def register(request):


    #really basic, will add more later
    form = TeamForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'form.html', {'form' : form})
=======
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context, loader
import json

from .forms import JudgeForm
from .models import Judge

def home(request):
    # check if user is checked in judge
    if request.user.is_authenticated:
        judge = Judge.objects.filter(user_id = request.user.id)
        if len(judge) and judge[0].checked_in:
                return render(request, 'home.html', {'name': judge[0].name(), 'checked_in': True})
    return render(request, 'home.html', {'checked_in': False})

# admin view for judge csv-upload
def judge_upload_view(request):
    if request.method == 'POST':
        judge_info = request.POST.get('judge_info')
        judges = json.loads(judge_info)
        for judge in judges:
            # firstname, lastname, email, org, jobtitle, spons
            judge_data = {'first_name'      :judge[0],
                          'last_name'       :judge[1],
                          'email'           :judge[2],
                          'organization'    :judge[3],
                          'job_title'       :judge[4],
                          'sponsor_judge'   :True if judge[5]=='TRUE' else False,
                          'checked_in'      :False,
                          'active'          :False if judge[6]=='FALSE' else True,
                          }
            judge_form = JudgeForm(judge_data)
            if judge_form.is_valid():
                judge_form.save()

        return JsonResponse({'judge_info':judge_info})
    else:
        template = loader.get_template("admin/judge_upload.html")
        return HttpResponse(template.render())
>>>>>>> 4931462f491fcff27b00099c66413d2154266d25
