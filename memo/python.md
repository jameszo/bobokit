# Python

## Cookbook

```
a, _ = [1, 2]
first, *middle, last = [1, 2, 3, 4]
first, *_, last = [1, 2, 3, 4]

deque(maxlen=history)

heapq.nlargest(3, mylist, key=lambda s: s['price'])
heapq.heapify(mylist)
"""
当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很 合适的。
如果你仅仅想查找唯一的最小或最大(N=1)的元素的话，那么使用 min() 和 max() 函数会更快些。
如果 N 的大小和集合大小接近的时候，通常先排序这个 集合然后再使用切片操作会更快点(sorted(items)[:N] 或者是 sorted(items)[-N:] )。
需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势(如果 N 快接近集合大小了，那么使用排序操作会更好些)。
"""

s=slice(20, 30, 2)
for i in range(*s.indices(100)):
    print(i)

d=defaultdict(list)
d['a'].append(1)

OrderedDict

z = zip([1,2,3], [4,5,6])]
zip(*z)

a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()

{key:a[key] for key in a.keys() - {'z', 'a'}}

Counter

type(1)
isinstance(1, int)

bool([])
float(2)
int(2.5)

11//2
fractions.Fraction(1, 3)
math.pi

[n if n > 0 else 0 for n in mylist]
[n for n in mylist if n > 0]
(n for n in mylist if n > 0)
list(filter(is_int, values))
compress()

re.split(r'[;,\s]\s*', line)

with patch('sys.stdout', new=StringIO()) as fake_out:
```

## IO

```
fo = open(file_path, access_mode)
(path, file_name) = os.path.split(file_path);  
(shortname, extension) = os.path.splitext(file_name);  

os.remove(path)
```
