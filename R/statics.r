# σ已知，关于μ 的检验（Z 检验）

#例 3,某车间用一台包装机包装糖果。包得的袋装糖重是一个随机变量，
#它服从正态分布。当机器正常时，其均值为 0.5 公斤，标准差为 0.015 公斤。
#某日开工后为检验 包装机是否正常，随机地抽取它所包装的糖 9 袋，称得净重为（公斤）： 

library(BSDA)

data <- c(0.497,0.506,0.518,0.524,0.498,0.511,0.520,0.515,0.512)

z.test(data,mu=0.5,sigma.x = 0.015)

# alternative hypothesis: true mean is not equal to 0.5 真均值不为0.5

# p=0.0248，说明在 0.05 的水平下，可拒绝原假设，即认为这天包装机 工作不正常

# 若a<p 则在显著水平a下接受 H0



#σ未知，关于μ 的检验（t检验）
#例 4,某种电子元件的寿命 x(以小时计)服从正态分布, 2 , σ μ均未知.
#现得 16 只元件的寿命如下:

data <- c(159,280,101,212,224,379,179,264, 222,362,168,250,149,260,485,170)

t.test(x=data,mu=225,alternative="greater")

print(qt(0.95,length((data)-1),lower.tail = FALSE))

# 两个正态总体均值差的检验（t检验）

#在平炉上进行一项试验以确定改变操作方法的建议是否会增加钢的得率,
#试验是在同一平炉上进行的。每炼一炉钢时除操作方法外,其它条件都可能做到相同。
#先用标准方法炼一炉,然后用建议的新方法炼一炉,以后交换进行,各炼了 10 炉,其得率分别为

standardMethod <- c(78.1,72.4,76.2,74.3,77.4,78.4,76.0,75.6,76.7,77.3)
improvedMehtod <- c(79.1,81.0,77.3,79.1,80.0,79.1,79.1,77.3,80.2,82.1)

t.test(x=standardMethod,y=improvedMehtod,alternative="less",var.equal=TRUE)

#https://blog.csdn.net/Hellolijunshy/article/details/80024683