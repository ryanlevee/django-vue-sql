import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from common.utils.email import send_email

from play2learn.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL
from .models import Applicant
from .forms import JobApplicationForm

####### ALSO ADD EMAIL FOR WHEN GAME SCORE IS LOGGED

class JobAppView(CreateView):
    model = Applicant
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')


    def form_valid(self, form):
            data = form.cleaned_data
            to = ADMIN_EMAIL
            subject = 'Application for Game Designer'
            # remove f from below (f''') per pylint
            content = '''<p>Hey HR Manager!</p>
                <p>Job application received:</p>
                <ol>'''
            for key, value in data.items():
                label = key.replace('_', ' ').title()
                entry = html.escape(str(value), quote=False)
                if label == 'Available Days':
                    entry = entry.replace('\'','').strip('][').split(', ')
                content += f'<li>{label}: {entry}</li>'
            content += '</ol>'

            send_email(to, subject, content)
            print(to, subject, content)
            return super().form_valid(form)


class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'
