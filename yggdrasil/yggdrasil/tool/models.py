from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=100)
    command = models.CharField(max_length=500)
    install_script = models.TextField(max_length=500)
    install_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Parameter(models.Model):
    name = models.CharField(max_length=100)
    default_value = models.CharField(max_length=100)
    default_trigger = models.BooleanField()
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
