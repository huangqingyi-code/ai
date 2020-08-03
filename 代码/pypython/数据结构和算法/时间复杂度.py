#评判程序的优劣方法：
#消耗计算机资源和执行效率（无法直观/空间复杂度）
#计算执行耗时（受机器和环境影响，看不到源码的时候采用）
#时间复杂度（推荐）

#时间复杂度
# 1.评判规则：量化执行操作的步骤数量
# 2.常见时间复杂度
#   O(1)<O(logn)<(n)<o(nlogn)<o(n^2)<o(n^3)<o(2^n)<0(n!)<o(n^n)

#算法是为了解决实际问题
# 使用不同数据结构，时间复杂度不一样，数据结构是算法需要处理问题的载体

from timeit import Timer
def test01():
    return [i for i in range(1000)]
if __name__ == '__main__':
    timer = Timer('test01()','from __main__ import test01')
    t1 = timer.timeit(1000)
    print(t1)