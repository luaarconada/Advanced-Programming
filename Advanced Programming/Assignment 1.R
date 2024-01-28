##################### EXERCISE 1 ###############################


###############################################################################
# Code for KNN starts here. You have to translate this code into C++ / Rcpp

my_knn_R = function(X, X0, y){
  # X data matrix with input attributes
  # y response variable values of instances in X  
  # X0 vector of input attributes for prediction (just one instance)
  
  nrows = nrow(X)
  ncols = ncol(X)
  
  distance = 0
  for(j in 1:ncols){
    difference = X[1,j]-X0[j]
    distance = distance + difference * difference
  }
  
  distance = sqrt(distance)
  
  closest_distance = distance
  closest_output = y[1]
  closest_neighbor = 1
  
  for(i in 2:nrows){
    
    distance = 0
    for(j in 1:ncols){
      difference = X[i,j]-X0[j]
      distance = distance + difference * difference
    }
    
    distance = sqrt(distance)
    
    if(distance < closest_distance){
      closest_distance = distance
      closest_output = y[i]
      closest_neighbor = i
    }
  }
  closest_output
}  

# Code for KNN ends here. 
##############################################################################


library(Rcpp)


cppFunction('
int my_knn_c ( NumericMatrix X, NumericVector X0, NumericVector y){
  // X data matrix with input attributes
  // y response variable values of instances in X  
  // X0 vector of input attributes for prediction (just one instance)
  int nrows=X.nrow();
  int ncols=X.ncol();
  double distance=0;
  int j;
  double difference;
  for (j=0;j<ncols;j++){
    difference = X(1,j)-X0[j];
    distance+=difference*difference;
  }
  distance = sqrt(distance);
  double closest_distance=distance;
  double closest_output = y[1];
  int closest_neighbor=1;
  for (int i=1;i<nrows;i++){
    distance=0;
    for (int j=0;j<ncols;j++){
      difference = X(i,j)-X0[j];
      distance+= difference*difference;
    }
    distance=sqrt(distance);
    if (distance<closest_distance){
      closest_distance = distance;
      closest_output = y[i];
      closest_neighbor = i;
    }
  }
  return closest_output;
}
')

# Code for KNN ends here. 
##############################################################################



## Here, we test the function we just programmed ###

# X contains the inputs as a matrix of real numbers
data("iris")
# X contains the input attributes (excluding the class)
X <- iris[,-5]
# y contains the response variable (named medv, a numeric value)
y <- iris[,5]

# From dataframe to matrix
X <- as.matrix(X)
# From factor to integer
y <- as.integer(y)

# This is the point we want to predict

X0 <- c(5.80, 3.00, 4.35, 1.30)



# Using my_knn and class:knn to predict point X0

print(my_knn_R(X, X0, y))

print(my_knn_C(X, X0, y))


library(class)
print(class::knn(X, X0, y, k=1))


library(microbenchmark)
comparison=microbenchmark(my_knn_R(X,X0,y),my_knn_C(X,X0,y),class::knn(X,X0,y))
comparison
#Microbenchmark creates a dataframe of 100 iterations of each function and it 
#gives its time




#comparison_R = comparison[comparison$expr=="my_knn_R(X, X0, y)",]
#comparison_C = comparison[comparison$expr=="my_knn_C(X, X0, y)",]
#comparison_class = comparison[comparison$expr=="class::knn(X, X0, y)",]


##################### EXERCISE 2 ###############################


