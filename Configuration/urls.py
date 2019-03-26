from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'find_company_id$', views.find_company_id, ),
]
