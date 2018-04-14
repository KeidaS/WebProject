from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Dog, Vaccine, Refuge
from forms import RefugeForm, DogForm
from views import RefugeCreate, DogCreate, RefugeDetail
from dogapp import views as core_views


urlpatterns = [
    # List latest 10 restaurants: /myrestaurants/
    url(r'^$',
        ListView.as_view(
            queryset=Refuge.objects.filter(),
            context_object_name='latest_refuge_list',
            template_name='dogapp/refuge_list.html'),
        name='restaurant_list'),
    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^refuges/(?P<pk>\d+)/$',
        RefugeDetail.as_view(),
        name='refuge_detail'),
    # Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^refuges/(?P<pkr>\d+)/dogs/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dog),
        name='dog_detail'),
    # Create a restaurant, /myrestaurants/restaurants/create/
    url(r'^refuges/create/$',
        RefugeCreate.as_view(),
        name='refuge_create'),
    # Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^refuges/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Refuge,
            template_name='dogapp/form.html',
            form_class=RefugeForm),
        name='refuge_edit'),
    # Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'^refuges/(?P<pk>\d+)/dogs/create/$',
        DogCreate.as_view(),
        name='dog_create'),
    # Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'^refuges/(?P<pkr>\\d+)/dogs/(?P<pk>\\d+)/edit/$',
        UpdateView.as_view(
            model=Dog,
            template_name='dogapp/form.html',
            form_class=DogForm),
        name='dog_edit'),
    url(r'^signup/$', core_views.signup, name='signup'),
# Restaurant details, from: /myrestaurants/1/
    url(r'^refuges/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Refuge,
            template_name='dogapp/refuge_detail.html'),
        name='refuge_detail'),


]
