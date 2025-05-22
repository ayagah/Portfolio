from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Project, Skill, Profile
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all().order_by('-created_at')[:4]
        context['skills'] = Skill.objects.all()
        try:
            context['profile'] = Profile.objects.get(user=self.request.user)
        except:
            context['profile'] = None
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    ordering = ['-created_at']
    paginate_by = 6

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_details.html'

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            
            # Send email notification
            send_mail(
                f"New Portfolio Contact: {message.subject}",
                f"From: {message.name} <{message.email}>\n\n{message.message}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})