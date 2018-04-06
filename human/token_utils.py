def get_token(card, test=False):
    """
    example_card = {
        "number": '4242424242424242',
        "exp_month": 12,
        "exp_year": 2019,
        "cvc": '123'
    }
    """
    if test:
        return 'tok_visa'
    else:
        return 'tok_visa'


