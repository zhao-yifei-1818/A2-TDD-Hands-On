'''TDD flow practice'''
def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    if not any(c.islower() for c in pwd):
        return False
    return True
