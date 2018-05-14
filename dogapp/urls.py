from django.conf.urls import url
from django.views.generic import DetailView, ListView, UpdateView
from models import Dog, Refuge
from forms import RefugeForm, DogForm
from views import RefugeCreate, DogCreate, RefugeDetail, RefugeDelete
from dogapp import views as core_views

urlpatterns = [
    # List all refuges: /dogapp/
    url(r'^$',
        ListView.as_view(
            queryset=Refuge.objects.filter(),
            context_object_name='latest_refuge_list',
            template_name='dogapp/refuge_list.html'),
        name='refuge_list'),
    # Refuge details, ex.: /dogapp/refuge/1/
    url(r'^refuges/(?P<pk>\d+)/$',
        RefugeDetail.as_view(),
        name='refuge_detail'),
    # Refuge dog details, ex: /dogapp/refuge/1/dishes/1/
    url(r'^refuges/(?P<pkr>\d+)/dogs/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dog),
        name='dog_detail'),
    # Create a restaurant, /dogapp/refuge/create/
    url(r'^refuges/create/$',
        RefugeCreate.as_view(),
        name='refuge_create'),
    # Edit restaurant details, ex.: /dogapp/refuge/1/edit/
    url(r'^refuges/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Refuge,
            template_name='dogapp/form.html',
            form_class=RefugeForm),
        name='refuge_edit'),
    # Delete refuge: ex.: /dogapp/refuge/1/delete

    url(r'^refuges/(?P<pk>\d+)/delete/$',
        RefugeDelete.as_view(
            model=Refuge,
            template_name='dogapp/refuge_delete.html',
            form_class=Refuge),
        name='refuge_delete'),

    # Create a restaurant dish, ex.: /dogapp/refuge/1/dog/create/
    url(r'^refuges/(?P<pk>\d+)/dogs/create/$',
        DogCreate.as_view(),
        name='dog_create'),
    # Edit restaurant dish details, ex.: /dogapp/refuge/1/dog/1/edit/
    url(r'^refuges/(?P<pkr>\d+)/dogs/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Dog,
            template_name='dogapp/form.html',
            form_class=DogForm),
        name='dog_edit'),
    url(r'^signup/$', core_views.signup, name='signup'),
    # Restaurant details, from: /dogapp/1/
    url(r'^refuges/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Refuge,
            template_name='dogapp/refuge_detail.html'),
        name='refuge_detail'),
    url(r'^accounts/login/$', core_views.login, name='login'),

    url(r'^dogs/(?P<pk>\d+)/adopt$',
        DetailView.as_view(
            model=Dog,
            template_name='dogapp/dog_adopt.html'),
        name='dog_adopt'),
]
