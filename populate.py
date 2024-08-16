import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gucc.settings')
django.setup()

from gucc_app.models import Committee, Helmet, Kayak, Paddle, BA, Spraydeck, Ball, Miscellaneous, Pool, Wetsuit, Garscube, MacPherson

# Create records for each committee position
positions = [
    {'position': 'Commodore', 'blurb': 'Leader of the fleet.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Fiona'},
    {'position': 'Secretary', 'blurb': 'Keeps all the records.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Emma'},
    {'position': 'Treasurer', 'blurb': 'Manages the funds.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Sophia'},
    {'position': 'Trip', 'blurb': 'Coordinates all trips(fun intro/blurb of the person).', 'img': '/images/canoe_club_logo.jpg', 'name': 'Junyi'},
    {'position': 'Social', 'blurb': 'Plans social events.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Liz'},
    {'position': 'Social', 'blurb': 'Plans social events.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Annie'},
    {'position': 'Development', 'blurb': 'Focuses on club growth.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Ruaridh'},
    {'position': 'Publicity', 'blurb': 'Handles promotions.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Patrick'},
    {'position': 'Welfare', 'blurb': 'Ensures member wellbeing.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Ella'},
    {'position': 'Shipwright', 'blurb': 'Maintains the kayaks.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Ossain'},
    {'position': 'Competition', 'blurb': 'Organizes competitions.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Jen'},
    {'position': 'Safety', 'blurb': 'Looks after safety regulations.(fun intro/blurb of the person)', 'img': '/images/canoe_club_logo.jpg', 'name': 'Sean'},
]

for pos in positions:
    committee = Committee(**pos)
    committee.save()

# Create helmets
helmets = [
    Helmet(size='S', colour='Blue', type='Polo'),
    Helmet(size='L', colour='Black', type='Polo'),
    Helmet(size='M', colour='Black', type='Polo'),
    Helmet(size='L', colour='Black', type='Polo'),
    Helmet(size='S', colour='Yellow', type='Polo'),
    Helmet(size='M', colour='Yellow', type='Polo'),
    Helmet(size='L', colour='Yellow', type='Polo'),
    Helmet(size='S', colour='Yellow', type='Polo'),
    Helmet(size='M', colour='Yellow', type='Polo'),
    Helmet(size='L', colour='Yellow', type='Polo'),
    Helmet(size='L', colour='Yellow', type='Polo'),
    Helmet(size='L', colour='Yellow', type='Polo'),
    Helmet(size='L', colour='Yellow', type='Polo'),
    Helmet(size='L', colour='Red', type='Palm'),
    Helmet(size='L', colour='Red', type='Palm'),
]

for helmet in helmets:
    helmet.save()

# Create BAs
bas = [
    BA(type = 'Polo', maincolour='Yellow', innercolour='Black', number=1, size='M'),
    BA(type = 'Polo', maincolour='Yellow', innercolour='Black', number=3, size='M'),
    BA(type = 'Polo', maincolour='Yellow', innercolour='Black', number=4, size='M'),
    BA(type = 'Polo', maincolour='Yellow', innercolour='Black', number=5, size='M'),
    BA(type = 'Polo', maincolour='Yellow', innercolour='Black', number=6,   size='M'),
    BA(type = 'Polo', maincolour='Navy', innercolour='Blue', number=1, size='M'),
    BA(type = 'Polo', maincolour='Navy', innercolour='Blue', number=2, size='M'),
    BA(type = 'Polo', maincolour='Navy', innercolour='Blue', number=3, size='M'),
    BA(type = 'Polo', maincolour='Navy', innercolour='Blue', number=4, size='M'),
]

for ba in bas:
    ba.save()

# Create spraydecks
spraydecks = [
    Spraydeck(decksize='S', waistsize='S'),
    Spraydeck(decksize='M', waistsize='M'),
    Spraydeck(decksize='L', waistsize='L'),
    Spraydeck(decksize='S', waistsize='M'),
    Spraydeck(decksize='M', waistsize='L'),
    Spraydeck(decksize='L', waistsize='S'),
    Spraydeck(decksize='S', waistsize='L'),
    Spraydeck(decksize='M', waistsize='S'),
    Spraydeck(decksize='L', waistsize='M'),
    Spraydeck(decksize='M', waistsize='M'),
]

