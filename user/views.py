from django.shortcuts import render, get_object_or_404
from .models import ResearchGrant
from .models import TravelGrant
from .models import ConferenceGrant
from .models import Fellowship
from .models import Scholarship
from .models import Message

def home(request):
	VC = get_object_or_404(Message, Post='Vice Chancelor')
	HOD = get_object_or_404(Message, Post='Head Of Department')
	Dean = get_object_or_404(Message, Post='Dean')
	return render(request, 'website/Home.html',{'VC':VC,'HOD':HOD,'Dean':Dean})
def about(request):
	return render(request, 'website/About.html',{})
def member(request):
	return render(request, 'website/Member.html',{})








def research_list(request):
	grants = ResearchGrant.objects.all()
	return render(request, 'website/ResearchGrants.html',{'grants':grants})
def travel_list(request):
	grants = TravelGrant.objects.all()
	return render(request, 'website/TravelGrants.html',{'grants':grants})
def conference_list(request):
	grants = ConferenceGrant.objects.all()
	return render(request, 'website/ConferenceGrants.html',{'grants':grants})




def research_grant(request,title):
	grants = ResearchGrant.objects.all()
	grant = get_object_or_404(ResearchGrant, title=title)
	return render(request, 'website/ResearchGrant.html',{'grant':grant, 'grants':grants})
def travel_grant(request,title):
	grants = TravelGrant.objects.all()
	grant = get_object_or_404(TravelGrant, title=title)
	return render(request, 'website/TravelGrant.html',{'grant':grant, 'grants':grants})
def conference_grant(request,title):
	grants = ConferenceGrant.objects.all()
	grant = get_object_or_404(ConferenceGrant, title=title)
	return render(request, 'website/ConferenceGrant.html',{'grant':grant, 'grants':grants})







def fellowship_list(request):
	grants = Fellowship.objects.all()
	return render(request, 'website/Fellowships.html',{'grants':grants})
def scholarship_list(request):
	grants = Scholarship.objects.all()
	return render(request, 'website/Scholarships.html',{'grants':grants})



def fellowship(request,title):
	grants = Fellowship.objects.all()
	grant = get_object_or_404(Fellowship, title=title)
	return render(request, 'website/Fellowship.html',{'grant':grant, 'grants':grants})
def scholarship(request,title):
	grants = Scholarship.objects.all()
	grant = get_object_or_404(Scholarship, title=title)
	return render(request, 'website/Scholarship.html',{'grant':grant, 'grants':grants})


def project_circle(request):
	return render(request, 'website/ProjectCircleGuest.html',{})
def intern_circle(request):
	return render(request, 'website/InternCircleGuest.html',{})
def research_circle(request):
	return render(request, 'website/ResearchCircleGuest.html',{})

# Create your views here.
