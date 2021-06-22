from django.urls import path		 
from . import views

urlpatterns=[ 
    path ('',views.home, name='home'),
    path ('shows',views.all_shows), 
    path ('shows/new',views.new_show, name='new_show'),
    path ('shows/create',views.create, name='create'),
    path ('shows/<number>',views.view_show, name='view_show'),
    path ('shows/<number>/edit',views.edit_show, name='edit_show'),
    path ('shows/<number>/update',views.update, name='update'),
    path ('shows/<number>/destroy',views.destroy, name='destroy'), 
]