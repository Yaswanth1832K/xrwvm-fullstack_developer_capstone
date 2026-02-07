from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(default=1)   # ✅ FIX HERE
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"

class Dealership(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=20)
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class Review(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    review = models.TextField()
    purchase = models.BooleanField()
    purchase_date = models.CharField(max_length=50, blank=True, null=True) # Accepting string date from frontend
    car_make = models.CharField(max_length=50, blank=True, null=True)
    car_model = models.CharField(max_length=50, blank=True, null=True)
    car_year = models.IntegerField(blank=True, null=True)
    sentiment = models.CharField(max_length=20, blank=True, null=True) # To store analyzed sentiment

    def __str__(self):
        return f"Review for {self.dealership.full_name} by {self.name}"
