import re

print(re.search(r"A.*a", "Argentina"))

print(re.search(r"^A.*a$", "Azernaijan"))

print(re.search(r"^A.*a$", "Australia"))

"""palabra = (input ("ingresa una oracion: "))
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, palabra))"""


def check_sentence(text):
    result = re.search(r"^[A-Z][A-Za-z\s]+[\.!\?]$", text)
    return result != None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True


def check_web_address(text):
    pattern = r".*\.[a-zA-Z]*$"
    result = re.search(pattern, text)
    return result != None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True


def check_time(text):
    pattern = (
        r"^[1-12]+[\:]+[00-59\s]+[am-pmAM-PM]*$"  # [1-12]*:[0123456789][ ]?[am|pm$]
    )
    result = re.search(pattern, text)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False
