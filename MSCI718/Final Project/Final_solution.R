#Section 2 question 1
# loading the dataset 
library(foreign)
library(glmnet)
library(fastDummies)
#----------------------Q1(a)-------------------------------------------

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
print(summary(data2$state))
#31138
removal_index<-c()

data2$heat2<-as.character(data2$heat2)
data2$heat4<-as.character(data2$heat4)
for( i in 1:nrow(data2))
{
  temp_heat2<-data2[i,3]
  temp_heat4<-data2[i,4]
  if(is.na(temp_heat2) && is.na(temp_heat4))
  {
    #data2<-data2[-i,]
    removal_index<-append(removal_index,i)
  }
  else if(is.na(temp_heat2) && !is.na(temp_heat4))
  {
    data2[i,3]<-data2[i,4]
  }
}
data2<-data2[-removal_index,]
#4598 rows to be deleted
#converting the columns back to factors
data2$heat2<-factor(data2$heat2)
data2$heat4<-factor(data2$heat4)
print(paste("The number of N.A values in heat2 column are:",sum(is.na(data2$heat2))))
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
class(data3$heat2)
#Creating empty dataframe to store all the results
result_1b<-data.frame(state=state_names,b1=rep(NA,l),b2=rep(NA,l),
                    b3=rep(NA,l),b4=rep(NA,l),b5=rep(NA,l))
