from django.urls import path
from django.views.generic import TemplateView

app_name = 'homepage'

urlpatterns = [
    # Serve the homepage index template at the app root.
    path('index', TemplateView.as_view(template_name='homepage/index.html'), name='index'),
]
