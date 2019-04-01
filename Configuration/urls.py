from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'find_company_id$', views.find_company_id, ),
    url(r'add_rtsp$', views.add_rtsp, ),
    url(r'see_rtsp$', views.see_rtsp, ),
    url(r'add_idconfig$', views.add_idconfig, ),
    url(r'login$', views.login, ),
    url(r'search_terminal$', views.search_terminal,),
    url(r'search_idconfig_by_terminal$', views.search_idconfig_by_terminal,),
]
