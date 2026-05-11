from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def _hash(password: str):
    hashed = password_hash.hash(
        password
    )
    
    return hashed


def _check_hash(password: str, hashed: str):
    matched = password_hash.verify(password=password, hash=hashed)
    
    return matched
    
