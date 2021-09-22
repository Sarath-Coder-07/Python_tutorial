"""The parameter weekday is True if it is a weekday, and the parameter
vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if
we sleep in.
function: sleep_in
output:
sleep_in(False, False) True
sleep_in(True, False) False
sleep_in(False, True) True"""


def sleep_in(weekday, vacation):

    if not weekday or vacation:
        return True
        #print(True)
    else:
        return False
        #print(False)


#sleep_in(False, False) #True
#sleep_in(True, False) #False
#sleep_in(False, True) #True

print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(True, True))


def sleep_in1(weekday, vacation):

    return not weekday or vacation

#sleep_in1(False, False) #True
#sleep_in1(True, False) #False
#sleep_in1(False, True) #True

print(sleep_in1(False, False))
print(sleep_in1(True, False))
print(sleep_in1(True, True))
############################################################

"""We have two monkeys, a and b, and the parameters a_smile and b_smile
indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is
smiling.
Return True if we are in trouble.
monkey_trouble(True, True) True
monkey_trouble(False, False) True
monkey_trouble(True, False) False"""


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        print(True)

    if not a_smile and not b_smile:
        print(True)

    return False


#monkey_trouble(True, True) #True
#monkey_trouble(False, False) #True
#monkey_trouble(True, False) #False

"""def function_that_prints():
    print ("I printed")

def function_that_returns():
    return True

f1 = function_that_prints()
function_that_returns()
#f2 = function_that_returns()
print ("Now let us see what the values of f1 and f2 are")
print (f1)
#print (f2)"""


##############################################################

"""Given a non-empty string and an int n, return a new string where the
char at index n has been removed.
The value of n will be a valid index of a char in the original string
(i.e. n will be in the range 0..len(str)-1 inclusive).
missing_char('kitten', 1) 'ktten'
missing_char('kitten', 0) 'itten'
missing_char('kitten', 4) 'kittn'
"""


def missing_char(strn, n):
    front = strn[:n]
    back = strn[n+1:]
    print(front )
    print(back)
    return front+back


print(missing_char("kitten", 2))


#######################################################################################


"""We have a loud talking parrot. The "hour" parameter is the current hour
time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or
after 20.
Return True if we are in trouble.
parrot_trouble(True, 6) True
parrot_trouble(True, 7) False
parrot_trouble(False, 6) False"""



def parrot_trouble(talking, hour):

    if talking and (hour < 7 or hour > 20):
            return True
    return False

def parrot_trouble1(talking, hour):
    return (talking and (hour < 7 or hour > 20))



print(parrot_trouble1(True, 7))


#########################################################################3

"""The web is built with HTML strings like "<i>Yay</i>" which draws Yay as
italic text.
In this example, the "i" tag makes <i> and </i> which surround the word
"Yay".
Given tag and word strings, create the HTML string with tags around the
word,
e.g. "<i>Yay</i>".
make_tags('i', 'Yay') '<i>Yay</i>'
make_tags('i', 'Hello') '<i>Hello</i>'
make_tags('cite', 'Yay') '<cite>Yay</cite>'"""


def make_tags(tag, str):
    #return <tag> + str + </tag>
    html_str="<{}>{}</{}>".format(tag,str,tag)
    return html_str
    #return "<" + tag + ">" + str + "</" + tag + ">"


print(make_tags("i","s"))

######################################################################

"""Given a string, return the string made of its first two chars, so the
String "Hello" yields "He".
If the string is shorter than length 2, return whatever there is, so
"X" yields "X", and the empty string "" yields the empty string "".
first_two('Hello') 'He'
first_two('abcdefg') 'ab'
first_two('ab') 'ab'"""


def first_two(str):
    return str[:2]


print(first_two("Hello"))

"""Given a string, return a version without the first and last char, so
"Hello" yields "ell".
The string length will be at least 2.
without_end('Hello') 'ell'
without_end('java') 'av'
without_end('coding') 'odin'"""


def without_end(str):
    if len(str)>2:
        return str[1:-1]
    return "The string length will be at least 2."

print(without_end("jav"))

############################################################################################

"""Given 2 int arrays, a and b, each length 3, return a new array length 2
containing their middle elements.
middle_way([1, 2, 3], [4, 5, 6]) [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) [2, 4]"""


def middle_way(a, b):
    a2 = len(a)//2
    b2 = len(b)//2
    print(a2)
    print(b2)
    return [a[a2], b[b2]]


print("middle_way" + str(middle_way([5, 2, 9, 2, 4], [1, 4, 2, 0, 5])))


################################################################################################################

"""Given an array of ints, return a new array length 2 containing the
first and last elements from the original array.
The original array will be length 1 or more.
make_ends([1, 2, 3]) [1, 3]
make_ends([1, 2, 3, 4]) [1, 4]
make_ends([7, 4, 6, 2]) [7, 2]"""


def make_ends(arr):
    a=arr[0]
    b=arr[-1]
    return [a,b]

print(make_ends([7, 4, 6, 2]))


##################################################################################3

"""Given an array of ints, return the sum of the first 2 elements in the
array.
If the array length is less than 2, just sum up the elements that
exist, returning 0 if the array is length 0.
sum2([1, 2, 3]) 3
sum2([1, 1]) 2
sum2([1, 1, 1, 1]) 2"""


def sum(ar):

    if len(ar) >= 2:
        print("array length " + str(len(ar)))
        return ar[0]+ar[1]
    if len(ar) == 1:
        print("array length " + str(len(ar)))
        return ar[0]
    else:
        return 0


print(sum([1]))
