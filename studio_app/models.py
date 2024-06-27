from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class bookings(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=True)
    phone =models.CharField(max_length=20,null=True)
    event = models.CharField(max_length=10,null=True)
    other = models.CharField(max_length=10,null=True)
    date=models.CharField(max_length=30,null=True)
    time = models.CharField(max_length=30,null=True)
    place = models.CharField(max_length=10,null=True)
    amount=models.IntegerField()
    status = models.CharField(max_length=20, null=True)
    message = models.CharField(max_length=20, null=True)
    payment_status = models.CharField(max_length=20,default="not paid")




class appoinment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    purpose = models.CharField(max_length=100)
    date=models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    status = models.CharField(max_length=20,null=True)
    message = models.CharField(max_length=20, null=True)


class designs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    your=models.FileField(upload_to='media',null=True)
    model=models.ImageField(upload_to='media',null=True)
    explain = models.CharField(max_length=100)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    message = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20,default="not paid")

def __str__(self):
    return f'{self.user}'



class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f'{self.name}'


class addframe(models.Model):
    frame_name=models.CharField(max_length=20)
    frame_photo=models.ImageField(upload_to='media',null=True)
    price = models.IntegerField()
    no_photo = models.IntegerField()


class gallery(models.Model):
    image=models.ImageField(upload_to='media',null=True)
    explanation = models.CharField(max_length=20)




class contact(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.CharField(max_length=20)
    message=models.CharField(max_length=20)

class feedback(models.Model):
    name=models.CharField(max_length=20)
    message=models.CharField(max_length=20)


class frame_orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    frame_name = models.ForeignKey(addframe,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    img=models.ImageField(upload_to='media')
    # status = models.CharField(max_length=20)
    message = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20,default="not paid")





# <!-----------------------TRY PAGE---------------------------!>

class Cart_Item(models.Model):
    addframe = models.ForeignKey(addframe, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.addframe.frame_name}'