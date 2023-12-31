from django.db import models
from django.utils import timezone

# Create your models here.
class Club(models.Model):
    
    # Maximum club name length
    NAME_MAX_LEN = 30;
    
    # Name of club
    club_name = models.CharField(max_length=NAME_MAX_LEN, blank=False, default='', unique=True)
    
    # Description of club
    description = models.TextField(blank=True, default='')
    
    # Whether Club is verified or not
    verified = models.BooleanField(default=False)
    
    # Whether Club is open to anyone to join, or requires exec+ to accept invite
    public = models.BooleanField(default=True)
    
    # Ranking amongst all clubs
    # ranking = models.IntegerField(blank=True)
    
    
    # ---------- CLUB ROLES ---------- #
    # * Each User can only have one role in a club
    
    # Owner of this club
    # Many Club to one User relationship
    # Permissions:
    #   - Create and edit club contests (assuming club is verified)
    #   - Change club settings
    #   - Accept member join requests (assuming it is non-public club)
    club_owner = models.ForeignKey('user.User', blank=False, related_name='owner_of_these_clubs')
    
    # IMPLEMENT INTERMEDIATE ROLES LATER
    # # Admins of this club
    # # Many Club to many User relationship
    # club_admins = models.ManyToManyField('user.User', blank=True, related_name='admin_of_these_clubs')
    
    # # Executive of this club
    # # Many Club to many User relationship
    # club_execs = models.ManyToManyField('user.User', blank=True, related_name='exec_of_these_clubs')
    
    # Members of this club
    # Many Club to many User relationship
    members = models.ManyToManyField('user.User', blank=True, related_name='members_of_these_clubs')
    # ---------- CLUB ROLES ---------- #
    
    
    # Date and time club was founded
    # (Auto generated)
    date_time_founded = models.DateTimeField(default=timezone.now)