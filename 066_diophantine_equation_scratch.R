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

df <- get_convergent_solutions(1000)
df <- get_convergent_solutions(7)
get_convergent_solutions(61)

D <- 61
df$y %>% reduce(c)

get_convergents_x_solution <- function(D = 5) {
  # Init for a
  m <- 0
  d <- 1
  a0 <- floor(sqrt(D))
  a <- a0
  
  # Init for x, y
  x <- a0
  x_prev <- 1
  y <- 1
  y_prev <- 0
  
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
  x
}

get_convergents_x_solution(5)


squares <- seq_len(sqrt(max_d))^2
D <- seq(to = max_d) %>% discard(`%in%`, squares)



# This method uses a to calculate x and y 
# Is d the same d?

my_d <- 7 # Test

# THIS WORKS:
# Init for a
m <- 0
d <- 1
a0 <- floor(sqrt(my_d))
a <- a0

# Init for x, y
x <- a0
x_prev <- 1
y <- 1
y_prev <- 0

for (i in 1:10) {
  cat("a: ", a, "; x: ", x, "; y: ", y, "\n")
  
  # Calculate a
  m <- d * a - m
  d <- (my_d - m^2) / d
  a <- floor((a0 + m) / d)
  
  # Calculate x, y
  x_new_prev <- x
  y_new_prev <- y
  x <- a * x + x_prev
  y <- a * y + y_prev
  x_prev <- x_new_prev
  y_prev <- y_new_prev
}

# ABOVE WORKS


m0 <- 0
d0 <- 1
a0 <- floor(sqrt(my_d))
m_next <- d * a - m
d_next <- (my_d - m_next^2) / d
a_next <- 
  

x <- m




get_convergents_x_solution <- function(d) {
  sqrt_d <- sqrt(d)
  x_prev2 <- 1
  x_prev <- a
  y_prev2 <- 0
  y_prev <- 1
  
  a <- floor(sqrt(d))
  
  while (x^2 - d * y^2 != 1) {
    x <- a * x_prev + x_prev2
    y <- a * y_prev + y_prev2
  }
  x
}

# A: x
# B: y


# https://en.wikipedia.org/wiki/Generalized_continued_fraction
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

# S: d
# m: 
# d:
# a:

my_d <- 7 # Test

m0 <- 0
d0 <- 1
a0 <- floor(sqrt(my_d))
m_next <- d * a - m
d_next <- (my_d - m_next^2) / d
a_next <- 


get_convergents_x_solution <- function(d) {
  sqrt_d <- sqrt(d)
  while (x^2 - d * y^2 != 1) {
    x <- a * x_prev + x_prev2
    y <- a * y_prev + y_prev2
  }
  x
}

# A: x
# B: y


get_convergents_x_solution <- function(d) {
  sqrt_d <- sqrt(d)
  while (x^2 - d * y^2 != 1) {
    x <- a * x_prev + x_prev2
    y <- a * y_prev + y_prev2
  }
  x
}

get_d_with_max_x <- function(max_d = 7) {
  squares <- seq_len(sqrt(max_d))^2
  d <- seq(to = max_d) %>% discard(`%in%`, squares)
  x <- get_convergents_x_solution(d)
  d[which.max(x)]
}


#  Chakaravala’s method

get_d_with_max_x <- function(max_d = 7) {
  squares <- seq_len(sqrt(max_d))^2
  d <- seq(to = max_d) %>% discard(`%in%`, squares)
  
  df <-
    tibble(
      d = d,
      convergents = d %>%
        sqrt() %>%
        map(contfrac::as_cf, n = 100000) %>% # Increase n
        map(contfrac::convergents) %>%
        map(as_tibble) %>%
        map(~rename(., x = A, y = B)),
      solution = map2(convergents, d, ~filter(.x, x^2 - .y * y^2 == 1) %>% slice(1))
      # solution = map2(convergents, d, ~filter(.x, x^2 - .y * y^2 == 1) %>% filter(x == min(x)))
    ) %>%
    unnest(solution)
  
  df %>% filter(x == max(x)) %>% pull(d)
}
# A and B mixed up?
get_d_with_max_x(1000)
get_d_with_max_x(7)

# The reason it isn't working is because n isn't big enough
df %>% mutate(s = map_int(solution, nrow)) %>% arrange(s)
df %>% mutate(s = map_int(solution, nrow)) %>% filter(s == 0)


df <-
  tibble(
    d = d,
    convergents = d %>%
      sqrt() %>%
      map(contfrac::as_cf, n = 100) %>% # Increase n
      map(contfrac::convergents) %>%
      map(as_tibble) %>%
      map(~rename(., x = A, y = B)),
    solution = map2(convergents, d, ~filter(.x, x^2 - .y * y^2 == 1) %>% filter(x == min(x)))
  ) %>%
  unnest(solution, .drop = FALSE)

df$convergents %>% head()

1

sqrt(7) %>% contfrac::as_cf() %>% contfrac::convergents()

sqrt(7) %>% contfrac::CF()


contfrac::GCF(2, 1)
contfrac::gconvergents(3, 1, b0 = 1)


# Why doesn't this work? --------------------------------------------------


