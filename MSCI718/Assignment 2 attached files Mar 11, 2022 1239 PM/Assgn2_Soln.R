set.seed(4)
#generating random inputs as specified in the question 1
x <- rnorm(n = 50,mean = 0,sd = 2)
# generating random out as specified in the question 1
y <- rnorm(n=50, mean = 2+1.5*x,sd=10)
lm_fit <- lm(y~x)
# Q1 a
plot(x,y)
abline(lm_fit)
#Q1 b
summary(lm_fit)
# The P value of B1 = 0.0056<0.05.
# thus the null hupothesis can be rejected 
# Q1 C
set.seed(200)
x <- rnorm(n = 50,mean = 0,sd = 2)
y <- rnorm(n=50, mean = 2+1.5*x,sd=10)
lm_fit <- lm(y~x)
plot(x,y)
abline(lm_fit)
summary(lm_fit)
# the p value of B1 = 0.28
dataset_read <- read.csv("voting_data.csv")
head(dataset_read)
y <- dataset_read$dem_vote
x1 <- dataset_read$marital_id
x2 <- dataset_read$state_id
bn_fit <- glm(y~x1+x2,data = dataset_read[-1],family = "binomial")
summary(bn_fit)
#Question 3
#R - total number of balls from bag A
#kbb - total black balls in Bag B
#kwb- total white balls in Bag B
# this log likelihood function is multipliction of
#combinations of the 2 types of balls
likelihood_func<- function(n1,n2,W,B)
{
  return(choose(n1,W)*choose(n2,B))
}
result_generator<- function(N,kwb,kbb,R,sample_w)
{
  S <- c()
  # Converting the input sample to numbers
  for(i in 1:length(sample_w))
  {
    if(sample_w[i]=='W')
    {
      S[i] <- 1
    }
    else
    {
      S[i] <- 0
    }
  }
  #creating an empty grid 
  result_like1 <- matrix(NA,nrow = kwb + R,ncol = kbb+R)
  #total white balls in the input sequence
  white_pick <- sum(S)
  #total black balls in the input sequence
  black_pick <- length(S) - sum(S)
  for(i in 1:kwb+R)
  {
    for(j in 1:kbb+R)
    {
      # grid method to find MLE for Bag B
      if(i+j <= kwb+kbb+R)
      {
        result_like1[i,j] <- likelihood_func(i,j,white_pick,black_pick)
      }
      
    }
  }
  temp <- max(result_like1,na.rm=T)
  #Max likelihood calculated for bag B
  #white and black balls in Bag B are calculated 
  adr_res<-which(result_like1==temp,arr.ind = T)
  #white balls in R sample
  R_w <- adr_res[1,1] - kwb
  #black balls in R sample
  R_b <-adr_res[1,2] - kbb
  # Calculating maximum likelihood for Bag A
  final_likelihood <- c(rep(NA,21))
  for (i in 0:20)
  {
    final_likelihood[i] <-likelihood_func(i,N-i,R_w,R_b) 
  }
  wt_lk <- max(final_likelihood,na.rm = T)
  white_balls <- which(final_likelihood == wt_lk) -1
  black_balls <- N-white_balls
  print(paste("The white balls in Bag A are:",white_balls))
  print(paste("The Black balls in Bag A are:",black_balls))
}
# part B
result_generator(20,10,10,5, c('W','B','B','W','B','W'))


