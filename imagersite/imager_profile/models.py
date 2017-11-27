"""Imager profile model."""
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ActiveManager(models.Manager):
    """Active user subclass."""

    def get_queryset(self):
        """Set query set for subclass."""
        return super(ActiveManager, self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Photographer profile model."""

    objects = models.Manager()
    active = ActiveManager()

    CAMERA_CHOICES = (('FL', 'Film'),
                      ('DG', 'Digital'),
                      ('PL', 'Polaroid'),
                      ('DG', 'Daguerreotype'))
    STYLE_CHOICES = (('PR', 'Portrait'),
                     ('SL', 'Still Life'),
                     ('NT', 'Nature'),
                     ('AB', 'Abstract'),
                     ('FS', 'Fashion'),
                     ('AD', 'Advertising'),
                     ('WL', 'Wildlife'),
                     ('WD', 'Wedding'),
                     ('BW', 'Black and White'),
                     ('MC', 'Macro'),
                     ('TP', 'Time Lapse'),
                     ('LS', 'Landscape'),
                     ('SP', 'Sports'))
    SERVICE_CHOICES = (('SS', 'Session'),
                       ('ED', 'Editing'),
                       ('CL', 'Coloring'),
                       ('PT', 'Printing'),
                       ('FR', 'Framing'),
                       ('AV', 'Advertising'),
                       ('TV', 'Travel'))
    location = models.CharField(max_length=180, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile')
    website = models.URLField()
    fee = models.DecimalField(max_digits=10, decimal_places=2,
                              blank=True, null=True)
    phone = models.CharField(max_length=12)
    bio = models.TextField(max_length=500)
    camera = models.CharField(choices=CAMERA_CHOICES, max_length=2)
    photo_style = models.CharField(choices=STYLE_CHOICES, max_length=2)
    service = models.CharField(choices=SERVICE_CHOICES, max_length=2)

    def __str__(self):
        """Print function displays username."""
        return self.user.username

    @property
    def is_active(self):
        """Return if user is active."""
        return self.user.is_active


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """Attach a profile after new user is created."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
