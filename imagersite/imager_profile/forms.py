"""Imager Images forms."""
from django import forms

from imager_profile.models import ImagerProfile, User

from django.forms import inlineformset_factory


class UpdateProfileForm(forms.ModelForm):
    """Update profile form."""

    class Meta:
        """Meta."""

        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


FormWrapper = inlineformset_factory(User, ImagerProfile, fields='__all__')


# BookFormSet = inlineformset_factory(Author, Book, fields=('title',))
# >>> author = Author.objects.get(name='Mike Royko')
# >>> formset = BookFormSet(instance=author)
