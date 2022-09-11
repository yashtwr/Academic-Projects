

#--------------------------Section 1 Question 1 --------------------------------
# loading the dataset 
library(foreign)
library(fastDummies)
library(glmnet)
library(ggplot2)
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


#----------------------------Section 2 -----------------------------------------

#-------------------------------Q1(a)-------------------------------------------
#1.a.1
data_read<- read.dta("Q1Data1.dta")
#selecting 4 columns from the dataset
data1<-data.frame(state=data_read$state,marital=data_read$marital,
                  heat2 = data_read$heat2, heat4 = data_read$heat4)
#will be working on these 4 coulumns as described in S2.Q.1.a.1
#nrow(data1[!is.na(data1$heat4),])
data2<- data1[!(data1$state=='hawaii' | data1$state =='washington dc' |
                  data1$state == 'alaska'),]
data2$state<-droplevels(data2$state)
#removed the following states as described in the question 

#S2.Q1.a.2
removal_index<-c() # storing indices that are to be removed 
data2$heat2<-as.character(data2$heat2) #changing from factor to character
data2$heat4<-as.character(data2$heat4)
for( i in 1:nrow(data2))
{
  temp_heat2<-data2[i,3]
  temp_heat4<-data2[i,4]
  if(is.na(temp_heat2) && is.na(temp_heat4)) # checking if both are na
  {
    #data2<-data2[-i,]
    removal_index<-append(removal_index,i)
  }
  else if(is.na(temp_heat2) && !is.na(temp_heat4)) # checking if heat2 is na
  {
    data2[i,3]<-data2[i,4] # replacing heat 2 value with heat4
  }
}
data2<-data2[-removal_index,] #removing Na of heat 2
#4598 rows to be deleted
#converting the columns back to factors
data2$heat2<-factor(data2$heat2)
data2$heat4<-factor(data2$heat4)
#Q1.1.3 implementation
data3<-subset(data2,data2$heat2=="dem/lean dem" | data2$heat2 == "rep/lean rep") 
data3$heat2<-droplevels(data3$heat2)
#Q1.1.4 implementation
data3$marital<-as.character(data3$marital)
removal_index1<-c()
for( i in 1:nrow(data3))
{
  if(is.na(data3[i,2]))
  {
    
    removal_index1<-append(removal_index1,i)
  }
  else if(data3[i,2] != "married")
  {
    data3[i,2] <- "other"
  }
}
data3<-data3[-removal_index1,]
data3$marital<-factor(data3$marital)
summary(data3$marital)
# marital column updated 13225 married,9042 others and 1447 N.A values removed

#-------------------------------Q1(b)-----------------------------------
state_names <-sort(unique(data3$state))
l<-length(state_names)

#Creating empty dataframe to store all the results
result_1b<-data.frame(state=state_names,b1=rep(NA,l),b2=rep(NA,l),
                      b3=rep(NA,l),b4=rep(NA,l),b5=rep(NA,l))
for(i in 1:nrow(result_1b))
{
  temp1<- result_1b[i,1] 
  #Q1.b.1
  democ_sp <-nrow(data3[data3$state==temp1 & data3$heat2 == "dem/lean dem",]) #selecting democratic voters/state
  no_of_candidates_state <- nrow(data3[data3$state==temp1,])
  result_1b[i,2]<-(democ_sp/no_of_candidates_state)*100
  #Q1.b.2
  married_people <- nrow(data3[data3$state==temp1 & data3$marital == "married",])
  result_1b[i,3] <- (married_people/no_of_candidates_state)*100
  #Q1.b.3
  married_democratic <- nrow(data3[data3$state==temp1 & data3$marital == "married"
                                   & data3$heat2 == "dem/lean dem",])
  result_1b[i,4] <- (married_democratic/married_people)*100
  #Q1.b.4
  non_married_democratic <-nrow(data3[data3$state==temp1 & data3$marital == "other"
                                      & data3$heat2 == "dem/lean dem",])
  result_1b[i,5] <- (non_married_democratic/(no_of_candidates_state-married_people))*100
  #Q1.b.5
  result_1b[i,6] <- result_1b[i,4] - result_1b[i,5]
}
View(result_1b)
#displaying 5 values
head(result_1b,n=5)
#-----------------------------------Q1(c)---------------------------------------
Q1data2 <-read.csv("Q1Data2.csv",header = T)
# Q1.c.1
Q1data2_subset<-Q1data2[!(Q1data2$state=='Hawaii' | Q1data2$state =='District of Columbia' |
                            Q1data2$state == 'Alaska'),] # removing the selected states

#Q1.c.2
Q1data2_sub2<- subset(Q1data2_subset,select = c("state","vote_Obama_pct"))
View(Q1data2_sub2)
head(Q1data2_sub2,n=5)
#---------------------------------Q1(d)-----------------------------------------
#Creating dummpy variable of the output and converting it to numeric type
#glm cannot run when output is a factor
y<-data3$heat2 # output
k<-dummy_cols(y,remove_first_dummy = T) # for accuracy calculation
y_numeric <-k$`.data_rep/lean rep`#for accuracy calculation 

                      #Assumption 1 - Complete pooling
