#--------------------------Section 1 Question 1 --------------------------------
set.seed(100)
clinic_time <- 420 # minutes 9Am-4Pm
entries <-c() # storing total entries of customers-1000 entries
waiting_list <- c() # storing no of customers waiting- 1000 entries
average_wait <-c() # storing average waiting time of customers -1000 entries
office_close <-c() # office closing time - 1000 entries
for(x in 1:1000)
{
entry_time <-rexp(100,rate = 0.1) # exponential distribution generation 
no_of_entry <- length(which(cumsum(entry_time)<=clinic_time)) # total number of customers/day
d_time <-c(0,0,0) # waiting of doctors
t = 0 # customer time at entry
count_wait <- c()
for(i in 1:no_of_entry)
{
  t<- t+entry_time[i]
  t1 <- runif(1,5,20) # doctor's uniform distribution
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
    k <- which(d_time==min(d_time)) # next available doctor
    temp <- d_time[k] - t # waiting time
    count_wait<-append(count_wait,temp) # appending waiting time to vector
    d_time[k] <- t+temp+t1
    
  }
}
avg <- sum(count_wait)/length(count_wait) # average waiting time
if(is.na(avg)) # if no customers waited then avg = N.A
{
  avg <- 0
}
entries<-append(entries,no_of_entry)
waiting_list <-append(waiting_list,length(count_wait))
average_wait <-append(average_wait,round(avg,3))
if(clinic_time>max(d_time)) # store should close atleast at 4pm
{
  cl<- clinic_time
}
else
{
  cl<- max(d_time)
}
office_close <- append(office_close,cl)
}

#------------------1(A)------------------------
cl<- office_close[1]
xy <-0
if(cl  >clinic_time)
{
  xy <- as.integer(cl - clinic_time) # calculating minutes after 4 pm
}
print(paste("The total patients that came to office are",entries[1]))
print(paste("Number of patients that waited for doctor are",waiting_list[1]))
print(paste("The average waiting time is:",round(average_wait[1],2),"minutes"))
print(paste("The office closes at",4,":",xy,"PM"))
#-----------------1(B)---------------------------

k1<- sum(entries)/length(entries)
k2<- sum(waiting_list)/length(waiting_list)
k3<- sum(office_close)/length(office_close)
k4<- sum(average_wait)/length(average_wait)
xy <-0
if(k3  > clinic_time)
{
  xy <- as.integer(k3 - clinic_time)
}
print(paste("The Median of total patients that came to office are",as.integer(k1)))
print(paste("Median of Number of patients that waited for doctor are",as.integer(k2)))
print(paste("The Median of average waiting time is:",round(k4,2),"minutes"))
print(paste("The office closes at",4,":0",xy,"PM"))

