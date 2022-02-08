from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("editor", views.editor, name='editor'),
    path("give",        views.give, name='give'),
    path("story",        views.story, name='story'),
    path("contact",views.contact, name='contact'),
    path("gallery",   views.gallery, name='gallery'),
    path("timeline",   views.timeline, name='timeline'),
    path("meetings",      views.meetings, name='meetings'),
    path("givingback",  views.givingback, name='givingback'),
    path("registered",   views.registered, name='registered' ),
    path("arrangement",   views.arrangement, name='arrangement'), 
    path("registration",   views.registration, name='registration'), 
    

]