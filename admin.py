# Django Imports
from django.contrib import admin, messages
from django.http import HttpResponse

# Standard Package Imports

# Project Imports
from .models import *

# Third Party Imports


class MemberAdmin(admin.ModelAdmin):
    #fields = ['image', 'description', 'project_details',
    #         'research_work', 'mail_id', 'facebook', 'linkedin', 'whatsapp']

    def save_model(self, request, obj, form, change):
        current_user = request.user
        print('Entered View')
        if (obj.name == (current_user.first_name + ' '+ current_user.last_name)) or (current_user.is_superuser):
            print('saved')
            return super(MemberAdmin, self).save_model(request, obj, form, change)
        else:
            print('Entered no access')
            messages.set_level(request, messages.ERROR)
            messages.error(request, "You don't have access to change this user.")


# Register your models here.
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Faq)
admin.site.register(Price)
admin.site.register(Member, MemberAdmin)
admin.site.register(viewMembers, MemberAdmin)
