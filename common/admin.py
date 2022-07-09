from django.contrib import admin

admin.site.index_title = 'Home'
admin.site.site_title = 'Play2Learn Admin'
admin.site.site_header = 'Play2Learn Admin'

class DjangoGamesAdmin(admin.ModelAdmin):
    save_as = True
