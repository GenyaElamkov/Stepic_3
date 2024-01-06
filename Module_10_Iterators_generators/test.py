def is_valid_IP(strng):
    ip = strng.split(".")
    if len(ip) < 4 or len(ip) >= 5:
        return False
    for i, num in enumerate(ip):
        if not all([n.isdigit() for n in num]):
            return False
        if int(num) > 255:
            return False
        if num.startswith("0") and len(num) >= 2:
            return False
    return True



print("\nSTART")
assert is_valid_IP("12.255.56:.1") == False
assert is_valid_IP("") == False
assert is_valid_IP("abc.def.ghi.jkl") == False
assert is_valid_IP("123.456.789.0") == False
assert is_valid_IP("12.34.56") == False
assert is_valid_IP("12.34.56 .1") == False
assert is_valid_IP("12.34.56.-1") == False
assert is_valid_IP("123.045.067.089") == False
assert is_valid_IP("127.1.1.0") == True
assert is_valid_IP("0.0.0.0") == True
assert is_valid_IP("0.34.82.53") == True
assert is_valid_IP("192.168.1.300") == False
print("END\n")
