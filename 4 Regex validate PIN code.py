# My # Best
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

s = "1234"
print(f"{s} --> {validate_pin(s)}")
s = "12345"
print(f"{s} --> {validate_pin(s)}")
s = "a234"
print(f"{s} --> {validate_pin(s)}")