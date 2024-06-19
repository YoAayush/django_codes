from django.db import models


# Create your models here.
class emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    job = models.CharField(max_length=9)
    mgr = models.IntegerField()
    # hiredate = models.DateField()
    sal = models.IntegerField()
    comm = models.IntegerField()
    deptno = models.IntegerField()
    class Meta:
        db_table = "emp"
        
# class dept(models.Model):
    