#Selecting only marital column to perform complete pooling on the states 
x_1<-model.matrix(heat2~0+marital+state+marital*state,data=data3[-4]) # input to the model
penality_factor<- rep(1,ncol(x_1))
penality_factor[1] <- 0 # removing penality for married:married column
penality_factor[2] <- 0 # removing penality for married:other column
model_complete_pooling<-glmnet(x_1,y,alpha = 1,lambda = 10^5,family = "binomial",
                               penalty.factor = penality_factor)
coef(model_complete_pooling)
pred_prob_y<-predict(model_complete_pooling,type = "response",newx = x_1,s=0)
pred_y<- predict(model_complete_pooling,type = "class",newx = x_1,s=0)
complete_pooling_df <-data.frame(state_name = data3$state,actual_output = y,predicted = pred_y,
                                 prediction_prob = pred_prob_y)
names(complete_pooling_df)[3]<-paste("predicted_output")
names(complete_pooling_df)[4]<-paste("predicted_prob")
(model_complete_pooling)
#Calculating accuracy
k<-dummy_cols(pred_y,remove_first_dummy = T)
y_numeric_pred1 <-k$`s1_rep/lean rep`

sum(abs(y_numeric - y_numeric_pred1))/length(y_numeric) #accuracy

                        # Assumption 2 - No pooling 

# Including states column as well
x_2 <-model.matrix(heat2~0+marital+state+state*marital,data = data3[-4])

model_no_pooling <-glmnet(x_2,y,lambda = 0,family = "binomial",alpha = 1)
pred_prob_y1<-predict(model_no_pooling,type = "response",newx = x_2,s=0)
pred_y1 <- predict(model_no_pooling,type = "class",newx = x_2,s=0)
no_pooling_df <-data.frame(state_name = data3$state,actual_output = y,predicted = pred_y1,
                           prediction_prob = pred_prob_y1,marital=data3$marital)
names(no_pooling_df)[3]<-paste("predicted_output")
names(no_pooling_df)[4]<-paste("predicted_prob")
coef(model_no_pooling)
#Calculating sum of squared error
k<-dummy_cols(pred_y1,remove_first_dummy = T)

y_numeric_pred1 <-k$`s1_rep/lean rep`
sum(abs(y_numeric - y_numeric_pred1))/length(y_numeric) #accuracy
model_no_pooling
                  # Assumption 3 - Partial Pooling
penality_factor<- rep(1,ncol(x_2))
#making penality factor of marital column = 0, since it should not be included 
penality_factor[1] <- 0
penality_factor[2] <-0
set.seed(200)
model_min_lambda <- cv.glmnet(x_2,y,family = "binomial",type.measure = "class",
                              nfolds = 10,penality.factor=penality_factor)

min_lambda <- model_min_lambda$lambda.min
model_partial_pooling<- glmnet(x_2,y,family = "binomial",lambda = min_lambda)

pred_prob_y2<-predict(model_partial_pooling,type = "response",newx = x_2,
                      s=min_lambda)
pred_y2 <-predict(model_partial_pooling,type = "class",newx = x_2,
                  s=min_lambda)

partial_pooling_df <-data.frame(state_name = data3$state,actual_output = y,predicted = pred_y2,
                                prediction_prob = pred_prob_y2,marital=data3$marital)
names(partial_pooling_df)[3]<-paste("predicted_output")
names(partial_pooling_df)[4]<-paste("predicted_prob")
#Calculating sum of squared error
k<-dummy_cols(pred_y2,remove_first_dummy = T)
y_numeric_pred2 <-k$`s1_rep/lean rep`
sum(abs(y_numeric - y_numeric_pred2))/length(y_numeric)

model_partial_pooling

#-----------------------------Q1(E)-------------------------------------
pool_graph_df <-data.frame(state_name = state_names,obama_pct = Q1data2_subset$vote_Obama_pct,
                           actual_pct =result_1b$b1 ,
                           predicted_pct_no = rep(NA,l),
                           predicted_pct_partial = rep(NA,l),
                           predict_nopool_gap = rep(NA,l),
                            predict_partial_gap =rep(NA,l),
                           actual_gap = rep(NA,l)) # frame for graph
