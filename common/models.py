# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from common.managers import UserManager


class IndexedTimeStampedModel(models.Model):
    created_at = AutoCreatedField('created_at', db_index=True)
    updated_at = AutoLastModifiedField('updated_at', db_index=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, IndexedTimeStampedModel):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        max_length=255,
    )
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
