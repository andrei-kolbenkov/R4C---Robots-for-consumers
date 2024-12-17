from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5,blank=False, null=False)
    status = models.CharField(max_length=20, choices=[('waiting', 'Waiting'), ('completed', 'Completed')],
                              default='waiting')

    def __str__(self):
        return f'{self.robot_serial} | {self.customer.email} | {self.status}'
