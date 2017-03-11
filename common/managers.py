# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, name):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            password=password,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user
