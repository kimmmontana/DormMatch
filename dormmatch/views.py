from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from .models import DormInfo, TenantProfile

from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dorms'] = DormInfo.objects.all()
        return context
    
class WaitlistView(ListView):
    model = DormInfo
    template_name = 'waitlist.html'
    context_object_name = 'dorms'



class SoloDormView(ListView):
    model = DormInfo
    template_name = 'solodorm.html'
    context_object_name = 'dorms'

class AboutUsView(TemplateView):
    template_name = "aboutus.html"
    
class AccountView(TemplateView):
    template_name = "account.html"