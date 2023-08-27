import hashlib

def read_dictionary(file_path):
    with open(file_path,'r') as file:
        return [line.strip() for line in file]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def crack_password(target_hash,dictionary):
    for word in dictionary:
        hashed_word = hash_password(word)
        if hashed_word == target_hash:
            return word
    return None

if __name__== "__main__":
    target_hash = "100a50bef700d11fa44cd532ceeff7becdc5cc023ceb23eb6977bf89fb115f03"
    dictionary_file = "dict.txt"
    dictionary = read_dictionary(dictionary_file)
    cracked_password = crack_password(target_hash,dictionary)

    if cracked_password:
        print(f"Password cracked, The password is: {cracked_password}")
    else:
        print("Password Not Found")
