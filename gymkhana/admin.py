from django.contrib import admin

from .models import meeting
from .models import pgSenator
from .models import facultyExecutivebodie
from .models import studentExecutivebodie
from .models import ugSenator
from .models import upcomingEvent
from .models import GirlSenator
from .models import landingPageImages

# Register your models here.
admin.site.register(meeting)
admin.site.register(ugSenator)
admin.site.register(pgSenator)
admin.site.register(facultyExecutivebodie)
admin.site.register(studentExecutivebodie)
admin.site.register(upcomingEvent)
admin.site.register(GirlSenator)
admin.site.register(landingPageImages)