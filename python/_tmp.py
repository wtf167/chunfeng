from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes, bytes_to_long
from libnum import generate_prime

# 读取data.txt中的数据
with open('/tmp/data.txt', 'rb') as f:
    lines = f.readlines()

# 将每一行转换为整数
x_values = [bytes_to_long(line.strip()) for line in lines]

# 使用中国剩余定理来解决这个问题
# 我们假设已经找到了所有对应的q值（实际上这一步可能非常困难）
# 但是为了演示，我们假设有这些q值
# 在实际情况下，你需要通过某种方式找到或猜测这些q值
# 这里我们只做演示，所以随机生成一些q值作为示例
# 注意：在真实场景下，你需要找到正确的q值
qs = [generate_prime(600) for _ in range(len(x_values))]

# 计算模数的乘积
M = 1
for q in qs:
    M *= q

# 初始化p的估计值
p_estimated = 0

# 应用中国剩余定理
for x, q in zip(x_values, qs):
    Mi = M // q
    ti = mod_inverse(Mi, q)
    p_estimated += (x % q) * Mi * ti

# 由于p_estimated可能比真实的p大很多倍，我们需要找到正确的p
# 通常我们会尝试不同的因子来缩小范围
# 但在这里，我们简单地尝试去除可能的填充
p_estimated %= M

# 尝试去除填充并打印可能的flag
while p_estimated > 999999:  # 假设flag不会太短
    possible_flag = long_to_bytes(p_estimated)
    if b'flag{' in possible_flag:  # 检查是否包含flag格式
        print(f"Possible flag: {possible_flag}")
        break
    # 如果没有找到，尝试减少p的大小
    p_estimated //= 8  # 假设填充是随机字节，通常不会是7位编码
else:
    print("Flag not found. You may need to refine the approach.")