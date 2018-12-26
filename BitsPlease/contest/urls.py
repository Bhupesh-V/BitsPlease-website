from django.conf.urls import url
from .views import (
    QuestionListView,
    ProblemDetailView,
    ContestListView,
    ContestDetailView,
    AboutUs,
    ContactUs,
    NoticeListView,
    events
)

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name="problems"),
    url(r'aboutus/', AboutUs.as_view(), name="aboutus"),
    url(r'notice/', NoticeListView.as_view(), name="notice"),
    url(r'contactus/', ContactUs.as_view(), name="contactus"),
    url(r'events/', events, name="events"),
    url(r'^problem/(?P<pk>\d+)', ProblemDetailView.as_view(), name="problem_detail"),
    url(r'^contest/$', ContestListView.as_view(), name="contests"),
    url(r'^contest/(?P<pk>\d+)', ContestDetailView.as_view(), name="contest_detail"),


]
