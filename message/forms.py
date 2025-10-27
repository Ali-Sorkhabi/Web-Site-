from django import forms
from .models import UserName, Upload, Support, Contact, Comment

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
        fields = ['first_name', 'last_name', 'subject', 'message']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'subject': 'موضوع',
            'message': 'پیام',
        }

# ---------------- Contact Form ----------------
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'first_name', 'last_name', 'subject', 'message']
        labels = {
            'title': 'عنوان پیام',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'subject': 'موضوع',
            'message': 'پیام',
        }

# ---------------- User Registration Form ----------------
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')

    class Meta:
        model = UserName
        fields = ['username', 'first_name', 'last_name', 'password']
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }

# ---------------- User Login Form ----------------
class UserAccountForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')

# ---------------- Comment Form ----------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['first_name', 'last_name', 'subject', 'message']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'subject': 'موضوع',
            'message': 'پیام',
        }
