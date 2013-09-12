from django.db import models

# Create your models here.

class Unit(models.Model):
    name = models.TextField(max_length = 250)
    hfea_code = models.IntegerField( unique=True )
    website = models.TextField(max_length = 1024, blank = True)
    live_births_per_cycle = models.FloatField(blank = True)
    live_births_per_icsi_cycle = models.FloatField(blank = True)
    live_births_per_icsi_cycle_3year = models.FloatField(blank = True)
    hfea_link = models.TextField(max_length = 1024)
    overall_births = models.IntegerField(blank = True)
    overall_embryos = models.IntegerField(blank = True)
    overall_cycles = models.IntegerField(blank = True)
    icsi_births = models.IntegerField(blank = True)
    icsi_embryos = models.IntegerField(blank = True)
    icsi_cycles = models.IntegerField(blank = True)
    icsi_births_3year = models.IntegerField(blank = True)
    icsi_embryos_3year = models.IntegerField(blank = True)
    icsi_cycles_3year = models.IntegerField(blank = True)
    tel = models.TextField()

    def save(self, *args, **kwargs):
        self.live_births_per_cycle = float(self.overall_births) / float(self.overall_cycles)
        self.live_births_per_icsi_cycle = float(self.icsi_births) / float(self.icsi_cycles)
        self.live_births_per_icsi_cycle_3year = float(self.icsi_births_3year) / float(self.icsi_cycles_3year)
        super(Unit, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
