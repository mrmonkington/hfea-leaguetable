from django.db import models

# Create your models here.

class Unit(models.Model):
    name = models.TextField(max_length = 250, verbose_name="Clinic name")
    hfea_code = models.IntegerField( unique=True, verbose_name="HFEA Code" )
    website = models.TextField(max_length = 1024, blank = True, verbose_name="Official website" )
    live_births_per_cycle = models.FloatField(
        blank = True,
        verbose_name="Live births per ART (IVF+ICSI) cycle"
        )
    live_births_per_icsi_cycle = models.FloatField(
        blank = True,
        verbose_name="Live births per ICSI cycle"
        )
    live_births_per_icsi_cycle_3year = models.FloatField(
        blank = True,
        verbose_name="Live births per ICSI cycle 3 year average"
        )
    hfea_link = models.TextField(
        max_length = 1024,
        verbose_name="Link to this clinic on HFEA website"
        )
    overall_births = models.IntegerField(
        blank = True,
        verbose_name="Total ART (IVF+ICSI) births last year"
        )
    overall_embryos = models.IntegerField(
        blank = True,
        verbose_name="Total of all embryos transferred for all ART treatments (IVF+ICSI)"
        )
    overall_cycles = models.IntegerField(
        blank = True,
        verbose_name="Overall number of ART cycles performed"
        )
    icsi_births = models.IntegerField(
        blank = True,
        verbose_name="Total ICSI births"
        )
    icsi_embryos = models.IntegerField(
        blank = True,
        verbose_name="Total embryos transferred due to ICSI"
        )
    icsi_cycles = models.IntegerField(
        blank = True,
        verbose_name="Total number of ICSI cycles performed"
        )
    icsi_births_3year = models.IntegerField(
        blank = True,
        verbose_name="3 year total number of births due to ICSI"
        )
    icsi_embryos_3year = models.IntegerField(
        blank = True,
        verbose_name="3 year total number of embryos transferred due to ICSI"
        )
    icsi_cycles_3year = models.IntegerField(
        blank = True,
        verbose_name="3 year total number of ICSI cycles performed"
        )
    tel = models.TextField(
        verbose_name="Telephone number of clinic"
        )
    last_updated = models.DateTimeField(
        null=True,
        verbose_name="Date last updated"
        )

    def save(self, *args, **kwargs):
        self.live_births_per_cycle = float(self.overall_births) / float(self.overall_cycles)
        self.live_births_per_icsi_cycle = float(self.icsi_births) / float(self.icsi_cycles)
        self.live_births_per_icsi_cycle_3year = float(self.icsi_births_3year) / float(self.icsi_cycles_3year)
        super(Unit, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
