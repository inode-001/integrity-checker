import hashlib
try:
    file_to_check_hash = input("Input filename to check it's hash")
    available_hash = input("Enter the hash of file to verify : ")

    with open(file_to_check_hash,"rb") as f:
        bytes = f.read()
        file_inputed_hash = hashlib.sha256(bytes).hexdigest()

    if available_hash == file_inputed_hash:
       print(f"{file_to_check_hash}:OK")

    else:
        print("Incorrect sum ")
except FileNotFoundError:
    print(f"File {file_to_check_hash} not found")
