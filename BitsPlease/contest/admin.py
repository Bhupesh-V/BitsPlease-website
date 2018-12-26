from django.contrib import admin
from .models import Question, Contest, Tag, Notice, Event


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish', 'date')


class ContestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publish', 'division', 'contest_date')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publish', 'tag', 'add_date', 'contest', 'answer')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Event)
