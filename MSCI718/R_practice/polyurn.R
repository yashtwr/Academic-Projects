temp <- matrix(NA,nrow = 3,ncol = 3)
temp
temp[1,] <- c(2,8,11)

inerval <- cumsum(temp[1,])/sum(temp[1,])
draw <- runif(1)# selecting one random number between 0-1
draw
bin_assign <- c(inerval >draw)*1
bin_assign
k1 <- list(c(1:3),c(4:5),c(6:8))
k2 <-list(1,2,3)
k1[[1]]
coin <- c("H", "T")
p <- 0.5
prop_10000 <- c()
a <- sample(coin, size = 100, replace = T, prob = c(p, 1-p))
for(i in 1:10^4){
  a <- sample(coin, size = 100, replace = T, prob = c(p, 1-p))
  prop_10000[i] <- table(a)[1]/sum(table(a))
}
hist(prop_10000, breaks = 30, xlab = "Proportion of tosses with a head", main =
       "", freq = F)
a <- runif(100, 0, 10)
a
hist(a, breaks=25,prob = T)
library(MASS)
b <-fitdistr(a , densfun = "Normal")
b
curve(dnorm(x, b$estimate[1], b$estimate[2]), col="red", lwd=3, add=T)
