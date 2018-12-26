from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Question, Contest, Tag, Notice, Event
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Q


def events(request):
    event_list = Event.objects.all()
    return render(request, 'events.html',{'Events':event_list})


class NoticeListView(ListView):
    model = Notice
    template_name = "notice_list.html"

    def get_queryset(self):
        queryset = Notice.objects.all().order_by("-date")
        queryset = queryset.filter(publish=True)

        return queryset


class AboutUs(TemplateView):
    template_name = "aboutus.html"


class ContactUs(TemplateView):
    template_name = "contactus.html"


class ContestDetailView(DetailView):
    model = Contest
    template_name = "contest_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ContestDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        obj = get_object_or_404(Contest, pk=pk)
        if obj.publish is False:
            raise Http404

        context['object'] = obj
        return context


class ContestListView(ListView):
    model = Contest
    template_name = "contest_list.html"

    def get_queryset(self):
        queryset = Contest.objects.all().order_by('-contest_date')
        queryset = queryset.filter(publish=True)
        div = self.request.GET.get('div' or None)

        if div:
            div = div.replace(" ", "").lower()
            queryset = queryset.filter(division__iexact=div)

        return queryset


class ProblemDetailView(DetailView):
    model = Question
    template_name = "question_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProblemDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        obj = get_object_or_404(Question, pk=pk)

        if not obj.publish:
            raise Http404

        context['object'] = obj
        return context


class QuestionListView(ListView):
    model = Question
    template_name = "question_list.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        queryset = Question.objects.filter(publish=True)
        level = self.request.GET.get('level' or None)
        tag = self.request.GET.get('tag' or None)
        qry = self.request.GET.get('qry' or None)

        if qry:
            queryset = queryset.filter(
                Q(name__icontains=qry) |
                Q(description__icontains=qry)
            ).distinct()

        if tag:
            queryset = queryset.filter(tag__name__iexact=tag)

        if level:
            queryset = queryset.filter(level__iexact=level)

        queryset = queryset.order_by("-id")

        return queryset
