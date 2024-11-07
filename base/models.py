from datetime import time
from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True,unique=True,verbose_name="Номер Телефона")
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True,verbose_name="Роль")
    last_latitude = models.DecimalField(max_digits=9, decimal_places=6,verbose_name="Широта",null=True)
    last_longitude = models.DecimalField(max_digits=9, decimal_places=6,verbose_name="Долгота",null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Баланс",default=0)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Club(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название Клуба')
    description = models.TextField(verbose_name="Описание",null=True)
    address = models.CharField(max_length=200,verbose_name="Адрес")
    city = models.CharField(max_length=100,verbose_name="Город")
    district = models.CharField(max_length=100,verbose_name="Район",null=True)
    postal_code = models.CharField(max_length=10,verbose_name="Почтовый Индекс",null=True)
    work_time_start = models.TimeField(verbose_name="Время Открытия")
    work_time_end = models.TimeField(verbose_name="Время Закрытия")
    x_size = models.IntegerField(verbose_name="Размер по X")
    y_size = models.IntegerField(verbose_name="Размер по Y")
    longitude = models.DecimalField(max_digits=9, decimal_places=5,verbose_name="Долгота")
    latitude = models.DecimalField(max_digits=9, decimal_places=5,verbose_name="Широта")
    phone_number = models.CharField(max_length=15, blank=True, null=True,unique=True,verbose_name="Номер Телефона")
    instagram_url = models.CharField(max_length=255,verbose_name="Instagram",null=True)
    whatsapp_url = models.CharField(max_length=255,verbose_name="Whatsapp",null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1,verbose_name="Рейтинг",default=0)
    website = models.URLField(verbose_name="Сайт",null=True)
    twogis_url = models.URLField(verbose_name="2gis",null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name="Владелец")
    
    def __str__(self):
        return self.name + ' ' + self.address
    
    def display_working_hours(self):
        # Define the 24/7 time range
        twenty_four_seven_start = time(0, 0)      # 00:00
        twenty_four_seven_end = time(23, 59)      # 23:59

        if self.work_time_start == twenty_four_seven_start and self.work_time_end == twenty_four_seven_end:
            return "24/7"
        else:
            start_time = self.work_time_start.strftime('%H:%M')
            end_time = self.work_time_end.strftime('%H:%M')
            return f"{start_time} - {end_time}"

class ClubImage(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE,verbose_name="Клуб",related_name='images')
    image = models.ImageField(upload_to='club_images/',verbose_name="Изображение")

    def __str__(self):
        return f"Images of {self.club.name}"
    
class ClubsComputer(models.Model):
    computer_number = models.IntegerField(verbose_name="Номер Компьютера")
    is_near_to_next = models.BooleanField(default=False,verbose_name="Рядом с Следующим")
    is_near_to_prev = models.BooleanField(default=False,verbose_name="Рядом с Предыдущим")
    gpu = models.CharField(max_length=100,verbose_name="Видеокарта")
    cpu = models.CharField(max_length=100,verbose_name="Процессор")
    ram = models.CharField(max_length=100,verbose_name="Оперативная Память")
    club = models.ForeignKey(Club, on_delete=models.CASCADE,verbose_name="Клуб")
    x_pos = models.IntegerField(verbose_name="Позиция по X")
    y_pos = models.IntegerField(verbose_name="Позиция по Y")
    is_active = models.BooleanField(default=True,verbose_name="Активен")
    instance = models.ForeignKey('Instance', on_delete=models.SET_NULL, null=True,verbose_name="Инстанс")


    def __str__(self):
        return f"Computer {self.computer_number} at {self.club.name}"
    

class Appointment(models.Model):
    start_date = models.DateTimeField(verbose_name="Дата Начала")
    end_date = models.DateTimeField(verbose_name="Дата Окончания")
    is_active = models.BooleanField(default=True,verbose_name="Активен")
    club_computer = models.ForeignKey(ClubsComputer, on_delete=models.CASCADE,verbose_name="Компьютер")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Пользователь")

class UserMainTransaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Сумма")
    transaction_type = models.CharField(max_length=50,verbose_name="Тип Транзакции")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Пользователь")
    club = models.ForeignKey(Club, on_delete=models.CASCADE,verbose_name="Клуб")

class UserBonusTransaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Сумма")
    transaction_type = models.CharField(max_length=50,verbose_name="Тип Транзакции")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Пользователь")
    club = models.ForeignKey(Club, on_delete=models.CASCADE,verbose_name="Клуб")

class Instance(models.Model):
    name = models.CharField(max_length=100,verbose_name="Название")
    icon_url = models.URLField(verbose_name="URL на иконку")

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
#       return self.username


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
