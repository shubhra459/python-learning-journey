with open ("studentss.txt","r")as file:
    for line in file:
        don = line.strip()
        don1 = don.split(",")
        print(f"studnet: {don1[0]} | course:{don1[1]} | age: {don1[2]}")