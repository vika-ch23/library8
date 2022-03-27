from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_custom_user(sender, instance, created, **kwargs):
    if created:
        CustomerUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_custom_user(sender, instance, **kwargs):
    instance.customeruser.save()

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     password = models.CharField(max_length=25)
#     # password2 = models.CharField(max_length=25)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     objects = MyAccountManager()
#
#     def __str__(self):
#         return self.username
