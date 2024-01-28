#include <Rcpp.h>
using namespace Rcpp;


// [[Rcpp::export]]
double sumC(NumericVector x){
  int n= x.size();
  double total=0;
  for (int i=0;i<n,++i){
    double total= total+x[i];
  }
  return total;
}

// [[Rcpp::export]]
NumericVector timesTwo(NumericVector x) {
  return x * 2;
}


// You can include R code blocks in C++ files processed with sourceCpp
// (useful for testing and development). The R code will be automatically 
// run after the compilation.
//

/*** R
timesTwo(42)
*/
