import html

# from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DetailView, ListView, TemplateView
)

# from common.utils.email import send_email
from django.core.mail import send_mail

from play2learn.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL
from .forms import ContactForm
from .models import Game, ContactUs


class ContactUsView(SuccessMessageMixin, CreateView):
    model = ContactUs
    form_class = ContactForm
    success_url = reverse_lazy('games:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = ADMIN_EMAIL
        subject = "Play2Learn 'Contact Us' Message Received"
        content = 'Hey Play2Learn Admin!\n\'Contact Us\' details below:\n'
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            if self.request.user.is_authenticated:
                if key == "email":
                    label = 'From'
                    entry = f'{self.request.user} ({self.request.user.email})'
            content += f'{label}: {entry}\n'

        send_mail(
            f'{subject}',           # subject
            f'{content}',       	# message
            f'{ADMIN_EMAIL}',	    # from
            f'{ADMIN_EMAIL}',       # to
            fail_silently=False,
        )
        print(data)
        print(to, subject, content)
        print()
        return super().form_valid(form)


class GameThanksView(TemplateView):
    template_name = 'games/thanks.html'


class AboutView(TemplateView):
    template_name = 'games/about.html'


class GameDetailView(DetailView):
    model = Game


class GamePlayView(TemplateView):
    template_name = 'games/play.html'


class GameListView(ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'

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
            # 'game': 'title',
            # 'game_title': 'game_title',
            # 'user': 'user__username',
            'score': 'score',
            # 'operation': 'operation',
            # 'max_number': 'max_number',
            'default_key': 'score',
        }

    def get_queryset(self):
        ordering = self.get_ordering()
        qs = Game.objects.all()

        if 'username' in self.kwargs:
            username = self.kwargs['username']
            qs = qs.filter(user__username=username)

        queryset = {
            'user': qs.prefetch_related('user').order_by(ordering),
            'angr_list': qs.filter(game_title_id=2).order_by(ordering)[:16],
            'math_list': qs.filter(game_title_id=1).order_by(ordering)[:16]
            }

        return queryset
