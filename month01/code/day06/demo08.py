"""
    集合set
        价值2：数学运算
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
# 1.	交集&：返回共同元素。
s3 = s1 & s2  # {2, 3}
# 2.	并集：返回不重复元素
s4 = s1 | s2  # {1, 2, 3, 4}
# 3.	补集-：返回只属于其中之一的元素
s5 = s1 - s2  # {1} 属于s1但不属于s2
s6 = s2 - s1  # {4}
# 补集^：返回不同的的元素
s7 = s1 ^ s2  # {1, 4}  等同于(s1-s2 | s2-s1)

# 4. 子集 <：判断一个集合的所有元素是否完全在另一个集合中
# 5.超集 >：判断一个集合是否具有另一个集合的所有元素
s8 = {2, 3}
# s8 子集  s1 超集
print(s8 < s1)  # True
print(s1 > s8)  # True