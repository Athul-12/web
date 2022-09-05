from django.urls import path
from . import views

urlpatterns=[
    path('service',views.customer_service),
    path('review',views.customer_review)

]