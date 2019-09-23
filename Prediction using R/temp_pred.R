require(tseries) 
setwd("D:/")
d=read.csv("mahatemp.csv")
temp_ts <- ts(d[,3], frequency =12, start = 1901)
class(temp_ts)
start(temp_ts)
end(temp_ts)
plot.ts(temp_ts)
temp_ts
temp.hw <- HoltWinters(temp_ts, seasonal="additive")
temp.predict<-predict(temp.hw, n.ahead=10*12)
temp.predict
ts.plot(temp_ts, temp.predict, lty=1:2)