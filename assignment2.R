# Anton MO Eriksson
# anter491
# 2017-11-16

require(readxl)
library(readxl)


setwd("/home/ame/git/tdde01/TDDE01/lab-1")
set.seed(12345)

# 2.1 Import data.
life_expectancy <- data.matrix(read_excel("machines.xlsx"))

# Helper functions for all sub-assiments.
log_likelihood <- function(theta, input_data) {
  prob_model = (theta * exp((-theta) * input_data))
  log_prob_model = sum(log(probability_model(theta, input_data)))
  return(log_prob_model)
}

bayesian_log_likelihood <- function(theta, input_data, lambda) {
  old_prob = (theta * exp((-theta) * input_data))
  new_prob = (lambda * exp((-lambda) * theta))
  bayesion_log_prob = (sum(log(old_prob * new_prob)))
  return(bayesion_log_prob)
}

# 2.2
# Plots the log-likehood curve & prints the maximun likelihood value for theta.
theta = seq(from = 0, to = 10, by = 0.01)
log_lh = c()
for (value in 1:length(theta)) {
  log_lh[value] = log_likelihood(theta[value], life_expectancy) 
}

plot(
  theta,
  log_lh,
  col = "Red",
  xlab = "Theta",
  ylab = "log(p(x|theta))",
  main = c("Max theta = ", max_theta)
)


# 2.3 with only 6 samples.

theta = seq(from = 0, to = 10, by = 0.01)
log_lh_6 = c()
for (value in 1:length(theta)) {
  log_lh_6[value] = log_likelihood(theta[value], life_expectancy[1:6]) 
}
max_theta_6 = theta[which.max(log_lh_6)]

plot(
  theta,
  log_lh_6,
  col = "Pink",
  ylim = c(-300, 0),
  xlab = "Theta",
  ylab = "log(p(x|theta))",
  main = c("Max of thetas are ", max_theta, max_theta_6)
  )
points(theta, log_lh, col = "black")
legend(
  x = "bottomleft",
  legend = c("All data", "Data 1:6"),
  col = c("Black", "Pink"),
  lty = c(1, 1)
)

# Task 2.4
theta = seq(from = 0, to = 10, by = 0.01)
log_lh_bay = c()
for (value in 1:length(theta)) {
  log_lh_bay[value] = bayesian_log_likelihood(theta[value], life_expectancy, 10) 
}

max_theta = theta[which.max(log_lh_bay)]

plot(
  theta,
  log_lh_bay,
  col = "Red",
  xlab = "Theta",
  ylab = "log(p(x|theta))",
  main = c("Max theta = ", max_theta)
)

random_exp_distribution = rexp(50, max_theta)

# 2.5
random_exp_distribution = rexp(50, theta_max)
hist(random_exp_distribution)
hist(life_expectancy)
