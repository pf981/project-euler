library("gmp")
library("tidyverse")

# This method calculates a https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion


get_convergent_solution <- function(D = 5) {
  # Init for a
  m <- 0
  d <- 1
  a0 <- floor(sqrt(D))
  a <- a0
  
  # Init for x, y
  x <- gmp::as.bigz(a0)
  x_prev <- gmp::as.bigz(1)
  y <- gmp::as.bigz(1)
  y_prev <- gmp::as.bigz(0)
  
  while (x^2 - D * y^2 != 1) {
    # cat("a: ", a, "; x: ", x, "; y: ", y, "\n")
    
    # Calculate a
    m <- d * a - m
    d <- (D - m^2) / d
    a <- floor((a0 + m) / d)
    
    # Calculate x, y
    x_new_prev <- x
    y_new_prev <- y
    x <- a * x + x_prev
    y <- a * y + y_prev
    x_prev <- x_new_prev
    y_prev <- y_new_prev
  }
  tibble(D, x = as.list(x), y = as.list(y))
  # tibble(D, x, y)
}

get_convergent_solutions <- function(max_D = 7) {
  squares <- seq_len(sqrt(max_D))^2
  D <- seq(to = max_D) %>% discard(`%in%`, squares)
  
  map_dfr(D, get_convergent_solution)# %>%
    # mutate_if(is_list, reduce, c)
}

get_d_with_max_x <- function(df) {
  df %>% slice(which.max(reduce(x, c))) %>% pull(D)
  # df %>% filter(x == max(x)) %>% pull(D)
}


get_convergent_solution(5)
get_convergent_solutions(7)

get_convergent_solutions(7) %>% get_d_with_max_x()
get_convergent_solutions(1000) %>% get_d_with_max_x()
