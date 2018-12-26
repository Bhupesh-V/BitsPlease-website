from django.db import models
from django.urls import reverse

LEVEL_CHOICES = (
    ('beginner', "Beginner"),
    ('easy', "Easy"),
    ('medium', "Medium"),
    ('hard', "Hard")
)

DIVISION_CHOICES = (
    ('div1', "Div 1"),
    ('div2', "Div 2")
)


class Notice(models.Model):
    title = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contest(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    winners = models.TextField(blank=True, default=None)
    publish = models.BooleanField(default=False)
    contest_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("contest:contest_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Question(models.Model):
    contest = models.ForeignKey('contest.Contest', blank=True, null=True, related_name='questions')
    tag = models.ForeignKey(Tag, blank=True, null=True, related_name='problems')
    name = models.CharField(max_length=200)
    description = models.TextField()
    testcases = models.TextField(null=True, blank=True, default=None)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    publish = models.BooleanField(default=False)
    Url1 = models.URLField(max_length=500, null=True, blank=True, default=None)
    Url2 = models.URLField(max_length=500, null=True, blank=True, default=None)
    Url3 = models.URLField(max_length=500, null=True, blank=True, default=None)
    Url4 = models.URLField(max_length=500, null=True, blank=True, default=None)
    Url5 = models.URLField(max_length=500, null=True, blank=True, default=None)
    answer = models.URLField(max_length=500, blank=True, default=None)
    add_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("contest:problem_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=False)
    speaker = models.TextField()
    registration_link = models.CharField(max_length=300)

    def __str__(self):
        return self.name