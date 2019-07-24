from django.urls import path
from . import views
from . import views_cbv
from quiz.views import *

app_name = 'quiz'

urlpatterns = [


    path('<int:question_id>/vote/', views.vote, name='vote'),
]
