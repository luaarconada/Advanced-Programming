#include <Rcpp.h>
using namespace Rcpp;


// [[Rcpp::export]]
double minkowski(NumericVector x, NumericVector y, double p){
  double distance;
  if (p > 0){
    distance = pow(sum(pow(x-y,p)),1/p);
  }
  else{
    distance = sum(abs(x-y));
  }
  return distance;
}



int my_knn_c_minkowski ( NumericMatrix X, NumericVector X0, NumericVector y, double p){
  // X data matrix with input attributes
  // y response variable values of instances in X  
  // X0 vector of input attributes for prediction (just one instance)
  int nrows=X.nrow();
  int ncols=X.ncol();
  double distance=0;
  int j;
  distance=minkowski(X(1,_),X0,p);
  double closest_distance=distance;
  double closest_output = y[1];
  int closest_neighbor=1;
  for (int i=1;i<nrows;i++){
    distance=minkowski(X(i,_),X0,p);
    if (distance<closest_distance){
      closest_distance = distance;
      closest_output = y[i];
      closest_neighbor = i;
    }
  }
  return closest_output;
}
