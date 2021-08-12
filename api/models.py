from django.db import models
from django.db.models.base import Model
from tastypie.resources import ModelResource
from movies.models import Movie

class MovieResource(ModelResource):
   class Meta:
      queryset = Movie.objects.all()
      resource_name = 'movies'
      excludes = ['date_created']