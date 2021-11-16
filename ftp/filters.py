import django_filters
from .models.models import T_user

class T_userFilter(django_filters.FilterSet):
    class Meta:
        model = T_user
        fields = {'ftpUsername': ['icontains'],
                  'dateExpiration': ['year__gt'],
                 }
