from django.urls import path

from . import views

urlpatterns = [
    path('cal/', views.cal_page, name='cal'),
    path('', views.index, name='index'),
    path('doCalTotal/', views.do_cal_total, name='do_cal_total')
]
