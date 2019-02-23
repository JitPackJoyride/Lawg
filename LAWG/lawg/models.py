from django.db import models

# Create your models here.
class Matter(models.Model):
    matter = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.matter}"

class Client(models.Model):
    client = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.client}"

class Lawyer(models.Model):
    lawyer = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.lawyer}"

class Record(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    startTime = models.DateTimeField(null = True, blank = True)
    endTime = models.DateTimeField(null = True, blank = True)
    duration = models.DurationField()
    description = models.CharField(max_length=200)

    def calcDuration(self):
        self.duration = self.endTime - self.startTime
    
    def __str__(self):
        return f"Lawyer: {self.lawyer}, Matter: {self.matter}, Client: {self.client} for Duration: {self.duration}"