from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^work_types/$', views.TypeOfWorkList.as_view()),
    url(r'^work_types/(?P<pk>[0-9]+)/$', views.TypeOfWorkDetail.as_view()),
    url(r'^employees/$', views.EmployeeList.as_view()),
    url(r'^employees/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view()),
]