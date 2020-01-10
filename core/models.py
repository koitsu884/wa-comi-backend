from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class BaseDataModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# -------------- Common ----------------
class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# --------------- User -----------------
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Profile(BaseDataModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    introduction = models.CharField(max_length = 1000, blank = True)
    area = models.ForeignKey(
        Area,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    main_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.name

# ----------------- Group --------------------
class Group(BaseDataModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    main_image = models.ImageField(null=True, blank=True)
    area = models.ForeignKey(
        Area,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    description = models.TextField()

    def __str__(self):
        return self.name