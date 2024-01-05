from django.contrib import admin

from .models import meeting
from .models import pgSenator
from .models import facultyExecutivebodie
from .models import studentExecutivebodie
from .models import ugSenator

# Register your models here.
admin.site.register(meeting)
admin.site.register(ugSenator)
admin.site.register(pgSenator)
admin.site.register(facultyExecutivebodie)
admin.site.register(studentExecutivebodie)