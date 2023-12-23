from django.db import models

POWER = [(1, "low"), (2, "medium"), (3, "high"), ]


class Tag(models.Model):
    name = models.CharField(max_length=100)

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


class Script(models.Model):
    name = models.CharField(max_length=100)
    script = models.FileField(upload_to="")

    def __str__(self):
        return f"{self.name}"


class Workflow(models.Model):
    name = models.CharField(max_length=100)
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    vulnerability = models.ManyToManyField('Vulnerability', blank=True)
    previous_workflows = models.ManyToManyField('Workflow', related_name='next_workflows', blank=True)

    def __str__(self):
        return f"{self.name} - {', '.join([vuln.name for vuln in self.vulnerability.filter()])}"


class Vulnerability(models.Model):
    name = models.CharField(max_length=100)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    power = models.IntegerField(choices=POWER)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def workflows(self):
        root = Workflow.objects.filter(vulnerability__id=self.id, previous_workflows=None).get()
        wfs = [root]
        while len(wfs) > 0 and len(wfs[-1].next_workflows.filter(vulnerability__id=self.id)) > 0:
            wfs.append(wfs[-1].next_workflows.filter(vulnerability__id=self.id).get())
        print(wfs)
        return wfs
