from urllib.parse import urlencode
from urllib.request import Request, urlopen

def send_notification(url):
    post_fields = {
        'k':'xxxxxxxxxxxxxxxxxx',
        't':'New PDF found!',
        'd':'a',
        'm':'A new PDF was found.',
        'u':url
    }
    
    ps = 'https://www.pushsafer.com/api' 
    request = Request(ps, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
