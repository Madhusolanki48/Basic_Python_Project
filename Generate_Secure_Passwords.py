"""
fixed length, At least 12 characters long is recommended, 8 at the minimum. The 
combination of both upper- and lower-case letters, numbers, and symbols. Random enough that 
they do not contain any predictable sequence
"""
import random
import string
Final=''
len=random.randint(8,12)
Digits=string.digits
Lower=string.ascii_lowercase
Upper=string.ascii_uppercase
Punc=string.punctuation
Final=Digits+Lower+Upper+Punc
k=len-4
p=random.choices(Final,k=k)
p.append(random.choice(Digits))
p.append(random.choice(Lower))
p.append(random.choice(Upper))
p.append(random.choice(Punc))
random.shuffle(p)
print("PASSWORD =",''.join(p))
