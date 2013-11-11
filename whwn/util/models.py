from django.db import models
import datetime

class TimestampedModel(models.Model):
    """Used to attach *created at* and *updated at* timestamps for any model class
    that mixes this in."""
    created_at = models.DateTimeField(auto_now_add=True,
                                        default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True,
                                        default=datetime.datetime.now)
    class Meta:
        abstract = True


class LocatableModel(models.Model):
    """Give *latitude* and *longitude* properties to any model that mixes
    this in."""
    latitude = models.DecimalField(max_digits=8, decimal_places=3, null=True,
                                    blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, null=True,
                                    blank=True)
    def _get_point(self):
        if self.latitude and self.longitude:
            return Point(self.longitude, self.latitude)
        else:
            return Point(0, 0)
    def _set_point(self, point):
        self.latitude = point.y
        self.longitude = point.x
        self.save()
    point = property(_get_point, _set_point)
    class Meta:
        abstract = True


