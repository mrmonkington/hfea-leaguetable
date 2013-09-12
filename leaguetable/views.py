# Create your views here.
from django.shortcuts import render
import hfeascrape.models
import django_tables2 as tables

class PercentageColumn(tables.Column):
    def render(self, value):
        return "%.1f%%" % (100 * value,)

class LeagueTable(tables.Table):
    website = tables.URLColumn()
    hfea_link = tables.URLColumn()
    live_births_per_cycle = PercentageColumn()
    class Meta:
        model = hfeascrape.models.Unit
        exclude = ('id','hfea_code')

def units(request):
    return render(request, "units.html", {"units": LeagueTable(hfeascrape.models.Unit.objects.all())})
