#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
HERE = os.path.dirname(__file__)

sys.path.append(HERE)
# sys.path.append(os.path.join(HERE, 'thirdparty'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

#pip install django django-suit django-filer django-helper
#Django
#south
#Pillow
#MySQL-python
#misaka
#django-suit
#django-attachments