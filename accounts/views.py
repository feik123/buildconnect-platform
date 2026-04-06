from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm
from contractors.models import Contractor
from jobs.models import City


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.object

        if form.cleaned_data.get('is_contractor'):
            if not Contractor.objects.filter(user=user).exists():
                city = City.objects.first()

                Contractor.objects.create(
                    user=user,
                    name=user.username,
                    description='New contractor',
                    city=city,
                    years_experience=1,
                )

            user.profile.is_contractor = True

        else:
            user.profile.is_contractor = False

        user.profile.save()

        login(self.request, self.object)
        return response
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('common:home')