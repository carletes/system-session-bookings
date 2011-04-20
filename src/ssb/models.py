from django.db import models


__all__ = [
    "SystemSession",
]


class SystemSession(models.Model):

    STATUS_CHOICES = (
        ("pending", "Aproval pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("canceled", "Canceled"),
    )

    title = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=max(len(c[0]) for c in STATUS_CHOICES),
                              default="pending",
                              editable=False)

    class Meta:
        ordering = ["start_date"]
        permissions = (
            ("can_change_status", "Can approve or cancel system sessions"),
        )

    def __unicode__(self):
        return self.title
