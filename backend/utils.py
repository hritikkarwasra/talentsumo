from .models import UserDetail

import random


def create_user_invite_code():
    fixed_digits = 6
    code = random.randrange(111111, 999999, fixed_digits)
    while UserDetail.objects.filter(invite_code=code).count() != 0:
        code = random.randrange(111111, 999999, fixed_digits)
    else:
        return code
