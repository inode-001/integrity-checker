import hashlib

try:
    fileName = input("Enter the file to check its integrity : ")

    knownHash = str(input("Enter the known hash of the file : "))

    with open(fileName, "rb") as f:
        bytes = f.read()
        readableHash = hashlib.sha256(bytes).hexdigest()

    if knownHash == readableHash:
        print("\n\t>>> Status:OK File Verified")
    else:
        print("Status:Not Okay File Isn't Legit")
except FileNotFoundError:
    print("Error:\tEnsure you input the right file path ")
