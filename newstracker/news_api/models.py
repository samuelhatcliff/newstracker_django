from django.db import models
from django.utils import timezone


class Story(models.Model):
    class Meta:
        db_table = 'Story'
    id = models.AutoField(primary_key=True)
    headline = models.TextField(blank=False)
    source = models.CharField(max_length=255)
    content_preview = models.TextField(blank=True)
    content_full = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.TextField(blank=False)
    image = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    sub = models.TextField(blank=True)
    pol = models.TextField(blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"ID: {self.id}, H:{self.headline}, S:{self.source}"


class Query(models.Model):
    class Meta:
        db_table = 'Query'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255, blank=True)
    default = models.BooleanField(blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField(default=10, blank=True, null=True)
    date_from = models.CharField(max_length=255, blank=True)
    date_to = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    sort_by = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    sa = models.CharField(max_length=255, default="", blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Default: {self.default}"