from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('display/', views.display), # aqui usar /<int:id>
    path('edit/', views.edit), # aqui usar /<int:id>
    path('courses/destroy/<int:id>/', views.destroy), # aqui usar /<int:id>
    path('other/', views.other), # aqui usar /<int:id>
    path('courses/destroy/ajax/<int:id>/', views.destroy_ajax), # aqui usar /<int:id>
]
