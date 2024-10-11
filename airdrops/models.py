from django.db import models

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
    image = models.ImageField(upload_to='airdrops/', null=True, blank=True)  # Optional image field

    def __str__(self):
        return self.name
