set.seed(200)
entry_time <-rexp(100,rate = 0.1)
no_of_entry <- length(which(cumsum(waiting_time)<=420))
entry_time
d_time <-c(0,0,0)
t = 0
count_wait <- c()
for(i in 1:no_of_entry)
{
  t<- t+entry_time[i]
  t1 <- runif(1,5,20)
  if(t>=d_time[1])
  {
    d_time[1] <- t1 + t
  }
  else if(t>=d_time[2])
  {
    d_time[2] <-t1 + t
  }
  else if(t >=d_time[3])
  {
    d_time[3] <- t1+t
  }
  else
  {
    k <- which(d_time==min(d_time))
    temp <- d_time[k] - t
    count_wait<-append(count_wait,temp)
    d_time[k] <- d_time[k]+temp+t1
    
  }
}

no_of_entry
length(count_wait)
sum(count_wait)/length(count_wait)