for spraydeck in spraydecks:
    spraydeck.save()

# Create paddles
paddles = [
    Paddle(feather=45, material='Carbon', rightHanded=True, size='L', group = 'Polo'),
    Paddle(feather=45, material='Carbon', rightHanded=True, size='L', group = 'Polo'),
    Paddle(feather=45, material='Carbon', rightHanded=True, size='M', group = 'Polo'),
    Paddle(feather=45, material='Carbon', rightHanded=True, size='L', group = 'Polo'),
    Paddle(feather=45, material='Carbon', rightHanded=True, size='L', group = 'Polo'),
    Paddle(feather=45, material='Carbon', rightHanded=False, size='L', group = 'Polo'),
    Paddle(feather=90, material='Metal', rightHanded=True, size='L', group = 'Polo'),
    Paddle(feather=90, material='Metal', rightHanded=True, size='L', group = 'Polo'),
    Paddle(feather=90, material='Cow', rightHanded=True, size='L', group = 'Polo'),
    Paddle(feather=45, material='Carbon', rightHanded=False, size='L', group = 'Polo'),
]

for paddle in paddles:
    paddle.save()

# Create kayaks
kayaks = [
    Kayak(type='ICAD', size='L', colour='Black', slot=1),
    Kayak(type='ICAD', size='L', colour='Black', slot=2),
    Kayak(type='ICAD', size='L', colour='Black', slot=3),
    Kayak(type='ICAD', size='S', colour='Black', slot=4),
    Kayak(type='ICAD', size='S', colour='White', slot=5),
    Kayak(type='Revenge', size='L', colour='Black', slot=6),
    Kayak(type='Plastic', size='L', colour='Yellow', slot=7),
    Kayak(type='Plastic', size='L', colour='Yellow', slot=8),
    Kayak(type='Playboat', size='S', colour='Blue', slot=9),
    Kayak(type='Playboat', size='L', colour='Pink', slot=10),
]

for kayak in kayaks:
    kayak.save()

# Create balls
balls = [Ball(size=5) for _ in range(3)]

for ball in balls:
    ball.save()

# Create miscellaneous items
misc_items = [Miscellaneous(description=f"Misc item {i}") for i in range(4)]

for item in misc_items:
    item.save()

# Create wetsuits
wetsuits = [
    Wetsuit(size='S'),
    Wetsuit(size='M'),
    Wetsuit(size='L'),
]

for wetsuit in wetsuits:
    wetsuit.save()

# Create pool and add items
pool = Pool()
pool.save()

pool.helmets.set(Helmet.objects.all())
pool.kayaks.set(Kayak.objects.all())
pool.paddles.set(Paddle.objects.all())
pool.bas.set(BA.objects.all())
pool.spraydecks.set(Spraydeck.objects.all())
pool.balls.set(Ball.objects.all())
pool.miscellaneous.set(Miscellaneous.objects.all())

# Save the pool object with related items
pool.save()

# Create Garscube and add items
garscube = Garscube()
garscube.save()

garscube.helmets.set(Helmet.objects.all())
garscube.kayaks.set(Kayak.objects.all())
garscube.paddles.set(Paddle.objects.all())
garscube.bas.set(BA.objects.all())
garscube.spraydecks.set(Spraydeck.objects.all())
garscube.wetsuits.set(Wetsuit.objects.all())
garscube.miscellaneous.set(Miscellaneous.objects.all())

# Save the Garscube object with related items
garscube.save()

# Create MacPherson and add items
macpherson = MacPherson()
macpherson.save()

macpherson.helmets.set(Helmet.objects.all())
macpherson.kayaks.set(Kayak.objects.all())
macpherson.paddles.set(Paddle.objects.all())
macpherson.bas.set(BA.objects.all())
macpherson.spraydecks.set(Spraydeck.objects.all())
macpherson.balls.set(Ball.objects.all())
macpherson.wetsuits.set(Wetsuit.objects.all())
macpherson.miscellaneous.set(Miscellaneous.objects.all())

# Save the MacPherson object with related items
macpherson.save()

print('Database populated successfully! yay! celebrate!')