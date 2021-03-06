import os
import time
import imghdr
from django.core.management.base import BaseCommand
from django.conf import settings
from pics.models import *


class Command(BaseCommand):
    def handle(self, **options):
        files = []
        for folder in settings.PICS_FOLDER:
            for dirname, dirnames, filenames in os.walk(folder):
                for filename in filenames:
                    path=os.path.join(dirname, filename)
                    if imghdr.what(path):
                        p, created = Photo.objects.get_or_create(path=path)
                        if created:
                            print("create : {} {}".format(p.pk, path))
                            #time.sleep(0.1)
                        else:
                            print("exists : {} {}".format(p.pk, path))
