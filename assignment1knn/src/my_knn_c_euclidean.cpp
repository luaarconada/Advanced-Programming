#include <Rcpp.h>
using namespace Rcpp;


// [[Rcpp::export]]
double euclidean(NumericVector x, NumericVector y) {
  double distance = sqrt(sum(pow((x-y),2)));
  return distance;
}


int my_knn_c_euclidean ( NumericMatrix X, NumericVector X0, NumericVector y){
  // X data matrix with input attributes
  // y response variable values of instances in X  
  // X0 vector of input attributes for prediction (just one instance)
  int nrows=X.nrow();
  int ncols=X.ncol();
  double distance=0;
  int j;
  distance=euclidean(X(1,_),X0);
  double closest_distance=distance;
  double closest_output = y[1];
  int closest_neighbor=1;
  for (int i=1;i<nrows;i++){
    distance=euclidean(X(i,_),X0);
    if (distance<closest_distance){
      closest_distance = distance;
      closest_output = y[i];
      closest_neighbor = i;
    }
  }
  return closest_output;
}