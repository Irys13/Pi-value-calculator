pi_value = 4.0
four = 4.0
denominator_value = 3.0
iterations = 50000000 #accuracy, the higher the value the more accurate it is

for i in range(0, iterations):
    if pi_value == 4: #first calculation
        pi_value = float(pi_value - float(four / denominator_value))
        print("%0.20f" % pi_value)
        denominator_value += 2

    if i % 2 == 0: #when formula requires addition
        pi_value = float(pi_value + float(four / denominator_value))
        print("%0.20f" % pi_value)
        denominator_value = denominator_value + 2

    if i % 2 == 1: #when formula requires subtraction
        pi_value = float(pi_value - float(four / denominator_value))
        print("%0.20f" % pi_value)
        denominator_value = denominator_value + 2