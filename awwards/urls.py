from  django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'profile', views.ProfileViewSet)
# router.register(r'project', views.ProjectViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('new/profile/',views.new_profile, name='profile'),
    path('project/', views.project, name='project'),
    path('rating/<int:pk>/',views.rating,name='rating'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT)