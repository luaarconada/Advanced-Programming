#include <Rcpp.h>
using namespace Rcpp;

// This is a simple example of exporting a C++ function to R. You can
// source this function into an R session using the Rcpp::sourceCpp 
// function (or via the Source button on the editor toolbar). Learn
// more about Rcpp at:
//
//   http://www.rcpp.org/
//   http://adv-r.had.co.nz/Rcpp.html
//   http://gallery.rcpp.org/
//

// [[Rcpp::export]]
double euclidean(NumericVector x, NumericVector y) {
  double distance = sqrt(sum(pow((x-y),2)));
  return distance;
}

// [[Rcpp::export]]
int my_knn_c_euclidean( NumericMatrix X, NumericVector X0, NumericVector y){
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


// [[Rcpp::export]]
int my_knn_c_minkowski( NumericMatrix X, NumericVector X0, NumericVector y, double p){
  // X data matrix with input attributes
  // y response variable values of instances in X  
  // X0 vector of input attributes for prediction (just one instance)
  int nrows=X.nrow();
  double distance=0;
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

// [[Rcpp::export]]
NumericMatrix keepFirstTwoThirds(NumericMatrix mat) {
  int numRows = mat.nrow();
  int numRowsToKeep = (2 * numRows) / 3;
  
  NumericMatrix result(numRowsToKeep, mat.ncol());
  
  for (int j = 0; j < mat.ncol(); ++j) {
    for (int i = 0; i < numRowsToKeep; ++i) {
      result(i, j) = mat(i, j);
    }
  }
  return result;
}
// [[Rcpp::export]]
NumericVector keepFirstTwoThirdsVector(NumericVector vec) {
  int vecSize = vec.size();
  int elToKeep = (2 * vecSize) / 3;
  
  NumericVector result(elToKeep);
  
  for (int j = 0; j < elToKeep; ++j) {
    result(j) = vec(j);
  }
  return result;
}

// [[Rcpp::export]]
NumericMatrix keepLastOneThird(NumericMatrix mat) {
  int numRows = mat.nrow();
  int numRowsToKeep = numRows / 3;
  
  NumericMatrix result(numRowsToKeep, mat.ncol());
  
  for (int i = 0; i < numRowsToKeep; ++i) {
    for (int j = 0; j < mat.ncol(); ++j) {
      result(i, j) = mat(numRows - numRowsToKeep + i, j);
    }
  }
  
  return result;
}

// [[Rcpp::export]]
NumericVector keepLastOneThirdVector(NumericVector vec) {
  int vecSize = vec.size();
  int elToKeep = vecSize / 3;
  
  NumericVector result(elToKeep);
  
  for (int j = 0; j < elToKeep; ++j) {
    result(j) = vec(vecSize - elToKeep + j);
  }
  return result;
}

// [[Rcpp::export]]
int my_knn_tuningp(NumericMatrix X, NumericVector X0, NumericVector y,
                   NumericVector possible_p) {
  int ncol=X.ncol();
  // to keep track of the best accuracies
  int rights;
  double best = 0;
  double best_p = 0;
  
  // split the data in train-test
  // Train data
  NumericMatrix X_train = keepFirstTwoThirds(X);
  NumericVector y_train = keepFirstTwoThirdsVector(y);
  // Test data
  NumericMatrix X_test = keepLastOneThird(X);
  NumericVector y_test = keepLastOneThirdVector(y);
  
  for (int i=0;i<possible_p.size();i++){
    rights = 0;
    
    for (int j=0; j<X_test.nrow();j++){
      int out = my_knn_c_minkowski(X_train, X_test(j,_), y_test(j),
                                   possible_p(i));
      if (out == y_test(j)){
        rights++;
      }
    }
    
    // accuracy for the given p
    double acc = rights/X_test.nrow();
    
    if (acc > best){
      // save the p that gives the best model
      best_p = possible_p(i);
    }
  }
  
  Rcout << "The best value for p is:" << best_p << "\n";
  
  return my_knn_c_minkowski(X, X0, y, best_p);
}
