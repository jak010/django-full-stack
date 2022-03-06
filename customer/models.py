from django.db import models


class Customers(models.Model):
    customernumber = models.IntegerField(db_column='customerNumber', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=50)  # Field name made lowercase.
    contactlastname = models.CharField(db_column='contactLastName', max_length=50)  # Field name made lowercase.
    contactfirstname = models.CharField(db_column='contactFirstName', max_length=50)  # Field name made lowercase.
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(db_column='addressLine1', max_length=50)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    postalcode = models.CharField(db_column='postalCode', max_length=15, blank=True,
                                  null=True)  # Field name made lowercase.
    country = models.CharField(max_length=50)
    # TODO: Employees 모델 작업시 업데이트 필요
    # salesrepemployeenumber = models.ForeignKey('Employees', models.DO_NOTHING, db_column='salesRepEmployeeNumber',
    #                                            blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='creditLimit', max_digits=10, decimal_places=2, blank=True,
                                      null=True)  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'customers'

    def __str__(self):
        return f"{self.customername}: {self.customername}"
