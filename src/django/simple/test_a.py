import os
import time
from random import choice

import django  # noqa
from simple.models import Journal

django.setup()  # noqa


LEVEL_CHOICE = [10, 20, 30, 40, 50]
count = int(os.environ.get('ITERATIONS', '1000'))


start = now = time.time()
for i in range(count):
    Journal.objects.create(
        level=choice(LEVEL_CHOICE),
        text=f'Insert from A, item {i}'
    )
now = time.time()

print(f'Django, A: Rows/sec: {count / (now - start): 10.2f}')
