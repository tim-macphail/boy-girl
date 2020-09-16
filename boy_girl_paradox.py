# solve the boy girl paradox
import random

sample_set = 0
desired_outcomes = 0
repetitions = 0


# generates a case of two random kids
def generate_case():
    kids = [random.choice(["BOY", "GIRL"]), random.choice(["BOY", "GIRL"])]
    return kids


while repetitions < 1000:
    # generate the case for this repetition
    case = generate_case()
    # choose at random one of the kids to open the door
    door_child = random.randint(0, 1)

    # if door child is GIRL, add 1 to sample_set (it meets the pre-existing condition)
    if case[door_child] == "GIRL":
        sample_set += 1
        # if the other child is also GIRL, add 1 to desired_outcomes
        if case[door_child - 1] == "GIRL":   # [door_child - 1] gives the index of the other child, either 0 or -1
            desired_outcomes += 1
        # if the second is not GIRL, do not add to desired outcomes
    # if the door child is BOY, do not add 1 to sample set or desired_outcomes (it does not meet pre-existing condition)
    repetitions += 1    # move on to the next repetition
# repeat for 1000 repetitions

# calculate the probability of 2 GIRLS given 1 GIRL
probability = desired_outcomes / sample_set
print(probability)


