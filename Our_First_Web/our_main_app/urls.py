from django.urls import path
from . import views
# '.' is the path to the target file

urlpatterns = [
	# path('', views.our_main_app, name='app1'),
	# path('app2', views.app2, name='app2'),

	path('', views.app1, name='app1'),
	path('about', views.about, name='about'),
]