# sites.py
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

basic_site = MyAdminSite(name='myadminbasic')
advanced_site = MyAdminSite(name='myadminadvanced')