import html

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView

from django.core.mail import send_mail

from play2learn.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL
from .forms import ReviewForm
from .models import Review

from django.db import IntegrityError
from django.shortcuts import render

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:thanks')


    def form_valid(self, form):
        try: ####################### NOT WORKING ##########################
            data = form.cleaned_data
            to = ADMIN_EMAIL
            subject = 'Play2Learn Game Review Received'
            # remove f from below (f''') per pylint
            content = 'Hey Play2Learn Admin!\n\'Review\' details below:\n'
            for key, value in data.items():
                label = key.replace('_', ' ').title()
                entry = html.escape(str(value), quote=False)
                content += f'{label}: {entry}\n'


            send_mail(
                f'{subject}',           # subject
                f'{content}',       	# message
                f'{ADMIN_EMAIL}',	    # from
                [f'{ADMIN_EMAIL}'],     # to
                fail_silently=False,
            )
            form.instance.user = self.request.user
            return super().form_valid(form)
        except IntegrityError:   ######################## THIS ISN'T WORKING ##
            return render(request=None, template_name="reviews/sorry.html")

class ReviewThanksView(TemplateView):
    template_name = 'reviews/thanks.html'


class ReviewListView(ListView):
    model = Review
    form_class = ListView

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_fields, order_key, direction = self.get_order_settings()

        context['order'] = order_key
        context['direction'] = direction

        context['order_fields'] = list(order_fields.keys())[:-1]

        return context

    def get_ordering(self):
        order_fields, order_key, direction = self.get_order_settings()

        ordering = order_fields[order_key]

        if direction != 'asc':
            ordering = '-' + ordering

        return ordering

    def get_order_settings(self):
        order_fields = self.get_order_fields()
        default_order_key = order_fields['default_key']
        order_key = self.request.GET.get('order', default_order_key)
        direction = self.request.GET.get('direction', 'desc')

        if order_key not in order_fields:
            order_key = default_order_key

        return (order_fields, order_key, direction)

    def get_order_fields(self):
        return {
            'game_title': 'game_title',
            'user': 'user__username',
            'message': 'message',
            'default_key': 'user',
        }

    def get_queryset(self):
        ordering = self.get_ordering()
        qs = Review.objects.all()

        return qs.prefetch_related('user').order_by(ordering)
