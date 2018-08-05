from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        """fields = ('first_name', 'last_name', 'email', 'contact',
                  'user_role', 'warehouse_exchange_id')"""
        fields = ('email', 'user_role')
