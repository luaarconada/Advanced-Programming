#include <Rcpp.h>
using namespace Rcpp;


// [[Rcpp::export]]
int my_knn_tuningp(NumericMatrix X, NumericVector X0, NumericVector y,
                   NumericVector possible_p) {
  int ncol=X.ncol();
  // to divide train-test in 2/3-1/3
  int part = int(2/3*ncol);
  // to keep track of the best accuracies
  double best = 0;
  int best_ind;
  
  // split the data in train-test
  // Train data
  NumericMatrix train_data = X(Range(0, part), _);
  NumericVector y_train = y[Range(0, part)];
  
  // Test data
  NumericMatrix test_data = X(Range(part + 1, X.nrow() - 1), _);
  NumericVector y_test = y[Range(part + 1, y.size() - 1)];
  
  for (int i=0;i<possible_p.size();i++){
    int rights = 0;
    for (int j=0; j<test_data.nrow();i++){
      int out = my_knn_c_minkowski(train_data, test_data(j,_), possible_p(j));
      if (out == y_test(j)){
        rights++;
      }
      // calculate accuracy for the given p
      double acc = rights/test_data.ncol();
      if (acc > best){
        // save the index of the p that gives the best model
        best_ind = i;
      }
    }
  }
  
  return my_knn_c_minkowski(X, X0, possible_p(best_ind));
}
