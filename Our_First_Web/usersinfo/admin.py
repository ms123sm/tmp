from django.contrib import admin
# Register your models here.

from .models import User, Player, PlayerHistory
admin.site.register(User)
admin.site.register(Player)
admin.site.register(PlayerHistory)