from django.db import models

class Upload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')
    video = models.FileField(upload_to='video/')
    pdf = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.title


class Support(models.Model):
    FEEDBACK_CHOICES = [
        ('complaint', 'شکایات'),
        ('criticism', 'انتقادات'),
        ('question', 'سوالات'),
        ('other', 'سایر موارد'),
    ]

    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=FEEDBACK_CHOICES,
        default='other'
    )

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"


class Contact(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title


# مدل جدید برای Login / کاربر
class UserAccount(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # می‌تونی بعداً رمزگذاری کنی

    def __str__(self):
        return self.username
