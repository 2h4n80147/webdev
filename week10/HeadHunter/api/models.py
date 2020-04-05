from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    city = models.CharField(max_length=300)
    address = models.TextField(default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,
                                related_name='vacancies', null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'description': self.description,
            'company': self.company.to_json()
        }
