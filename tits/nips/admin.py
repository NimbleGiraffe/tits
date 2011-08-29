from django.contrib import admin
from nips.models import Nipple, NippleOpinion

class NippleAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'score', 'votes', 'hometown']
    search_fields = ['first_name', 'last_name', 'high_school']
    
class NippleOpinionAdmin(admin.ModelAdmin):
    list_display = ['user', 'nipple', 'score', 'comment']
    search_fields = ['user__first_name', 'user__last_name', 'nipple__first_name', 'nipple__last_name']
    
admin.site.register(Nipple, NippleAdmin)
admin.site.register(NippleOpinion, NippleOpinionAdmin)