from django.contrib import admin
from tg.models import BusRoutes
from tg.models import UserPrefHist
from tg.models import PoribohonRoutes
from tg.models import PlaceLocs
from tg.models import HubLocs

#username:Sumit pass: Django#001

# Register your models here.
admin.site.register(BusRoutes)
admin.site.register(UserPrefHist)
admin.site.register(PoribohonRoutes)
admin.site.register(PlaceLocs)
admin.site.register(HubLocs)
