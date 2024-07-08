def bayes():
    prior_a = float(input("Enter the prior probability of event A: "))
    prior_b = float(input("Enter the prior probability of event B: "))
    conditional_b_given_a = float(input("Enter the conditional probability of event B given event A: "))
    denominator = prior_b
    numerator = prior_a * conditional_b_given_a
    pro_a_given_b = numerator / denominator
    return pro_a_given_b
print(bayes())