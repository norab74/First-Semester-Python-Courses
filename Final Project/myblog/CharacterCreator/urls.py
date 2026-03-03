from django.urls import path
from . import views

app_name = 'charactercreator'

urlpatterns = [
    path('', views.list_characters, name='index'),
    path('create/', views.start_creation, name='start'),
    path('create/step1/', views.step1_basic, name='step1'),
    path('create/step2/', views.step2_background, name='step2'),
    path('create/step3/', views.step3_abilities, name='step3'),
    path('create/step4/', views.step4_combat, name='step4'),
    path('create/step5/', views.step5_skills, name='step5'),
    path('create/step6/', views.step6_equipment, name='step6'),
    path('create/review/', views.review, name='review'),
    path('create/success/<int:pk>/', views.creation_success, name='success'),
    path('load/<int:pk>/', views.load_character, name='load'),
]
