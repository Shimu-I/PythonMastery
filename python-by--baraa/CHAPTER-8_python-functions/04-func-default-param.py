# Building full clean name
def clean_name(first_name, last_name, country="n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)


clean_name(" MariA", "SmITH", "DE")
clean_name(" MariA", "SmITH")


print("*" * 30)
# RULE: parameter without a default follows parameter with a default\
# last parameter will only have the default value after this no parameter can have default or can have a default value

def clean_name(first_name, last_name="N/A", country="n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)


clean_name(" MariA", "SmITH", "DE")
clean_name(" MariA")

print("*" * 30)


