def reverse(s):
    length = len(s)
    spaces = [' ']
    words = []
    i = 0 
    while i < length: 
        if s[i] not in spaces:
            word_start = 1
            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:1])

        i += 1
    return "".join(reversed(s))
print(reverse("This is the best"))

#####################################################

def py_reverse(s):
    return s.split()[::-1]
print(py_reverse('Hello, I am MyNameHere'))