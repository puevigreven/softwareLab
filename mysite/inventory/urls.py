from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/1/$', 'inventory.views.add'),
   # url(r'^all/$', 'appointments.views.all'),

]

