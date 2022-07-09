def int32_to_ip(x):
    x = bin(x)[2:].rjust(32, "0")
    res = f"{int(x[:8], 2)}.{int(x[8:16], 2)}.{int(x[16:24], 2)}.{int(x[24:], 2)}"
    return res


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(32) == "0.0.0.32"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(0) == "0.0.0.0"
