import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

# 生成n个随机数可用rv_continuous.rvs(size=n)或rv_discrete.rvs(size=n)，其中rv_continuous表示连续型的随机分布
# 均匀分布（uniform）、正态分布（norm）、贝塔分布（beta）等
# rv_discrete表示离散型的随机分布，如伯努利分布（bernoulli）、几何分布（geom）、泊松分布（poisson）等
rv_unif = stats.uniform.rvs(size=10)
print(rv_unif)
rv_beta = stats.beta.rvs(size=10, a=4, b=2)
print(rv_beta)

np.random.seed(seed=2015)
rv_beta = stats.beta.rvs(size=10, a=4, b=2)
print("method 1:")
print(rv_beta)

np.random.seed(seed=2015)
beta = stats.beta(a=4, b=2)
print("method 2:")
print(beta.rvs(size=10))

print("假设检验")
norm_dist = stats.norm(loc=0.5, scale=2)
n = 200
dat = norm_dist.rvs(size=n)
print(dat)
print("mean of data is: " + str(np.mean(dat)))
print("median of data is: " + str(np.median(dat)))
print("standard deviation of data is: " + str(np.std(dat)))

# 验证某个数据集是否符合某个分布
mu = np.mean(dat)
sigma = np.std(dat)
stat_val, p_val = stats.kstest(dat, 'norm', (mu, sigma))
print('KS-statistic D = %6.3f p-value = %6.4f' % (stat_val, p_val))

stat_val, p_val = stats.ttest_1samp(dat, 0)
print('One-sample t-statistic D = %6.3f, p-value = %6.4f' % (stat_val, p_val))

print("某个数值在一个分布中的分位")

g_dist = stats.gamma(a=2)
print("quantiles of 2, 4 and 5:")
print(g_dist.cdf([2, 4, 5]))
print("Values of 25%, 50% and 90%:")
print(g_dist.pdf([0.25, 0.5, 0.95]))

print("六阶原点矩")
print(stats.norm.moment(6, loc=0, scale=1))

print("使用describe函数对数据集统计信息进行描述")
norm_dist = stats.norm(loc=0, scale=1.8)
dat = norm_dist.rvs(size=100)
info = stats.describe(dat)
print("Data size is: " + str(info[0]))
print("Minimum value is: " + str(info[1][0]))
print("Maximum value is: " + str(info[1][1]))
print("Arithmetic mean is: " + str(info[2]))
print("Unbiased variance is: " + str(info[3]))
print("Biased skewness is: " + str(info[4]))
print("Biased kurtosis is: " + str(info[5]))

# 当我们知道一组数据服从某些分布的时候，可以调用fit函数来得到对应分布参数的极大似然估计
# （MLE, maximum-likelihood estimation）。以下代码示例了假设数据服从正态分布，用极大似然估计分布参数：
print("调用fit函数来得到对应分布参数的极大似然估计")
norm_dist = stats.norm(loc=0, scale=1.8)
dat = norm_dist.rvs(size=100)
mu, sigma = stats.norm.fit(dat)
print("MLE of data mean:" + str(mu))
print("MLE of data standard deviation:" + str(sigma))

# pearsonr和spearmanr可以计算Pearson和Spearman相关系数，这两个相关系数度量了两组数据的相互线性关联程度
# pearson 相关系数，
# |r|<=0.3为不存在线性相关
# 0.3<|r|<=0.5 低度线性相关
# 0.5<|r|<0=.8 显著线性相关
# |r|>0.8 高度线性相关
print("pearson * spearman")
norm_dist = stats.norm()
dat1 = norm_dist.rvs(size=100)
exp_dist = stats.expon()
dat2 = exp_dist.rvs(size=100)
cor, pval = stats.pearsonr(dat1, dat2)
print("Pearson correlation coefficient: " + str(cor))
cor, pval = stats.pearsonr(dat1, dat2)
print("Spearman's rank correlation coefficient: " + str(cor))

# 线性回归
print("线性回归")
x = stats.chi2.rvs(3, size=50)
print(x)

y = 2.5 + 1.2 * x + stats.norm.rvs(size=50, loc=0, scale=1.5)
print(y)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("斜率 Slope of fitted model is:", slope)
print("截距 Intercept of fitted model is:", intercept)
print("R-squared:", r_value ** 2)


