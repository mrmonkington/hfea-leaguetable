# Create your views here.
from django.core.exceptions import *
from django.shortcuts import render, redirect
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
    sort = request.GET.get("sort")
    try:
        if sort:
            league = hfeascrape.models.Unit.objects.all().order_by("-"+sort)
        else:
            league = hfeascrape.models.Unit.objects.all()
        return render(request, "units.html", {"units": LeagueTable(league)})
    except FieldError:
        raise
        return redirect(units)
