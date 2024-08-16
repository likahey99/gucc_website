from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Position(models.TextChoices):
    COMMODORE = 'Commodore', _('Commodore')
    SECRETARY = 'Secretary', _('Secretary')
    TREASURER = 'Treasurer', _('Treasurer')
    TRIP = 'Trip', _('Trip')
    SOCIAL = 'Social', _('Social')
    DEVELOPMENT = 'Development', _('Development')
    PUBLICITY = 'Publicity', _('Publicity')
    WELFARE = 'Welfare', _('Welfare')
    SHIPWRIGHT = 'Shipwright', _('Shipwright')
    COMPETITION = 'Competition', _('Competition')
    SAFETY = 'Safety', _('Safety')

class SML(models.TextChoices):
    S = 'S', _('Small')
    M = 'M', _('Medium')
    L = 'L', _('Large')

class Helmet(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20,default="Palm")
    size = models.CharField(
        max_length=1,
        choices=SML.choices,
        default=SML.L
    )
    colour = models.CharField(max_length=20, default="Yellow")

class Kayak(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, default="Creaker")
    size = models.CharField(
        max_length=1,
        choices=SML.choices,
        default=SML.L
    )
    colour = models.CharField(max_length=20, default="Black")
    hasairbags = models.BooleanField(default=False, blank=True)
    slot = models.PositiveIntegerField(default=0, blank=True)

class Paddle(models.Model):
    id = models.AutoField(primary_key=True)
    feather = models.IntegerField(default=45)
    material = models.CharField(max_length=20, default="Carbon")
    size = models.CharField(
        max_length=1,
        choices=SML.choices,
        default=SML.L
    )
    righthanded = models.BooleanField(default=True)
    group = models.CharField(default="none", max_length=20) #enum??

class BA(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, default="Polo") # enum polo river
    maincolour = models.CharField(max_length=20, default="Yellow")
    innercolour = models.CharField(max_length=20, default="Black") # nullable
    number = models.PositiveIntegerField(default=0) # nullable
    size = models.CharField(
        max_length=1,
        choices=SML.choices,
        default=SML.M
    )


class Spraydeck(models.Model):
    id = models.AutoField(primary_key=True)
    decksize = models.CharField(
        max_length=1,
        choices=SML.choices,
        default=SML.L
    )
    waistsize = models.CharField(
        max_length=1,
        choices=SML.choices,
        default=SML.L
    )

class Ball(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField(default=5)

class Wetsuit(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(
        max_length=1,
        choices=SML.choices,
        default=SML.M
    )

class Miscellaneous(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="random", max_length=30)
    description = models.TextField(default="")
    # type (throw line, sling, other)


class Pool(models.Model):
    helmets = models.ManyToManyField(Helmet)
    kayaks = models.ManyToManyField(Kayak)
    paddles = models.ManyToManyField(Paddle)
    bas = models.ManyToManyField(BA)
    spraydecks = models.ManyToManyField(Spraydeck)
    balls = models.ManyToManyField(Ball)
    miscellaneous = models.ManyToManyField(Miscellaneous)

class Garscube(models.Model):
    helmets = models.ManyToManyField(Helmet)
    kayaks = models.ManyToManyField(Kayak)
    paddles = models.ManyToManyField(Paddle)
    bas = models.ManyToManyField(BA)
    spraydecks = models.ManyToManyField(Spraydeck)
    wetsuits = models.ManyToManyField(Wetsuit)
    miscellaneous = models.ManyToManyField(Miscellaneous)


class MacPherson(models.Model):
    helmets = models.ManyToManyField(Helmet)
    kayaks = models.ManyToManyField(Kayak)
    paddles = models.ManyToManyField(Paddle)
    bas = models.ManyToManyField(BA)
    spraydecks = models.ManyToManyField(Spraydeck)
    balls = models.ManyToManyField(Ball)
    wetsuits = models.ManyToManyField(Wetsuit)
    miscellaneous = models.ManyToManyField(Miscellaneous)

class Store(models.Model):
    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=10)
    description = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

class Committee(models.Model):
    position = models.CharField(
        max_length=20,
        choices=Position.choices,
        default=Position.COMMODORE,
    )
    blurb = models.TextField()
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Record {self.position}"