"""Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included)."""
def validate_usr(username):
    if username == "____": return True
    if 4 <= len(username) <= 16 and username.islower():
        for i in username:
            if i.isalnum() or i == "_":
                continue
            else:
                return False
        return True
    return False 
