from scourgify import normalize_address_record, NormalizeAddress

test = NormalizeAddress('2515 Boston St., Baltimor MD 21224').normalize()

print(test)