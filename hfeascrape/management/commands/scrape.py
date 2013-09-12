from django.core.management.base import BaseCommand
import os
from django.conf import settings

from hfeascrape.models import *
from hfeascrape.index import *

class Command( BaseCommand ):
    
    def handle( self, *args, **options ):
        clinics = get_all_clinic_data()
        for clinic in clinics:
            u, created = Unit.objects.get_or_create(
                hfea_code = clinic["code"],
                name = clinic[ "name" ],
                #code = clinic[ "code" ],
                #hfea_code = clinic[ "code" ],
                website = clinic[ "website" ],
                hfea_link = clinic["hfea_link"],
                overall_births = clinic["overall_births"],
                overall_embryos = clinic["overall_embryos"],
                overall_cycles = clinic["overall_cycles"],
                icsi_births = clinic["icsi_births"],
                icsi_embryos = clinic["icsi_embryos"],
                icsi_cycles = clinic["icsi_cycles"],
                icsi_births_3year = clinic["3year_icsi_births"],
                icsi_embryos_3year = clinic["3year_icsi_embryos"],
                icsi_cycles_3year = clinic["3year_icsi_cycles"],
                tel = clinic["tel"]
            )
            if created:
                pass
            #u.save()
