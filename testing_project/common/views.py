from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from testing_project.common.models import Profile


class ProfileCreateView(views.CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profiles/create.html'
    # success_url = reverse_lazy('profile lists')

    # another option for success url when we want to pass the pk (dinamicaly),
    # we need def get_success_url, success_url cannot work
    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class ProfilesListView(views.ListView):
    model = Profile
    template_name = 'profiles/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user.username
        else:
            context['user'] = 'No user'

        return context

    # another method to be tested
    # def get_queryset(self):
    #     pass
    #     # return super().get_queryset().prefetch_related().filter()


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profiles/details.html'