for(i in 1:nrow(result_1b))
{
  temp1<- result_1b[i,1] 
  #Q1.b.1
  democ_sp <-nrow(data3[data3$state==temp1 & data3$heat2 == "dem/lean dem",])
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
#displaying 5 values
head(result_1b,n=5)
#-----------------------------------Q1(c)---------------------------------------
Q1data2 <-read.csv("Q1Data2.csv",header = T)
# Q1.c.1
Q1data2_subset<-Q1data2[!(Q1data2$state=='Hawaii' | Q1data2$state =='District of Columbia' |
                     Q1data2$state == 'Alaska'),]
head(Q1data2_subset,n = 5)

#Q1.c.2
Q1data2_sub2<- subset(Q1data2_subset,select = c("state","vote_Obama_pct"))
head(Q1data2_sub2,n=5)
#---------------------------------Q1(d)-----------------------------------------
#Creating dummpy variable of the output and converting it to numeric type
#glm cannot run when output is a factor
y<-data3$heat2
k<-dummy_cols(y,remove_first_dummy = T)
y_numeric <-k$`.data_rep/lean rep`
                #Assumption 1 - Complete pooling
#Selecting only marital column to perform complete pooling on the states 
x_1<-model.matrix(heat2~ + .,data=data3[-4])
View(x_1)
penality_factor<- rep(1,ncol(x_1))
penality_factor[49] <- 0
model_complete_pooling<-glmnet(x_1,y,alpha = 1,lambda = 10^5,family = "binomial",
                               penalty.factor = penality_factor)
pred_prob_y<-predict(model_complete_pooling,type = "response",newx = x_1,s=0)
pred_y <-c()
for(i in 1:length(pred_prob_y))
{
  if(pred_prob_y[i]>=0.5)
  {
    pred_y[i] <- "dem/lean dem"
  }
  else
  {
    pred_y[i] <- "rep/lean rep"
  }
}
complete_pooling_df <-data.frame(state_name = data3$state,actual_output = y,predicted = pred_y,
                                 prediction_prob = pred_prob_y)
names(complete_pooling_df)[3]<-paste("predicted_output")
View(complete_pooling_df)
coef(model_complete_pooling)
#Calculating sum of squared error
k<-dummy_cols(pred_y,remove_first_dummy = T)
y_numeric_pred1 <-k$`.data_rep/lean rep`

sum(abs(y_numeric - y_numeric_pred1))/length(y_numeric)

              # Assumption 2 - No pooling 

# Including states column as well
x_2 <-model.matrix(heat2~0+state+marital+state*marital,data = data3[-4])
penality_factor<- rep(1,ncol(x_2))
penality_factor[49]<-0
model_no_pooling <-glmnet(x_2,y,lambda = 0,family = "binomial",alpha = 1)
pred_prob_y1<-predict(model_no_pooling,type = "response",newx = x_2,s=0)
pred_y1 <-c()
for(i in 1:length(pred_prob_y))
{
  if(pred_prob_y1[i]>=0.5)
  {
    pred_y1[i] <- "dem/lean dem"
  }
  else
  {
    pred_y1[i] <- "rep/lean rep"
  }
}
no_pooling_df <-data.frame(state_name = data3$state,actual_output = y,predicted = pred_y1,
                                 prediction_prob = pred_prob_y1)
View(no_pooling_df)
coef(model_no_pooling)
#Calculating sum of squared error
k<-dummy_cols(pred_y1,remove_first_dummy = T)

y_numeric_pred1 <-k$`.data_rep/lean rep`
sum(abs(y_numeric - y_numeric_pred1))/length(y_numeric)

        # Assumption 3 - Partial Pooling
penality_factor<- rep(1,ncol(x_2))
#making penality factor of marital column = 0, since it should not be included 
penality_factor[49] <- 0
set.seed(200)
model_min_lambda <- cv.glmnet(x_2,y,family = "binomial",type.measure = "class",
                              nfolds = 10)

min_lambda <- model_min_lambda$lambda.min
model_partial_pooling<- glmnet(x_2,y,family = "binomial",lambda = min_lambda,
                               penalty.factor = penality_factor)

pred_prob_y2<-predict(model_partial_pooling,type = "response",newx = x_2,
                      s=min_lambda)
pred_y2 <-c()
for(i in 1:length(pred_prob_y2))
{
  if(pred_prob_y2[i]>=0.5)
  {
    pred_y2[i] <- "dem/lean dem"
  }
  else
  {
    pred_y2[i] <- "rep/lean rep"
  }
}
partial_pooling_df <-data.frame(state_name = data3$state,actual_output = y,predicted = pred_y2,
                                prediction_prob = pred_prob_y2)
names(partial_pooling_df)[3]<-paste("predicted_output")
#Calculating sum of squared error
k<-dummy_cols(pred_y2,remove_first_dummy = T)
y_numeric_pred2 <-k$`.data_rep/lean rep`
sum(abs(y_numeric - y_numeric_pred2))/length(y_numeric)

coef(model_partial_pooling)

#-----------------------------Q1(E)-------------------------------------
pool_graph_df <-data.frame(state_name = state_names,obama_pct = Q1data2_subset$vote_Obama_pct,
                           actual_pct =result_1b$b1 ,
                           predicted_pct_no = rep(NA,l),
                           predicted_pct_partial = rep(NA,l))
for(i in 1:l)
{
  t6 <- pool_graph_df[i,1]
  t1<-nrow(partial_pooling_df[partial_pooling_df$state_name==t6 & partial_pooling_df$predicted_output == "dem/lean dem",])
  t2<-nrow(partial_pooling_df[partial_pooling_df$state_name==t6,])
  pool_graph_df[i,5]<- (t1/t2)*100
  t3 <-nrow(no_pooling_df[no_pooling_df$state_name==t6 & no_pooling_df$predicted == "dem/lean dem",])
  t4<- nrow(no_pooling_df[no_pooling_df$state_name==t6,])
  pool_graph_df[i,4] <- (t3/t4)*100
  
  }

head(pool_graph_df)
View(pool_graph_df)
plot(x = pool_graph_df$state_name,y = pool_graph_df$obama_pct,
     xlab = "State Names", ylab = "Percentage of democratic votes",
     type = "p",col="red",pch=25,cex=2)
library(ggplot2)
qplot(x = pool_graph_df$state_name,y = pool_graph_df$obama_pct,
      geom = "point", colou)
