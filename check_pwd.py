'''TDD flow practice'''
def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    if not any(c.islower() for c in pwd):
        return False
    if not any(c.isupper() for c in pwd):
        return False
    if not any(c.isnumeric() for c in pwd):
        return False
    special_chars = "~`!@#$%^&*()_+-="
    if not any(c in special_chars for c in pwd):
        return False
    return True
