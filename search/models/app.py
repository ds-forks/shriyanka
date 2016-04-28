from .base import Base
from django.db import models

class Apps(Base):
	app_id = models.CharField(max_length=64, null=True, blank=True)
	app_name =  models.CharField(max_length=128, null=True, blank=True)
	developer_name =  models.CharField(max_length=128, null=True, blank=True)
	developer_email = models.EmailField(max_length=128)
	icon_url = models.URLField(max_length=256)


class SearchTerm(Base):
    term = models.CharField(max_length=128, primary_key=True)
    apps = models.ManyToManyField('Apps', related_name='apps', through='SearchResultApp')


class SearchResultApp(Base):
    app = models.ForeignKey('Apps')
    term = models.ForeignKey('SearchTerm')