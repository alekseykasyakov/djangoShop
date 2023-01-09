from django.urls import path
from . import views


urlpatterns = [
    path('about', views.about, name='about'),
    path('faq', views.faq, name='faq'),
    path('shipping', views.shipping, name='shipping'),

]
