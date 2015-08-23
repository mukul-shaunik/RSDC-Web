from django.contrib import admin
from .models import ResearchGrant
from .models import TravelGrant
from .models import ConferenceGrant
from .models import Fellowship
from .models import Scholarship
from .models import Message
admin.site.register(ResearchGrant)
admin.site.register(TravelGrant)
admin.site.register(ConferenceGrant)
admin.site.register(Fellowship)
admin.site.register(Scholarship)
admin.site.register(Message)
# Register your models here.
