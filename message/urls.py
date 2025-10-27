from django.urls import path
from .views import UserNameView, UploadView, SupportView, ContactView  

urlpatterns = [
    path('', UserNameView.as_view(), name='username'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('support/', SupportView.as_view(), name='support'),
    path('contact/', ContactView.as_view(), name='contact'),

]
