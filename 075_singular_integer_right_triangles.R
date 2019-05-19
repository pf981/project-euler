library("tidyverse")

# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

generate_triplets <- function(max_length = 48) {
  max_m <- sqrt(max_length / 2) %>% as.integer()
  
  primitive_triplets <- map_dfr(seq_len(max_m), function(n) {
    map_dfr(seq(from = n + 1, to = max_m), function(m) {
      tibble(
        m,
        n,
        a = m^2 - n^2,
        b = 2 * m * n,
        c_ = m^2 + n^2,
        total_length = a + b + c_)
    })
  })
  
  primitive_triplets <-
    primitive_triplets %>%
    filter(
      total_length <= max_length,
      (n + m) %% 2 == 1, # Only keep primitive triplets
      gcd(n, m) == 1
    ) %>%
    arrange(total_length)
  
  all_triplets <-
    primitive_triplets %>%
    mutate(multiplier = map(max_length / total_length, seq_len)) %>%
    unnest() %>%
    mutate(
      a = a * multiplier,
      b = b * multiplier,
      c_ = c_ * multiplier,
      total_length = total_length * multiplier
    ) %>%
    # mutate_at(vars(a, b, c_, total_length), ~ . * multiplier) %>%
    arrange(total_length)
  all_triplets
}

count_singular <- function(triplets) {
  triplets %>%
    group_by(total_length) %>%
    count() %>%
    filter(nn == 1) %>%
    nrow()
}


generate_triplets()
generate_triplets() %>% count_singular()

df <- generate_triplets(1500000)
df %>% count_singular()



# Scratch -----------------------------------------------------------------
all_triplets <- function(triplets, max_length) {
  triplets %>%
    mutate(multiplier = map(max_length / total_length))
}





# https://en.wikipedia.org/wiki/Diophantine_equation
# https://en.wikipedia.org/wiki/Pythagorean_triple

a^2 + b^2 = c^2
a + b + c = L

a + b + c^2 = L

# Largest L is 120
# This would be sides 1 + 60 + 60; approx
# So we just need to test integers up to 60. (half max)


count_triangles <- function(max_length = 48) {
  triangles <- integer(max_length)
  all_a <- integer(max_length)
  all_b <- integer(max_length)
  all_c <- integer(max_length)
  
  max_m <- sqrt(max_length)
  
  for (m in seq_len(max_m))  {
    for (n in seq_len(max_m))  {
      a <- m^2 - n^2
      b <- 2 * m * n
      c_ <- m^2 + n^2
      
      total_length <- a + b + c_
      
      triangles[[total_length]] <- triangles[[total_length]] + 1
      
      all_a[[total_length]] <- triangles[[total_length]] + 1
    }
  }

  triangles
}





primitive_triplets <- function(max_length = 48) {
  max_m <- sqrt(max_length / 2) %>% as.integer()
  
  triangles <- map_dfr(seq_len(max_m), function(n) {
    map_dfr(seq(from = n + 1, to = max_m), function(m) {
      tibble(
        m,
        n,
        a = m^2 - n^2,
        b = 2 * m * n,
        c_ = m^2 + n^2,
        total_length = a + b + c_)
    })
  })
  
  triangles %>%
    filter(
      total_length <= max_length,
      (n + m) %% 2 == 1, # Only keep primitive triplets
      gcd(n, m) == 1
    ) %>%
    arrange(total_length)
}




primitive_triplets <- function(max_length = 48) {
  max_m <- sqrt(max_length / 2) %>% as.integer()
  
  triangles <- map_dfr(seq_len(max_m), function(n) {
    map_dfr(seq(from = n + 1, to = max_m), function(m) {
      tibble(
        a = m^2 - n^2,
        b = 2 * m * n,
        c_ = m^2 + n^2,
        total_length = a + b + c_)
    })
  })
  
  triangles %>%
    filter(total_length <= max_length) %>%
    arrange(total_length)
}

df <- primitive_triplets()
df

df %>% mutate()

cross2(1:10, 1:10)[[1]]

