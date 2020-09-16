import re

m = re.search(r'w.*a', 'sdasdqweasdafsasdqwasdasdas')
# 开始结束下标
print(m.span())

# 获取匹配的结果
print(m.group())

print(re.sub(r'\d', 'x', '22a1s2s2s2s2sw'))
