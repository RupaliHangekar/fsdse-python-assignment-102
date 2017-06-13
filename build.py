import re
def is_rotation(s1, s2):
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False
    if re.search(s1, s2+s2):
        return True
    else:
        return False

output=is_rotation("madam","madam1")
print output
