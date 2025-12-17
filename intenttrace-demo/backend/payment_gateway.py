def process_payment(payment_info):
    retries = 0
    while retries < 2:
        try:
            return external_gateway.charge(payment_info)
        except TimeoutError:
            retries += 1
    raise PaymentFailed("Payment service unavailable")
