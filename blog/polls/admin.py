from django.contrib import admin
from polls.models import Poll, Choice, Hacker

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Hacker)

#You can assign arbitrary HTML classes to each fieldset