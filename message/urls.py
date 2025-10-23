from django.urls import path
from .views import UserAccountView, UploadView, SupportView, ContactView

urlpatterns = [
    path('', UserAccountView.as_view(), name='useraccount '),
    path('upload/', UploadView.as_view(), name='upload'),
    path('support/', SupportView.as_view(), name='support'),
    path('contact/', ContactView.as_view(), name='contact'),
]