for(i in 1:l)
{
  t6 <- pool_graph_df[i,1] # state name
  t1<-nrow(partial_pooling_df[partial_pooling_df$state_name==t6 & partial_pooling_df$predicted_output == "dem/lean dem",])
  t2<-nrow(partial_pooling_df[partial_pooling_df$state_name==t6,])
  pool_graph_df[i,5]<- (t1/t2)*100 # partial predicted democratic voters /state
  t3 <-nrow(no_pooling_df[no_pooling_df$state_name==t6 & no_pooling_df$predicted_output == "dem/lean dem",])
  t4<- nrow(no_pooling_df[no_pooling_df$state_name==t6,])
  pool_graph_df[i,4] <- (t3/t4)*100 # no pool democratic voters/state
  t5<- nrow(partial_pooling_df[partial_pooling_df$state_name==t6 & 
                                 partial_pooling_df$predicted_output == "dem/lean dem" &
                                 partial_pooling_df$marital=="married",])
  t7<-nrow(partial_pooling_df[partial_pooling_df$state_name==t6 & 
                                partial_pooling_df$predicted_output == "dem/lean dem" &
                                partial_pooling_df$marital=="other",])
  pool_graph_df[i,7] <- abs(t5-t7)*100/t2 # partial maritalgap/state 
  t8 <- nrow(no_pooling_df[no_pooling_df$state_name==t6 & 
                                  no_pooling_df$predicted_output == "dem/lean dem" &
                                  partial_pooling_df$marital=="married",])
  t9 <- nrow(no_pooling_df[no_pooling_df$state_name==t6 & 
                             no_pooling_df$predicted_output == "dem/lean dem" &
                             partial_pooling_df$marital=="other",])
  pool_graph_df[i,6]<- abs(t8-t9)*100/t2 # no pool marital gap/state
  t10 <- nrow(data3[data3$state==t6 & 
                              data3$heat2 == "dem/lean dem" &
                              data3$marital=="married",])
  t11 <- nrow(data3[data3$state==t6 & 
                      data3$heat2 == "dem/lean dem" &
                      data3$marital=="other",])
  pool_graph_df[i,8] <- abs(t10-t11)*100/t2 # actual marital gap/state
  
}

ggplot(data = pool_graph_df)+
  geom_point(aes(x=state_name,y=actual_pct),shape = 25,color=1:48) +
  geom_point(aes(x=state_name,y=predicted_pct_partial),shape = 18,color=1:48)+
  geom_point(aes(x=state_name,y=obama_pct),shape = 10,color=1:48) +
  labs(x= "State Names", y = "Vote percentage",title = "Partial Pool Model Analysis for Democratic Party Votes") +
  theme_bw() +
  theme(axis.text.x = element_text(colour = "grey20", size = 9, angle = 90, hjust = 0.5, vjust = 0.5),
        axis.text.y = element_text(colour = "grey20", size = 12),
        axis.title = element_text(size=12),
        strip.text = element_text(face = "italic"),
        text = element_text(size = 16))

#-------------------------Q1(F)------------------------------------------------
ggplot(data = pool_graph_df)+
  geom_point(aes(x=state_name,y=predict_partial_gap),shape = 25,color=1:48) +#triangle shape
  geom_point(aes(x=state_name,y=actual_gap),shape = 18,color=1:48)+ #Diamond shape
  geom_point(aes(x=state_name,y=obama_pct),shape = 1,color=1:48) + #round shape
  labs(x= "State Names", y = "marital gap percentages",title = "Partial Pool Model Analysis for Marital Gap") +
  theme_bw() +
  theme(axis.text.x = element_text(colour = "grey20", size = 9, angle = 90, hjust = 0.5, vjust = 0.5),
        axis.text.y = element_text(colour = "grey20", size = 12),
        axis.title = element_text(size=12),
        strip.text = element_text(face = "italic"),
        text = element_text(size = 16))
#--------------------Q1(G)--------------------------------------
#Marital gap for assumption 2
#All the computation done in part E
ggplot(data = pool_graph_df)+
  geom_point(aes(x=state_name,y=actual_pct),shape = 25,color=1:48) + #triangle
  geom_point(aes(x=state_name,y=predicted_pct_no),shape = 18,color=1:48)+#diamond
  geom_point(aes(x=state_name,y=obama_pct),shape = 10,color=1:48) +#round
  labs(x= "State Names", y = "Vote percentage",title = "Partial Pool Model Analysis for Democratic Party Votes") +
  theme_bw() +
  theme(axis.text.x = element_text(colour = "grey20", size = 9, angle = 90, hjust = 0.5, vjust = 0.5),
        axis.text.y = element_text(colour = "grey20", size = 12),
        strip.text = element_text(face = "italic"),
        axis.title = element_text(size=12),
        text = element_text(size = 16))

#Marital Gap for assumption 2

ggplot(data = pool_graph_df)+
  geom_point(aes(x=state_name,y=predict_nopool_gap),shape = 25,color=1:48) +#triangle shape
  geom_point(aes(x=state_name,y=actual_gap),shape = 18,color=1:48)+ #Diamond shape
  geom_point(aes(x=state_name,y=obama_pct),shape = 1,color=1:48) + #round shape
  labs(x= "State Names", y = "marital gap percentages")+
  ggtitle("Partial Pool Model Analysis for Marital Gap")+
  theme_bw() +
  theme(axis.text.x = element_text(colour = "grey20", size = 9, angle = 90, hjust = 0.5, vjust = 0.5),
        axis.text.y = element_text(colour = "grey20", size = 12),
        strip.text = element_text(face = "italic"),
        axis.title = element_text(size=12),
        text = element_text(size = 16))
View(pool_graph_df)
