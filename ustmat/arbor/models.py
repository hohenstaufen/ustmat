from django.contrib.gis.db import models


class Shape(models.Model):
    gid = models.IntegerField(primary_key=True)
    address_po = models.IntegerField(null=True, blank=True)
    address_fu = models.CharField(max_length=131, blank=True)
    objectid = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    struct_id = models.CharField(max_length=20, blank=True)
    common_nam = models.CharField(max_length=254, blank=True)
    botanical = models.CharField(max_length=254, blank=True, db_column='botanical_')
    diameter_b = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    tree_posit = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    geom = models.PointField(srid=0, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = u'stgd'


class Image(models.Model):
    file = models.ImageField(upload_to='image/')
    small_url = models.URLField()
    big_url = models.URLField()
    botanical_name = models.CharField(max_length=254, blank=True)