get_d_with_max_x <- function(max_d = 7) {
  squares <- seq_len(sqrt(max_d))^2
  d <- seq(to = max_d) %>% discard(`%in%`, squares)
  
  df <-
    tibble(
      d = d,
      convergents = d %>%
        sqrt() %>%
        map(contfrac::as_cf, n = 100000) %>% # Increase n
        map(contfrac::convergents) %>%
        map(as_tibble) %>%
        # map(~rename(., x2 = A, y2 = B)),
        map(~rename(., x = A, y = B)),
      # solution = map2(convergents, d, ~filter(.x, x2 - .y * y2 == 1) %>% filter(x == min(x)))
      solution = map2(convergents, d, ~filter(.x, x^2 - .y * y^2 == 1) %>% filter(x == min(x)))
    ) %>%
    unnest(solution)
  
  df %>% filter(x2 == max(x2)) %>% pull(d)
}
# A and B mixed up?
get_d_with_max_x(1000)
get_d_with_max_x(7)

df %>% mutate(rhs = x^2 - d * y^2) %>% View()

# Wrong Attempts :
# 533
# 795
# 307

#

get_d_with_max_x <- function(max_d = 7) {
  squares <- seq_len(sqrt(max_d))^2
  d <- seq(to = max_d) %>% discard(`%in%`, squares)
  
  df <-
    tibble(
      d = d,
      convergents = d %>%
        sqrt() %>%
        map(contfrac::as_cf, n = 100000) %>% # Increase n
        map(contfrac::convergents) %>%
        map(as_tibble) %>%
        # map(~rename(., x = B, y = A)),
        map(~rename(., x = A, y = B)),
      solution = map2(convergents, d, ~filter(.x, x^2 - .y * y^2 == 1) %>% filter(x == min(x)))
      # solution = map2(convergents, d, ~filter(.x, x^2 - .y * y^2 == 1) %>% filter(x == min(x)))
      # solution = map2(convergents, d, ~filter(.x, A^2 - .y * B^2 == 1) %>% filter(A == min(A)))
      # solution = map2(convergents, d, ~filter(.x, A^2 - .y * B^2 == 1) %>% head(n = 1))
    ) %>%
    unnest(solution)
  
  df %

get_max_x <- function(max_d = 7) {
  squares <- seq_len(sqrt(max_d))^2
  d <- seq(to = max_d) %>% discard(`%in%`, squares)
  
  df <-
    tibble(
      d = D,
      convergents = d %>%
        sqrt() %>%
        map(contfrac::as_cf) %>%
        map(contfrac::convergents) %>%
        map(as_tibble),
      solution = map2(convergents, d, ~filter(.x, A^2 - .y * B^2 == 1) %>% head(n = 1))
    ) %>%
    unnest(solution)
  
  largest_x <- max(df$A)
  largest_x
}


# Scratch -----------------------------------------------------------------


squares <- seq_len(100)^2

D <-
  seq_len(1000) %>%
  discard(`%in%`, squares)



x^2 = 1 + D*y^2


x2 <- seq_len(100)^2



y2 = (x^2 - 1) / D


D <- head(D, n = 5)


# map((x2 - 1) / d

# https://en.wikipedia.org/wiki/Pell%27s_equation

install.packages("contfrac")



contfrac::convergents(sqrt(2))


jj <- contfrac::convergents(c(3,7,15,1,292))
contfrac::convergents(rep(1,10))
contfrac::convergents(c(1,1,1,1,1))


contfrac::as_cf(pi)

D
D2 <- D^2


D <- 2
contfrac::as_cf(D)

contfrac::GCF(D)



contfrac::convergents(rep(pi,10))

contfrac::as_cf(pi) %>% contfrac::convergents()
contfrac::as_cf(pi) %>% contfrac::gconvergents()



contfrac::as_cf(pi) %>% contfrac::convergents()
contfrac::as_cf(pi)


contfrac::convergents(c(3,7,15,1,292))


# THIS
contfrac::as_cf(pi) %>% contfrac::convergents()



contfrac::as_cf(sqrt(5)) %>% contfrac::convergents()
contfrac::as_cf(sqrt(D)) %>% contfrac::convergents()

D %>%
  head() %>%
  sqrt() %>%
  map(contfrac::as_cf) %>%
  map(contfrac::convergents)

D <- head(D, n = 5)



max_d <- 7

squares <- seq_len(sqrt(max_d))^2
d <- seq(to = max_d) %>% discard(`%in%`, squares)

df <-
  tibble(
    d = D,
    convergents = d %>%
      sqrt() %>%
      map(contfrac::as_cf) %>%
      map(contfrac::convergents) %>%
      map(as_tibble),
    solution = map2(convergents, d, ~filter(.x, A^2 - .y * B^2 == 1) %>% head(n = 1))
  ) %>%
  unnest(solution)

largest_x <- max(df$A)

df <-
  tibble(
    d = D,
    convergents = d %>%
      sqrt() %>%
      map(contfrac::as_cf) %>%
      map(contfrac::convergents) %>%
      map(as_tibble)
  )

df %>%
  mutate(
    solution = map2(convergents, d, ~filter(.x, A^2 - .y * B^2 == 1) %>% head(n = 1))
  ) %>%
  unnest(solution)


get_max_x <- function(max_d = 7) {
  squares <- seq_len(sqrt(max_d))^2
  d <- seq(to = max_d) %>% discard(`%in%`, squares)
  
  df <-
    tibble(
      d = D,
      convergents = d %>%
        sqrt() %>%
        map(contfrac::as_cf) %>%
        map(contfrac::convergents) %>%
        map(as_tibble),
      solution = map2(convergents, d, ~filter(.x, A^2 - .y * B^2 == 1) %>% head(n = 1))
    ) %>%
    unnest(solution)
  
  largest_x <- max(df$A)
  largest_x
}

get_max_x(1000)
