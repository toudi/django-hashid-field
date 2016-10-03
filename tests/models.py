from django.db import models

from hashid_field import HashidAutoField, HashidField


class Record(models.Model):
    name = models.CharField(max_length=40)
    reference_id = HashidField()
    key = HashidField(min_length=10, alphabet="abcdlmnotuvwxyz123789", null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.reference_id)


class Artist(models.Model):
    id = HashidAutoField(primary_key=True, min_length=20)
    name = models.CharField(max_length=40)

    def __str__(self):
        return "{} ({})".format(self.name, self.id)
