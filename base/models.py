from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    
    
    phone_number = models.CharField(max_length=15, blank=True, null=True,unique=True,verbose_name="Номер Телефона")
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username + ' ' +self.first_name + ' ' + self.last_name

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    work_time_start = models.TimeField()
    work_time_end = models.TimeField()
    x_size = models.IntegerField()
    y_size = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + ' ' + self.address


class ClubsComputer(models.Model):
    computer_number = models.IntegerField()
    is_near_to_next = models.BooleanField(default=False)
    is_near_to_prev = models.BooleanField(default=False)
    gpu = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    x_pos = models.IntegerField()
    y_pos = models.IntegerField()
    instance = models.ForeignKey('Instance', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Computer {self.computer_number} at {self.club.name}"
    

class Appointment(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    club_computer = models.ForeignKey(ClubsComputer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserMainTransaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

class UserBonusTransaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

class Instance(models.Model):
    name = models.CharField(max_length=100)
    icon_url = models.URLField()

    def __str__(self):
        return self.name
# # class Room(models.Model):
# #     ROOM_TYPE_CHOICES = [
# #         ('VIP', 'VIP Room'),
# #         ('REGULAR', 'Regular Room'),
# #     ]
# #     club = models.ForeignKey(Club, on_delete=models.CASCADE)
# #     room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
# #     number_of_pc = models.IntegerField(default=0)
# #     number_of_consoles = models.IntegerField(default=0)
# #     is_available = models.BooleanField(default=True)

# #     def __str__(self):
# #         return self.username

# # Каждое устройство в зале
# class Device(models.Model):
#     DEVICE_TYPE_CHOICES = [
#         ('PC', 'PC'),
#         ('CONSOLE', 'Console'),
#     ]
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     device_type = models.CharField(max_length=10, choices=DEVICE_TYPE_CHOICES)
#     is_available = models.BooleanField(default=True)

#     def __str__(self):
#         return self.username


# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     club = models.ForeignKey(Club, on_delete=models.CASCADE)
#     device = models.ForeignKey(Device, on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     is_confirmed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.username


# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_date = models.DateTimeField(auto_now_add=True)
#     transaction_type = models.CharField(max_length=50, choices=[('CREDIT', 'Credit'), ('DEBIT', 'Debit')])
#     description = models.CharField(max_length=200)

#     def __str__(self):
#         return self.username


# class Package(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     hours = models.IntegerField()  # Сколько часов включает пакет
#     description = models.TextField()

# def __str__(self):
#         return self.username


# class Bonus(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     earned_at = models.DateTimeField(auto_now_add=True)
#     expires_at = models.DateTimeField()

# def __str__(self):
#         return self.username
