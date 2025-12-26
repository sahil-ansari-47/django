from django.urls import path
from .views import HomeView, ServicesView, BookingView, AboutView, ServiceDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'my_app'
urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('about/', AboutView.as_view(), name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)