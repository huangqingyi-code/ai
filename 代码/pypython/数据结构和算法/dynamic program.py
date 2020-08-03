# 动态规划题目特点：
# 1.计数：1.有多少种方式走到右下角；2.有多少种方法选出k个数使得和是sum
# 2.求最大值最小值：
# 3.求存在性：1.取石子游戏，先手能不能必胜；2.能不能选出k个数使得和为sum
# 动态规划解题步骤：
# 1.确定状态：最后一步和分解子问题
# 2.转移方程
# 3.初始条件和边界情况
# 4.  计算顺序
#
# 常见的动态规划类型：
# 坐标型  20%  f[i]表示ai为结尾的某种性质
# 序列型  20%  f[i]表示前a[0],a[1]...a[i-1]的某种性质
# 划分型  20%
# 区间型  15%
# 背包型  10%
# 最长序列型 5%
# 博弈型  5%
# 综合型  5%

class Solution():
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = costs
        for i in range(1, len(costs)):
            dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])
        return min(dp[-1])
    