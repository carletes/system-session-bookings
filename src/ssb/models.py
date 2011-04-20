from django.db import models


__all__ = [
    "SystemSession",
]


class SystemSession(models.Model):

    STATUS_CHOICES = (
        ("pending", "Aproval pending"),
        ("approved", "Aproved"),
        ("canceled", "Canceled"),
    )

    title = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=max(len(c[0]) for c in STATUS_CHOICES),
                              default="pending")

    class Meta:
        ordering = ["start_date"]

    def __unicode__(self):
        return self.title
