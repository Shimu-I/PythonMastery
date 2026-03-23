
print("*" * 30)
#---------------------------------------
# Transformation function
#---------------------------------------
# if wer are not returning any thing python is going to return NONE
def clean_name(name):
    cleaned = name.strip().lower()
    return cleaned

cln_name = clean_name("  MariA   ")
print(cln_name)



print("*" * 30)
#---------------------------------------
# return multiple value
#---------------------------------------
# if the value is empty, convert it to None, Otherwise, clean it

def clean_name(name):
    if not name:
        return None
    cleaned = name.strip().lower()
    return cleaned

cln_name = clean_name("  MariA   ")
print(cln_name)

cln_name = clean_name("")
print(cln_name)



print("*" * 30)
#---------------------------------------
# return multiple value seperated by comma,
#---------------------------------------
def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned # return tuple

cln_name = clean_name("  MariA   ")
print(cln_name)
lo_name, up_name =  clean_name(" MariA")
print(lo_name)
print(up_name)