from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from models import Refuge, Dog, Adoption
from forms import RefugeForm, DogForm, AdoptionForm

from dogapp.forms import SignUpForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/dogapp')
    else:
        form = SignUpForm()
    return render(request, 'dogapp/signup.html', {'form': form})


class RefugeDetail(DetailView):
    model = Refuge
    template_name = 'dogapp/refuge_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RefugeDetail, self).get_context_data(**kwargs)
        return context


class RefugeCreate(CreateView):
    model = Refuge
    template_name = 'dogapp/form.html'
    form_class = RefugeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RefugeCreate, self).form_valid(form)


class DogCreate(CreateView):
    model = Dog
    template_name = 'dogapp/form.html'
    form_class = DogForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.refuge = Refuge.objects.get(id=self.kwargs['pk'])
        return super(DogCreate, self).form_valid(form)


class RefugeDelete(DeleteView):
    model = Refuge
    template_name = 'dogapp/refuge_delete.html'
    form_class = RefugeForm
    success_url = '/dogapp/'

    def get_object(self, queryset=None):
        obj = super(RefugeDelete, self).get_object()
        return obj


class DogDelete(DeleteView):
    model = Dog
    template_name = 'dogapp/dog_delete.html'
    form_class = DogForm
    success_url = '/dogapp/'

    def get_object(self, queryset=None):
        obj = super(DogDelete, self).get_object()
        return obj

'''
class AdoptionCreate(CreateView):
    model = Adoption
    template_name = 'dogapp/dog_adopt.html'
    form_class = AdoptionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.refuge = Dog.objects.get(id=self.kwargs['pk'])
        form.instance.dog = Dog.objects.get(id=self.kwargs['pk'])
        return super(AdoptionCreate, self).form_valid(form)
'''
