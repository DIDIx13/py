+from PIL import Image
import pytesseract # sudo pip install pytesseract && sudo apt-get install tesseract-ocr
import requests
from StringIO import StringIO

#script to get, sort, and post the data

def solve(captcha):
    return pytesseract.image_to_string(Image.open(captcha))[::-1]

def postSolution():
    url = "https://www.hackthis.co.uk/levels/captcha/1"
    login = "https://www.hackthis.co.uk/?login"
    payload = {"username": "DIDIx13", "password": "Ilovedloser"}

    s = requests.Session() # Start a session
    s.post(login, data=payload) # Login
    response = s.get(url).text # Get problem data
    captcha = s.get("https://www.hackthis.co.uk/levels/extras/captcha1.php")
    captcha = Image.open(StringIO(captcha.content))
    captcha.save("captcha1.png")
    solution = solve("captcha1.png")
    payload = {"answer": solution}
    s.post(url, data=payload) # Post data
    response = s.get(url).text
    if ("Incomplete" in response):
        return "Fail"
    else:
        return "Sucessfully solved problem"

while postSolution() == "Fail":
    postSolution()
print "Done"
