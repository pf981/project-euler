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
