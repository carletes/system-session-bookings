from django.db import models


__all__ = [
    "SystemSession",
]


class SystemSession(models.Model):

    URGENCY_CHOICES = (
        ("default", "Default"),
        ("high", "High")
    )

    IMPACT_CHOICES = (
        ("definite", "Definite"),
        ("potential", "Potential")
    )

    IMPACT_PROBABILITY_CHOICES = ((i, i) for i in range(6))

    IMPACT_SEVERITY_CHOICES = ((i, i) for i in range(6))

    title = models.CharField(max_length=256)
    services = models.CharField(max_length=128,
                                help_text="Systems and services that will be "
                                          "worked on")
    start_date = models.DateTimeField()
    impl_time = models.PositiveIntegerField(verbose_name="Implementation time",
                                            help_text="Length (in minutes) "
                                                      "of the system session")
    rollback_time = models.PositiveIntegerField(help_text="Time (in minutes) "
                                                          "required for "
                                                          "rollback")
    responsible = models.CharField(max_length=128,
                                   help_text="Person(s) involved")
    purpose = models.TextField()

    urgency = models.CharField(choices=URGENCY_CHOICES,
                               max_length=32,
                               default="default")
    impact_level = models.CharField(choices=IMPACT_CHOICES,
                                    max_length=32,
                                    blank=True)
    ops_impact = models.TextField(verbose_name="Operational impact",
                                  help_text="Expected impact on operations")
    high_risk_period = models.BooleanField(default=False,
                                           help_text="High risk period "
                                                     "requested")

    svc_impact = models.TextField(verbose_name="Impact on services",
                                  help_text="Expected impact on other "
                                            "services")
    impact_probability = models.PositiveIntegerField(default=0,
                                                     choices=IMPACT_PROBABILITY_CHOICES,
                                                     help_text="0: Unlikely, "
                                                               "5: Almost certain")
    impact_severity = models.PositiveIntegerField(default=0,
                                                  choices=IMPACT_SEVERITY_CHOICES,
                                                  help_text="0: No impact, "
                                                            "5: Very serious")
    worst_case_scenario = models.TextField(help_text="Worst case scenario "
                                                     "and exit strategy")

    standby = models.CharField(max_length=256, blank=True,
                               help_text="Person(s) required on standby "
                                         "during the session")
    approved = models.BooleanField(default=False, editable=False)

    owner = models.CharField(max_length=128,
                             editable=False)

    class Meta:
        ordering = ["start_date"]
        permissions = (
            ("can_approve", "Can approve system sessions"),
        )

    def __unicode__(self):
        return self.title
