import re
def read_template (path) :
    try :
        with open ("../" + path, "r") as f:
            text = f.read()

        return text
    except FileNotFoundError:
        return "Please check of the path of your text file"






def find_between(s, first, last):
    try:
        regex = rf'{first}(.*?){last}'
        parts  = (re.findall(regex, s))
        return parts
    except ValueError:
        return -1
    
def parse_template (t) :
    regex = "\{(.+?)\}"
import re
def read_template (path) :
    try :
        with open ("../" + path, "r") as f:
            text = f.read()

        return text
    except  KeyError as err:
        return err




 
def find_between(s, first, last):
    try:
        regex = rf'{first}(.*?){last}'
        parts  = (re.findall(regex, s))
        return parts
    except ValueError:
        return -1
    
def parse_template (t) :
    regex = "\{(.+?)\}"
    for x in t:
        # res1 = t.replace(regex , "{}")
        x = re.sub(regex, "{}", t )

    res2 = find_between(t,"{", "}")
    my_tuple= (*res2,) 
    return x , my_tuple

def merge(blank , tuple) :

    blank = blank.format(*tuple)
    return blank


if __name__=="__main__" : 
    print("""
    Welcome to madlib game <3"
    ---------------------------
    In this game you will be asked to enter some words and these words will be in a funny article.
    """)
          
# reading = read_template("assets/dark_and_stormy_night_template.txt")
# path = "assets/dark_and_stormy_night_template.txt"
    t = read_template("assets/myText.txt")
    countOfWords = len(find_between(t , "{" , "}"))
    print("Now please Enter" ,countOfWords,"words")
    wordsList = []
    for i in range(countOfWords):
        i = input()
        wordsList.append(i)
    t = read_template("assets/myText.txt")
    path = "assets/dark_and_stormy_night_template.txt"

    str, x = parse_template(t)
    print("""
    Your article is generated ....
        Here is it : 
          """)


    print (merge(str , wordsList))
    completed_text = merge(str , wordsList)
    f = open("comp.txt", "a")
    f.write(completed_text)
    f.close()








 



