from django.db import models
import datetime
class Airdrop(models.Model):
    name = models.CharField(max_length=255)
    listing_date = models.DateField(null=True, blank=True)  # Allows "N/A" by being optional
    overview = models.TextField()
    qualification = models.TextField()
    farming_ending_date = models.DateField(null=True, blank=True)  # Allows "N/A" by being optional
    whitepaper = models.URLField(blank=True)
    total_supply = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  # "N/A" for total supply
    supply_for_airdrop = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  # "N/A" for airdrop supply
    starting_link = models.URLField()
    image = models.ImageField(upload_to='airdrops/', null=True, blank=True)  


    
class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=255, unique=True)
    date_joined = models.DateField(default=datetime.date.today)
    last_login = models.DateField(null=True, blank=True,default=datetime.date.today)
    login_count = models.IntegerField(default=1)

    def __str__(self):
        return self.telegram_id
