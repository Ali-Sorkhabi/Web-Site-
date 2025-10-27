from django.contrib import admin
from .models import UserName
from .models import Upload
from .models import Support
from .models import Contact
from .models import Comment

# ثبت مدل‌ها در پنل ادمین
admin.site.register(UserName)
admin.site.register(Upload)
admin.site.register(Support)
admin.site.register(Contact)
admin.site.register(Comment)
