def domain_name(domain):
    if "//" in domain:
        res = domain.split("//")[1]
    else:
        res = domain
    res = res.split(".")
    if res[0] == "www":
        return res[1]
    else:
        return res[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
