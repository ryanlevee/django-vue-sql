import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from common.utils.email import send_email
from django.core.mail import send_mail

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
            subject = 'Play2Learn Application for Game Designer Received'
            # remove f from below (f''') per pylint
            content = 'Hey Play2Learn Admin!\n\'Application\' details below:\n'
            for key, value in data.items():
                label = key.replace('_', ' ').title()
                entry = html.escape(str(value), quote=False)
                if label == 'Available Days':
                    entry = entry.replace('\'','').strip('][').split(', ')
                content += f'{label}: {entry}\n'
            # content += '</ol>'

            # send_email(to, subject, content)
            # print(to, subject, content)
            # return super().form_valid(form)
            send_mail(
                f'{subject}',                   # subject
                f'{content}',       	        # message
                f'{ADMIN_EMAIL}',	    # from
                [f'{ADMIN_EMAIL}'],    # to
                fail_silently=False,
            )
            print(data)
            print(to, subject, content)
            print()
            return super().form_valid(form)


class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'
