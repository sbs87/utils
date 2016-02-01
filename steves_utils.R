defactor.numeric <- function(vector_as_factors) {
   return(as.numeric(levels(vector_as_factors))[vector_as_factors])
 }
