import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username', 'email', 'campus_type']

    def __init__(self, *args, **kwargs):
        super(UserFilter, self).__init__(*args, **kwargs)
        self.filters['username'].label = "Ім'я користувача"
        self.filters['email'].label = "Ел. Пошта"
        self.filters['campus_type'].label = "Статус"
        for key in self.filters:
            self.filters[key].field.widget.attrs.update({'class': 'form-control'})