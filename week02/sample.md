#### Run this code and see what happens ####

```python
dict = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in dict:
    print key + " " + dict[key]
```

What is this called?
How would you print just one key in the dictionary?

```python
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break
```

How is this different from a for loop?

Remember you can always go back to your old code/notes to see how to set up functions, loops, dictionaries, etc.

```python
def reverse(s): 
"""Return the sequence string in reverse order.""" 
    letters = list(s) 
    letters.reverse() 
    return ''.join(letters) 
    
print reverse('CCGGAAGAGCTTACTTAG') 
```
So what about reverse complement?
What is the reverse complement of CCGGAAGAGCTTACTTAG? (write it out, then code it. remember we have a tool called a dictionary)



