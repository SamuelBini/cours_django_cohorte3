from django.contrib import admin

# Register your models here.

from .models import Auteur
admin.site.register(Auteur)

from .models import Editeur
admin.site.register(Editeur)

from .models import Rayon
admin.site.register(Rayon)

from .models import Theme
admin.site.register(Theme)

from .models import Mot_Cle
admin.site.register(Mot_Cle)

from .models import Abonné
admin.site.register(Abonné)

from .models import Pret
admin.site.register(Pret)

from .models import Livre
admin.site.register(Livre)