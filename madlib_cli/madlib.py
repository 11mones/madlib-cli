import re
def read_template (path) :
    with open (path, "r") as f:
        text = f.read()
        
    return text


t = read_template("../assets/dark_and_stormy_night_template.txt")

print(1111,read_template("../assets/dark_and_stormy_night_template.txt"))

def find_between(s, first, last):
    try:
        regex = rf'{first}(.*?){last}'
        parts  = (re.findall(regex, s))
        return parts
    except ValueError:
        return -1
    
def parse_template (t) :
    for x in t:
        res1 = t.replace("{Adjective}" , "{}")

    res2 = find_between(t,"{", "}")
    my_tuple= (*res2,) 
    return res1 , my_tuple



str, x = parse_template(t) 
print(str)
print(x)
print(parse_template(t))

# print(parse_template(t))






 


