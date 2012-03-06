# -*- coding: utf-8 -*-
import csv
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from devotional.models import Devotional


class Command(BaseCommand):
    help = 'Imports the devotionals in the CSV file.'

    def handle(self, *args, **options):
        count = 0
        try:
            reader = csv.reader(open(settings.CSV_FILE_PATH, 'rb'))
        except:
            raise CommandError('CSV source file "%s" does not exist' \
                                % settings.CSV_FILE_PATH)

#        import ipdb; ipdb.set_trace()
        for index, row in enumerate(reader):
            dev = None
            if index > 0:
                month = int(row[1])
                day = int(row[2])

                if month > 12:
                    date = datetime.date(2012, month - 12, day)
                else:
                    date = datetime.date(2011, month, day)

                dev = Devotional.objects.create(body=row[3],
                                          title=row[0],
                                          date=date)
                count += 1

                self.stdout.write('Successfully created devotional "%s"\n' \
                                        % dev.id)

        self.stdout.write('-' * 80)
        self.stdout.write('\nSuccessfully created %s devotionals.\n' % count)
