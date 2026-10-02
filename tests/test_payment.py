from src.payment import calculate_payment

def test_payment():
    assert calculate_payment(10, 2) == 20
