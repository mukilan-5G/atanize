from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^attendance/(?P<date>\d{4}-\d{2}-\d{2})/(?P<type_of_work>[0-9]+)/$', views.AttendanceList.as_view()),
    url(r'^attendance/(?P<pk>[0-9]+)/$', views.AttendanceDetail.as_view()),
]