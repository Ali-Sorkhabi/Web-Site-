from django.shortcuts import render
from django.views.generic import TemplateView

class UserAccountView(TemplateView):
    template_name = 'useraccount.html'  # فاصله اضافی حذف شد

class SupportView(TemplateView):
    template_name = 'support.html'

class UploadView(TemplateView):
    template_name = 'upload.html'  # قبلاً کامنت شده و نام اشتباه بود

class ContactView(TemplateView):
    template_name = 'contact.html'
