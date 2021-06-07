import hashlib
with open('top-10000-passwords.txt', 'r') as file1:
    dbPasswords = file1.readlines()
with open('known-salts.txt', 'r') as file2:
    f2 = file2.readlines()

def crack_sha1_hash(hash, use_salts=False):
    result = "PASSWORD NOT IN DATABASE"
    for password in dbPasswords:
        password = password.strip()
        if use_salts:
            for salt in f2:
                salt = salt.strip()
                guessed_hash1 = hashlib.sha1((salt+password).encode("utf-8")).hexdigest()
                guessed_hash2 = hashlib.sha1((password + salt).encode("utf-8")).hexdigest()
                if hash == guessed_hash1 or hash == guessed_hash2:
                    result = password
                    break
        else:
            bPassword = password.encode("utf-8")
            dbPassword = hashlib.sha1(bPassword).hexdigest()
            if dbPassword == hash:
                result = password
                break
    return result