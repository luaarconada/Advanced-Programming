library(Rcpp)


################### Exercise 1 ###########################
cppFunction('
double my_mean (NumericVector x){
  int n;
  n = x.size();
  double total;
  total = 0;
  int i;
  double mean;
  mean = 0;
  for (i=0; i<n; ++i){
    total = total + x[i];
  }
  mean = total/n;
  return mean;
}')

my_mean(c(1,2,3))


################### Exercise 2 ###########################
cppFunction('
NumericVector my_cum_sum(NumericVector x){
  int n= x.size();
  NumericVector out(n);
  out[0]=x[0];
  int i;
  for (i=0;i<n;++i){
    out[i]=out[i-1]+x[i];
  }            
  return out;
}
')

my_cum_sum(c(1,2,3,4,5,6,7,9,10))


################### Exercise 3 ###########################
cppFunction('
NumericVector my_range(NumericVector x){
  NumericVector out(2);
  out[0]=min(x);
  out[1]=max(x);
  return out;
}            
')

my_range(c(3,1,5,2))


################### Exercise 4 ###########################
cppFunction('
NumericMatrix my_info(NumericMatrix x){
  int ncol=x.ncol();
  int nrow=x.nrow();
  NumericMatrix out(nrow,4);
  int i;
  for (i=0;i<nrow;++i){
    out(i,0)=min(x(i,_));
    out(i,1)=max(x(i,_));
    out(i,2)=mean(x(i,_));
    out(i,3)=sd(x(i,_));
  }
  return out;
}
')

my_info(matrix(runif(30),nrow=5))
