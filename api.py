from firebase import firebase

firebase=firebase.FirebaseApplication("https://lifesaver-18f28.firebaseio.com/")
while True:
    res = firebase.get('/zoom', None)
    f= open(r"C:\Users\PIYUSH\Desktop\fir.txt","w+")

    f.write(str(res))

    f=open(r"C:\Users\PIYUSH\Desktop\fir.txt", "r")
    contents =f.read()
    print(contents)
