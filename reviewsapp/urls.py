from django.conf.urls import url

from . import views

app_name = 'reviews'

urlpatterns = [
    url(r'^$', views.index, name='postreview'),
	url(r'reviews', views.reviewview, name='reviewview'),
]