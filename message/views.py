from django.shortcuts import render, redirect
from django.views import View
from django.core.files.storage import FileSystemStorage
from .models import UserName, Upload, Support, Contact, Comment
from .forms import UploadForm, SupportForm, ContactForm, CommentForm, UserAccountForm
from django.views.generic import TemplateView
import uuid


class UploadView(View):
    template_name = 'upload.html'

    def get(self, request, *args, **kwargs):
        # فرم دیدگاه
        comment_form = CommentForm()
        comments = Comment.objects.all()

        # فایل‌ها با فیلتر درست
        images = Upload.objects.exclude(image='').exclude(image__isnull=True)
        audio = Upload.objects.exclude(audio='').exclude(audio__isnull=True)
        video = Upload.objects.exclude(video='').exclude(video__isnull=True)
        pdf = Upload.objects.exclude(pdf='').exclude(pdf__isnull=True)

        context = {
            'form': comment_form,
            'comments': comments,
            'images': images,
            'audio': audio,
            'video': video,
            'pdf': pdf,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # ثبت دیدگاه
        if 'submit_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.save()
                return redirect(request.path)

        # ثبت فایل‌ها
        uploaded_files = request.FILES.getlist('document')
        fs = FileSystemStorage()

        for file in uploaded_files:
            ext = file.name.split('.')[-1].lower()
            unique_filename = f"{uuid.uuid4().hex}_{file.name}"
            saved_file = fs.save(unique_filename, file)

            # ذخیره بر اساس نوع فایل
            if ext in ['jpg', 'jpeg', 'png', 'gif']:
                Upload.objects.create(title=file.name, image=saved_file)
            elif ext in ['mp3', 'wav', 'ogg']:
                Upload.objects.create(title=file.name, audio=saved_file)
            elif ext in ['mp4', 'mov', 'avi']:
                Upload.objects.create(title=file.name, video=saved_file)
            elif ext == 'pdf':
                Upload.objects.create(title=file.name, pdf=saved_file)

        return redirect(request.path)


class ContactView(TemplateView):
    template_name = 'contact.html'


class SupportView(TemplateView):
    template_name = 'support.html'


class UserNameView(TemplateView):
    template_name = 'username.html'
