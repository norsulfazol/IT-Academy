with open("imperial guard.jpg", "rb") as donor:
    with open("imperial guard copy.jpg", "wb") as receiver:
        while True:
            b = donor.read(100)
            print(b)
            if b:
                receiver.write(b)
            else:
                break
        #receiver.write(donor.read())