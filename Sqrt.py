import time
# 步长法
def square_root_1():
    c = 10
    g = 0
    i = 0
    for j in range(0, c+1):
        if j * j > c:
            g = j - 1
            break

    # 缓存 g*g
    g_squared = g * g
    while abs(g_squared - c) > 0.0001:
        #对于一开始差距较大的时候,使用较大的步长进行逼近，后面逐步缩小
        if abs(g_squared - c) > 1:
            g += 0.25
        elif abs(g_squared - c) > 0.1:
            g += 0.0025
        elif abs(g_squared - c) > 0.001:
            g += 0.00025
        else:
            g += 0.000025
        g_squared = g * g  # 避免多次计算，只进行一次计算
        i += 1
        print(f"stride-approach {i}: g = {g:.5f}")
start = time.perf_counter()
square_root_1()
end = time.perf_counter()
print("stride-approach execution time: %f s \n" % (end - start))

# 二分法
def square_root_2():
    c = 10
    m_max = c
    m_min = 0
    g = (m_min + m_max) / 2
    i = 0
    g_squared = g * g
    while abs(g_squared - c) > 0.00000000001:
        if g_squared < c:
            m_min = g
        else:
            m_max = g
        g = (m_min + m_max) / 2
        g_squared = g * g  # 缓存 g*g
        i += 1
        print(f"dichotomy-approach {i}: {g:.13f}")

start = time.perf_counter()
square_root_2()
end = time.perf_counter()
print("dichotomy-approach execution time: %f s\n" % (end - start))

# 牛顿法
def square_root_3():
    c = 10
    g = c / 2
    i = 0
    g_squared = g * g
    while abs(g_squared - c) > 0.00000000001:
        g = (g + c / g) / 2
        g_squared = g * g  # 缓存 g*g
        i += 1
        print(f"Newton-approach {i}: {g:.13f}")

start = time.perf_counter()
square_root_3()
end = time.perf_counter()
print("Newton-approach execution time: %f s" % (end - start))
