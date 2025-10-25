from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import Upload
import uuid


# --- صفحه آپلود فایل ---
class UploadView(TemplateView):
    template_name = 'upload.html'

    def post(self, request, *args, **kwargs):
        uploaded_files = request.FILES.getlist('document')  # چند فایل همزمان
        context = {'images': [], 'audio': [], 'video': [], 'pdf': []}

        if not uploaded_files:
            return self.render_to_response({'error': 'هیچ فایلی انتخاب نشده است'})

        for uploaded_file in uploaded_files:
            fs = FileSystemStorage()
            unique_filename = f"{uuid.uuid4().hex}_{uploaded_file.name}"
            filename = fs.save(unique_filename, uploaded_file)
            file_url = fs.url(filename)

            # ذخیره در مدل
            Upload.objects.create(file=filename)

            # تشخیص نوع فایل
            file_ext = uploaded_file.name.split('.')[-1].lower()
            if file_ext in ['jpg', 'jpeg', 'png', 'gif']:
                context['images'].append({'file_url': file_url})
            elif file_ext in ['mp3', 'wav']:
                context['audio'].append({'file_url': file_url})
            elif file_ext in ['mp4', 'mov', 'avi']:
                context['video'].append({'file_url': file_url})
            elif file_ext in ['pdf']:
                context['pdf'].append({'file_url': file_url})

        return self.render_to_response(context)


# --- صفحه پشتیبانی ---
class SupportView(TemplateView):
    template_name = 'support.html'


# --- صفحه تماس با ما ---
class ContactView(TemplateView):
    template_name = 'contact.html'


# --- صفحه حساب کاربری ---
class UserAccountView(TemplateView):
    template_name = 'useraccount.html'
