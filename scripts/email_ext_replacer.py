"""
Author @Hakan Dabanli
27.05.2019
"""

email = input("E-mail adresinizi giriniz: ")
extension = input("Değiştirmek istediğiniz e-mail uzantısını giriniz: ")

def replaceExtension():
    at_char = '@'
    global newmail
    for x in email:
        if x == at_char:
            ext = email.split(at_char, 2)
            ext[1] = extension
            newmail = ext[0] + at_char + ext[1]
    

replaceExtension()
print("Eski mail: {0} \nYeni mail: {1}".format(email, newmail))