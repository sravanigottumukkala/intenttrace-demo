def process_payment(payment_info):
    while True:
        try:
            return external_gateway.charge(payment_info)
        except TimeoutError:
            pass
