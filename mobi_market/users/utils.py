from random import choices

def generate_verification_code():
    return "".join(choices("0123456789", k=4))