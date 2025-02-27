hex1 = 0xc4115

hex2 = 0x4cf8

one_xor_two = hex1 ^ hex2

results_hex = hex(one_xor_two)

print("The flag to submit is CTFlearn{" + str(results_hex) + "}")
