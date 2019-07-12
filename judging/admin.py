from django.contrib import admin, messages
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.template import Context, loader
import json


from .models import Judge
from .forms import JudgeForm
from .models import Team
from .forms import TeamForm

# Filter for active status
class ActiveFilter(admin.SimpleListFilter):
    title = 'Active'
    parameter_name = 'active'

    def lookups(self, request, model_admin):
        return [
            ('active', 'Active'),
            ('not_active', 'Not Active'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'active':
            return queryset.distinct().filter(active=True)
        if self.value():
            return queryset.distinct().filter(active=False)


# controls /admin/judging/judge
class JudgeAdmin(admin.ModelAdmin):
    # override default form
    form = JudgeForm

    # Table columns on form
    list_display = ('name', 'organization', 'job_title', 'email', 'username', 'sponsor_judge', 'checked_in', 'active')
    search_fields = ['user__first_name', 'user__last_name', 'organization', 'user__email']
    list_filter = (ActiveFilter, )


# new admin view for judge csv-upload
def judge_upload_view(request):
    if request.method == 'GET':
        template = loader.get_template("admin/judge_upload.html")
        return HttpResponse(template.render())

    elif request.method == 'POST':
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

# register new view on admin site
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Judge, JudgeAdmin)
admin.site.register_view('judges/judge-upload/', view=judge_upload_view)
