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

What is the reverse complement of AAATTTCGCGCG?


```python
def revcomp(dna, reverse):
    bases = 'ATGCTACG'
    complement_dict = {bases[i]:bases[i+4] for i in range(4)} #what is this!?!?!?!?!?!
    if reverse:
        dna = reversed(dna)
    result = [complement_dict[base] for base in dna]
    return ''.join(result)
    

my_dna = 'AAATTTCGCGCG'
print(revcomp(my_dna, True))
print(revcomp(my_dna, False))
```


What about the reverse complement of GATTACAGTCAATCCAGGT?




