"""Django profile app views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView

from imager_images.models import Photo

# from imager_profile.models import ImagerProfile
from imager_profile.forms import FormWrapper, UpdateProfileForm


class ProfileView(TemplateView):
    """User view class based view."""

    template_name = 'imager_profile/profile.html'


class GuestView(TemplateView):
    """Profile view class based view."""

    template_name = 'imager_profile/guest_profile.html'

    def get_context_data(self, username=None):
        """Get context data for view."""
        user = User.objects.get(username=username)
        photo = Photo.objects.order_by('?').first()
        return {'photo': photo,
                'user': user}


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    """Class based view to display form for updating and editing photos."""

    template_name = 'imager_profile/profile_update.html'
    form_class = UpdateProfileForm
    success_url = '/profile/'
    redirect_field_name = '/login/'

    def get_context_data(self, **kwargs):
        """."""
        data = super(ProfileUpdate, self).get_context_data(**kwargs)

        use = self.request.user
        formset = FormWrapper(instance=use)
        data['here'] = formset
        return data

        # data = super(ProfileUpdate, self).get_context_data(**kwargs)
        # if self.request.POST:
        #     data['here'] = formset(self.request.POST)
        # else:
        #     data['here'] = formset()
        # return data

    def get_object(self):
        """Get and return current user."""
        use = self.request.user
        return use
