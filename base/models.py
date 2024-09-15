from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.username

class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    #contact_info = models.CharField(max_length=100)
    description = models.TextField()
    vip_rooms = models.IntegerField()
    regular_rooms = models.IntegerField()
    available_pc = models.IntegerField()
    available_console = models.IntegerField()
    # opening_hours = models.CharField(max_length=100)  # Часы работы

    def __str__(self):
        return self.username

class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('VIP', 'VIP Room'),
        ('REGULAR', 'Regular Room'),
    ]
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    number_of_pc = models.IntegerField(default=0)
    number_of_consoles = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.username

# Каждое устройство в зале
class Device(models.Model):
    DEVICE_TYPE_CHOICES = [
        ('PC', 'PC'),
        ('CONSOLE', 'Console'),
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=50, choices=[('CREDIT', 'Credit'), ('DEBIT', 'Debit')])
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hours = models.IntegerField()  # Сколько часов включает пакет
    description = models.TextField()

def __str__(self):
        return self.username


class Bonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    earned_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

def __str__(self):
        return self.username
