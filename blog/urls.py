from django.conf.urls import url
from . import views

# CSyang
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]