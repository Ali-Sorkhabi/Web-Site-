from django.contrib import admin
from .models import UserAccount 
from .models import Upload 
from .models import Support 
from .models import Contact 
admin.site.register(UserAccount)
admin.site.register(Upload)
admin.site.register(Support)
admin.site.register(Contact)
# Register your models here.
