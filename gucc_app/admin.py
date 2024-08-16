from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Committee, Store, Pool, Helmet, Kayak, Paddle, BA, Spraydeck, Ball, Miscellaneous

admin.site.register(Committee)
admin.site.register(Pool)
admin.site.register(Helmet)
admin.site.register(Kayak)
admin.site.register(Paddle)
admin.site.register(BA)
admin.site.register(Spraydeck)
admin.site.register(Ball)
admin.site.register(Miscellaneous)
admin.site.register(Store)