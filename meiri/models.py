from django.db import models


class DataCs(models.Model):
    subno = models.IntegerField(primary_key=True)
    date = models.DateField()
    bal = models.DecimalField(max_digits=26, decimal_places=6, blank=True, null=True)
    bal_c = models.DecimalField(max_digits=26, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_cs'
        unique_together = (('subno', 'date'),)

class DataMova(models.Model):
    branchno = models.IntegerField(primary_key=True)
    subno = models.IntegerField()
    date = models.DateField()
    bal = models.DecimalField(max_digits=26, decimal_places=6, blank=True, null=True)
    bal_c = models.DecimalField(max_digits=26, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_mova'
        unique_together = (('branchno','subno', 'date'),)