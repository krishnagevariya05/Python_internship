# from collections import namedtuple
#
# a = namedtuple('Courses','name, Technology')
# s=a('data science','python')
# print(s)
# s=a._make(['Artificial intelligent','python'])
# print(s)

# from collections import  deque
# a=['K','R','I','S','H','N','A']
# d=deque(a);
# print(d)
# d.append('Gevariya')
# print(d)
# d.pop();
# print(d)
# d.appendleft('Gevariya')
# print(d)
# d.popleft()
# print(d)

# from  collections import ChainMap
#
# a={1:'DS',2:'python'}
# b={3:'ML',4:'AI'}
# a1=ChainMap(a,b)
# print(a1)

from collections import Counter

a=[1,2,3,2,3,4,4,5,5,5,2,4]
c=Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub={2:1, 5:1}
print(c.subtract(sub))
print(c.most_common())

# from collections import OrderedDict
#
# d=OrderedDict()
# d[1]='e'
# d[2]='d'
# d[3]='u'
# d[4]='r'
# d[5]='e'
# d[6]='k'
# d[7]='a'
# print(d)
# print(d.keys())
# print(d.items())
# d[3]='w'
# print(d)



# from collections import defaultdict
# d=defaultdict(int)
# d[1]='python'
# d[2]='C++'
# print(d[3])
"""
a={1:'python',2:'C++'}
print(a[3])
"""


