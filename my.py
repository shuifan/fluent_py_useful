import requests

url = "https://api.youku.com/oauth2/token.json"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_id\"\r\n\r\n64ab9b21e32f22cd\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"grant_type\"\r\n\r\nrefresh_token\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"refresh_token\"\r\n\r\ne9a14a61ba7762cd8fb0e3f105ddf23b\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    }

response = requests.request("POST", url, data=payload, headers=headers)

<<<<<<< HEAD
    def the_counter(*args):
        global i
        i += 1
        return func(*args)

    return the_counter


@clock
def my(seconds):
    time.sleep(seconds)


@functools.lru_cache()
# @clock
@counter
def febonaqie(n):
    if n < 2:
        return n
    return febonaqie(n - 2) + febonaqie(n - 1)

class test():
    def __init__(self, value):
        self.x = value

    def __call__(self, value):
        return self.x * value

if __name__ == '__main__':
    # t0 = time.time()
    # time.sleep(2)
    # t1 = time.time()
    # print(t1 - t0)
    # print(febonaqie(30))
    # print(i)
    a = test(4)
    print(a(4))
=======
print(response.text)
>>>>>>> 0eeb23ffee003319cba2956000a405c94566c369
