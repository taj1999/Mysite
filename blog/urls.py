from . import views
from django.urls import path
from django.urls import include

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
	path('', views.home, name='home'),
	path('education/', views.education, name='education'),
	path('resume/', views.resume, name='resume'),
	path('achievements/', views.achievements, name='achievements'),
	path('projects/', views.projects, name='projects'),
	path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
	
	
] 
