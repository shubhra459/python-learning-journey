import numpy as np
customers = np.array(["C101","C102","C1030","C104","C105"])
random_choice = np.random.choice(customers,3,replace=False)
print(random_choice)