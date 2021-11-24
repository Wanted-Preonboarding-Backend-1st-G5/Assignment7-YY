from django.db                  import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email      = models.EmailField(max_length=255, unique=True)
    is_admin   = models.BooleanField(default=False)
    username   = models.CharField(max_length=10, default='', null=True, blank=True)
    first_name = models.CharField(max_length=10, default='', null=True, blank=True)
    last_name  = models.CharField(max_length=10, default='', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD  = 'email'
    # REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'users'