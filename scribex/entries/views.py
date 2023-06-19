from entries.models import Entry

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class EntryListView(LockedView, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-data_created')


class EntryDetailView(LockedView, DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
    success_url = reverse_lazy('entry-list')
    success_message = "Your new entry was created!"


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']
    success_message = "Your entry was updated!"


    def get_success_url(self) -> str:

        return reverse_lazy(
            'entry-detail',
            kwargs={'pk': self.object.pk}
        )


class EntryDeleteView(SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('entry-list')
    success_message = "Your entry was deleted!"


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
