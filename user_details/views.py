from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import UserProfile, Measurement




DB_CONFIG = {
    
    'eu' : 'eu',
    'default': 'default'
}


class UserProfileView(ListView):
  
    # specify the model for list view
    model = UserProfile
    templats = 'user_details/userprofile_list.html'
    context_object_name = 'object_list'
  
    def get_queryset(self, *args, **kwargs):
        db_name = self.kwargs.get('region', 'default')
        qs = self.model.objects.all().using(db_name)
        qs = qs.order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        db_name = self.kwargs.get('region', 'default')
        ctx['db_name'] = db_name
        return ctx


class UserProfileCreate(CreateView):
  
    model = UserProfile
    fields = ['email', 'street', 'stree2', 'name', 'city', 'country']

    def form_valid(self, form):
        db_name = self.kwargs.get('region', 'default')
        object = form.save(commit=False)
        object.save(using=db_name)
        return redirect('/eu' if db_name=='eu' else '/')


class MeasurementView(ListView):
  
    # specify the model for list view
    model = Measurement
    context_object_name = 'object_list'
  
    def get_queryset(self, *args, **kwargs):
        db_name = self.kwargs.get('region', 'default')
        qs = self.model.objects.all().using(db_name)
        qs = qs.order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        db_name = self.kwargs.get('region', 'default')
        ctx['db_name'] = db_name
        return ctx


class MeasurementCreate(CreateView):
  
    model = Measurement
    templats = 'user_details/m_create_form.html'
    fields = ['user', 'weight', 'height', 'width', 'dateTime']

    def form_valid(self, form):
        db_name = self.kwargs.get('region', 'default')
        object = form.save(commit=False)
        object.save(using=db_name)
        return redirect('/eu/messurment' if db_name=='eu' else '/messurment')


