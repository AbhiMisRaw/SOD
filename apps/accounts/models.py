from django.db import models
from django.db import models


COUNTRIES = [
    ('IN', 'India'),
    ('US', 'United States'),
    ('CN', 'China'),
    ('JP', 'Japan'),
    ('HK', 'Hong Kong'),
    ('FR', 'France'),
    ('UK', 'United Kingdom'),
    ('CA', 'Canada'),
    ('KR', 'South Korea'),
    ('TW', 'Taiwan'),
    ('CH', 'Switzerland'),
    ('AU', 'Australia'),
    ('NL', 'Netherlands'),
    ('IR', 'Iran'),
    ('ZA', 'South Africa'),
    ('BR', 'Brazil'),
    ('SE', 'Sweden'),
    ('ES', 'Spain'),
    # add more countries
]

SUBSCRIPTION_TYPES = [
    ("F", "Free"),
    ("P", "Premium")
]

class UserProfile(models.Model):
    id: int = models.AutoField(auto_created=True, primary_key=True, verbose_name="ID")
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    user_id = models.IntegerField("user_id", blank=True, null=True)
    country = models.CharField(max_length=4, choices=COUNTRIES)
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_TYPES, default="F")
