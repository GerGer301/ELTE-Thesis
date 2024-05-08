from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import HistoricalLotteryTicket
# Register your models here.

class HistoricalLotteryTicketResource(resources.ModelResource):
    class Meta:
        model = HistoricalLotteryTicket
        fields = ('draw_id', 'draw_date', 'red_1', 'red_2', 'red_3', 'red_4', 'red_5', 'red_6', 'blue_1')

class HistoricalLotteryTicketAdmin(ImportExportModelAdmin):
    resource_class = HistoricalLotteryTicketResource
    list_display = ('draw_id', 'draw_date', 'red_1', 'red_2', 'red_3', 'red_4', 'red_5', 'red_6', 'blue_1')

admin.site.register(HistoricalLotteryTicket, HistoricalLotteryTicketAdmin)
