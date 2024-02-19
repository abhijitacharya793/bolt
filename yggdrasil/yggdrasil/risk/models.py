from django.db import models

POWER = [(1, "low"), (2, "medium"), (3, "high"), ]
PART = [("h", "header"), ("b", "body"), ("q", "query param"), ]
SEVERITY = [("i", "info"), ("l", "low"), ("m", "medium"), ("h", "high"), ("c", "critical")]


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Fuzzing(models.Model):
    part = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    remediation = models.TextField(max_length=500, null=True, blank=True)
    steps_to_reproduce = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Risk(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    remediation = models.TextField(max_length=500, null=True, blank=True)
    steps_to_reproduce = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Vulnerability(models.Model):
    name = models.CharField(max_length=100)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    command = models.CharField(max_length=1000, null=True, blank=True)
    severity = models.CharField(max_length=10, choices=SEVERITY, default="i")
    power = models.IntegerField(choices=POWER)
    tag = models.ManyToManyField(Tag, blank=True)
    fuzzing_rules = models.ManyToManyField(Fuzzing, blank=True)

    def __str__(self):
        return f"{self.name}"

    # @property
    # def workflows(self):
    #     root = Workflow.objects.filter(vulnerability__id=self.id, previous_workflows=None).get()
    #     wfs = [root]
    #     while len(wfs) > 0 and len(wfs[-1].next_workflows.filter(vulnerability__id=self.id)) > 0:
    #         wfs.append(wfs[-1].next_workflows.filter(vulnerability__id=self.id).get())
    #     print(wfs)
    #     return wfs


class Template(models.Model):
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
    path = models.CharField(max_length=500)

