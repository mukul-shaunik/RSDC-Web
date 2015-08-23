from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$',					views.home,		name='Home'),
    url(r'^About/$',				views.about,		name='About'),
    url(r'^Member/$',				views.member,		name='Member'),
    





    url(r'^ResearchGrants/$',			views.research_list,	name='ResearchList'),
    url(r'^TravelGrants/$',			views.travel_list,	name='TravelList'),
    url(r'^ConferenceGrants/$',			views.conference_list,	name='ConferenceList'),
    


    url(r'^ConferenceGrant/(?P<title>.*)/$',	views.conference_grant,	name='ConferenceGrant'), 
    url(r'^ResearchGrant/(?P<title>.*)$',	views.research_grant,	name='ResearchGrant'), 
    url(r'^TravelGrant/(?P<title>.*)/$',	views.travel_grant,	name='TravelGrant'), 
    



    url(r'^Fellowships/$',			views.fellowship_list,	name='FellowshipList'),
    url(r'^Fellowship/(?P<title>.*)/$',		views.fellowship,	name='Fellowship'),
    url(r'^Scholarships/$',			views.scholarship_list,	name='ScholarshipList'),
    url(r'^Scholarship/(?P<title>.*)/$',	views.scholarship,	name='Scholarship'),
    



    url(r'^ProjectCircle/$',			views.project_circle,	name='ProjectCircle'),
    url(r'^ResearchCircle/$',			views.research_circle,	name='ResearchCircle'),
    url(r'^InternCircle/$',			views.intern_circle,	name='InternCircle'),  
]
