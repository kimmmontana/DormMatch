from django.urls import path
from .views import HomePageView, WaitlistView, SoloDormView, AboutUsView, AccountView

urlpatterns = [
    
    path('account/', AccountView.as_view(), name='account'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('solodorm/', SoloDormView.as_view(), name='solodorm'),
    path('waitlist/', WaitlistView.as_view(), name='waitlist'),
    path('', HomePageView.as_view(), name='home'),
    
]