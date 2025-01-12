from django.db import models


STATE = (
    ("1","Működik"),
    ("2","Hibás"),
    ("3","Nincs adat")
)

# Create your models here.
class Repont(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_created=True)
    created_ip = models.CharField(max_length=15)

    def get_state_value(self):
        obj = Statement.objects.filter(repont=self.pk).order_by("-created_at").first()

        if obj:
            return obj.state
        else:
            return 3


    def get_state(self):
        obj = Statement.objects.filter(repont=self.pk).order_by("-created_at").first()
        if obj:
            return obj
        else:
            return None

class Statement(models.Model):
    repont = models.ForeignKey(Repont,on_delete=models.CASCADE,related_name="get_statements")
    ip = models.CharField(max_length=15)
    state = models.CharField(max_length=1,choices=STATE)
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
    description = models.TextField(blank=True,null=True)

