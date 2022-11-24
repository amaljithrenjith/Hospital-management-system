from django.urls import path
from . import views
from django.conf.urls.static import static
from xml.dom.minidom import Document
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('theme/',views.theme,name='theme'),
    path('doctors/',views.doctors,name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)