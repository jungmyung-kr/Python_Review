"""
chap06_Function
step02_module_func
"""

'''
모듈(module)
- 파이썬에서 제공하는 파일(*.py)
- 경로 : ~\anaconda3\lib
- 함수와 클래스 제공

모듈 함수
 -모듈에서 제공하는 함수
 -유형
  1) built-in 모듈 : 내장함수
  2) import 모듈 : 가져오기 모듈 
'''

# 1. built-in 모듈
# import builtins 
# 원래 모듈은 이렇게 임포트해서 사용해야하지만
# 빌트인의 경우 자주 사용하는 것들만 자체적으로 기본 모듈로 파이썬이 포함하고 있기 때문에
# 임포트 안하고 바로바로 사용가능
# ex) len(x) 

dataset = list(range(1,6))
print(dataset) # [1,2,3,4,5]

# built-in 모듈 제공 함수
sum(dataset) # 15
max(dataset) # 5
min(dataset) # 1
len(dataset) # 5

help(len)
# Help on built-in function len in module builtins: 
# 빌트-인 모듈이라고 알려줌.

# 2. import 모듈
# 방법1
import statistics 

dir(statistics) # 함수 or 클래스 
print('방법1 - 평균 =', statistics.mean(dataset)) # 방법1 - 평균 = 3

'''
mean                Arithmetic mean (average) of data.
fmean               Fast, floating point arithmetic mean.
geometric_mean      Geometric mean of data.
harmonic_mean       Harmonic mean of data.
median              Median (middle value) of data.
median_low          Low median of data.
median_high         High median of data.
median_grouped      Median, or 50th percentile, of grouped data.
mode                Mode (most common value) of data.
multimode           List of modes (most common values of data).
quantiles           Divide data into intervals with equal probability.
pvariance           Population variance of data.
variance            Sample variance of data.
pstdev              Population standard deviation of data.
stdev               Sample standard deviation of data.
'''

# 방법2
from statistics import mean, median, stdev # 방법2
print('방법2 - 평균 =', mean(dataset)) # 방법2 - 평균 = 3
median(dataset) # 3
stdev(dataset) # 1.5811388300841898