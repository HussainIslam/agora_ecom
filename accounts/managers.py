from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager to create users based on emails rather than usernames
    """
    def create_user(self, email, password, **others):
        """
        Create and save a new user with email and password
        """
        if not email:
            raise ValueError(_('The email must be used'))
        if not password:
            raise ValueError(_('Password must be provided'))

        others.setdefault('is_staff', False)
        others.setdefault('is_superuser', False)
        others.setdefault('is_active', True)

        email = self.normalize_email(email)
        user = self.model(email=email, **others)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **others):
        """
        Create and save a new superuser with email and password
        """
        others.setdefault('is_staff', True)
        others.setdefault('is_superuser', True)
        others.setdefault('is_active', True)
        if others.get('is_staff') is not True:
            raise ValueError(_("Superuser must have 'staff' property"))
        if others.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have 'superuser' property"))
        return self.create_user(email, password, **others)