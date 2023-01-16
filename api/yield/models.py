from django.db import models

# Create your models here.
class Yield(models.Model):
    year = models.IntegerField(primary_key=True)
    yield_corn = models.IntegerField()

    class Meta:
        db_table = 'yield_data'



from django.db import models

# Create your models here.
