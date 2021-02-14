from django.contrib import admin
from admini.models import Member, Reunion, Treasury, BoardMembers
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('amci', 'nom','prenoms','mail','annee_bourse')
    ordering = ('nom',)
    search_fields = ('nom',)

admin.site.register(Member, MemberAdmin)

class ReunionAdmin(admin.ModelAdmin):
    list_display = ('nom','pdf')
    ordering = ('nom',)
    search_fields = ('nom',)
admin.site.register(Reunion, ReunionAdmin)

class TreasuryAdmin(admin.ModelAdmin):
    list_display = ('nom','prix','date')
    ordering = ('date',)
    search_fields = ('nom',)

admin.site.register(Treasury, TreasuryAdmin)

class BoardMembersAdmin(admin.ModelAdmin):
    list_display = ('nom','prenoms','statut')
    ordering = ('nom',)
    search_fields = ('nom',)
admin.site.register(BoardMembers, BoardMembersAdmin)
