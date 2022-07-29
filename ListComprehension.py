pow2 = [2 ** x for x in range(10)]
print(pow2)
pow2 = []
for x in range(10):
   pow2.append(2 ** x)

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# Output: True
print('p' in my_list)

# Output: False
print('a' in my_list)

# Output: True
print('c' not in my_list)

for fruit in ['apple','banana','mango']:
    print("I like",fruit)