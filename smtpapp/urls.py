from django.urls import path
from . import  views
from . import mailsender




urlpatterns = [
    path('mail/',views.smtp_view),

]