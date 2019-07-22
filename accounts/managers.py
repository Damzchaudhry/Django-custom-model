from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, user_type, **extra_fields):
        
        if username is None:
            raise TypeError('User must have a username.')

        if email is None:
            raise TypeError('User must have an email address.')
        
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user_type = self.user_type
        user = self.model(username=username, email=email, user_type=user_type, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        
        return user


    def create_user(self, username, email=None, password=None, user_type=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, user_type, **extra_fields)


    def create_superuser(self, username, email, password, user_type, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, user_type, **extra_fields)