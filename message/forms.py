from django import forms
from django.contrib.auth.models import User
from .models import Upload, Support, Contact

# ---------------- Upload Form ----------------
class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['title', 'image', 'audio', 'video', 'pdf']
        labels = {
            'image': 'Upload image',
            'audio': 'Upload audio',
            'video': 'Upload video',
            'pdf': 'Upload pdf',
        }

# ---------------- Support Form ----------------
class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['first_name', 'last_name', 'phone_number', 'subject', 'message']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تلفن',
            'subject': 'موضوع',
            'message': 'پیام',
        }

# ---------------- Contact Form ----------------
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'first_name', 'last_name', 'phone_number', 'subject', 'message']
        labels = {
            'title': 'عنوان پیام',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تلفن',
            'subject': 'موضوع',
            'message': 'پیام',
        }

# ---------------- User Registration Form ----------------
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'password']
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تلفن',
        }

# ---------------- User Login Form ----------------
class UserLoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')
