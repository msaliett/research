from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    investigators = models.ManyToManyField('Investigator',through='Assignment')
    pi = models.ForeignKey('Investigator', on_delete=models.SET_NULL, null=True, related_name='led_projects')
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title

class Investigator(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' '+ self.surname


class Assignment(models.Model):
	project = models.ForeignKey(Project, on_delete=models.RESTRICT)
	investigator = models.ForeignKey(Investigator, on_delete=models.RESTRICT)
	datein = models.DateField()
	dateout = models.DateField(null=True, blank=True)

class HourEntry(models.Model):
    project = models.ForeignKey(Project, on_delete=models.RESTRICT)
    investigator = models.ForeignKey(Investigator, on_delete=models.RESTRICT)
    hours = models.PositiveIntegerField()
    date = models.DateField()
 

