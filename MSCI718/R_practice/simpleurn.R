rm(list = ls(all.names = TRUE))
simple_urn<-c(rep(1,2),rep(2,3),rep(3,3))
n_trails = 10^4
without_replacement <- matrix(NA,nrow = n_trails,ncol = length(simple_urn))
for (i in 1:n_trails)
{
  without_replacement[i,] = sample(simple_urn,replace = FALSE,)
}
success_function<- function(x)
{
  start_indices = which(x == 1)
  success <-c()
  for (i in 1:length(start_indices))
    {
      second_result = x[start_indices[i]+1] == 2
      third_result = x[start_indices[i]+2] == 3
      success[i] = sum(second_result+third_result)
  }
  total_success <- sum(success == 2, na.rm = T)
  return (total_success)
}
solution <- apply(without_replacement,1,function (x) success_function(x))
sum(solution >=1)

