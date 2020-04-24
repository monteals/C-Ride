from django.db import models

class CRideModel(models.Model):

    created = models.DateTimeField('created_at', auto_now_add = True, help_text = 'Date time on wich the object was created.')
    modified = models.DateTimeField('modified_at', auto_now = True, help_text = 'Date time on wich the object was last modified.')

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
    
class Person(CRideModel):
    first_name = models.CharField()
    last_name = models.CharField()

class MyPerson(Person):
    class Meta:
        proxy = True
    
    def say_hi(self, name):
        pass

MyPerson.objects.all()
ricardo = MyPerson.objects.get(pk=1)
ricardo.say_hi('Pablo')

