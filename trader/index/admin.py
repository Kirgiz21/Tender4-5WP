from django.contrib import admin
from .models import Tender, TenderItem, Bidder, Bid, Award

admin.site.register(Tender)
admin.site.register(TenderItem)
admin.site.register(Bidder)
admin.site.register(Bid)
admin.site.register(Award)