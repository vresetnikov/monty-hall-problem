# Monty Hall problem expressed in Python.
# We are always opting to change when offered by the game host and by doing so we are expecting a 66% win rate.
# https://github.com/vresetnikov

import random

choices = [True, False, False]
success = 0
iterations = 2555  # increase iterations for better accuracy

for _ in range(iterations):
    random.shuffle(choices)  # optional, spice things up
    choice = random.choice(choices)

    # our initial choice was a failure, however with the game host removing 1 failure and by us always
    # opting for change we unknowingly switch to the only possible alternative - success:

    if not choice:
        success += 1

ratio = round(success / iterations * 100, 2)

print(f"{iterations} games complete of which {success} were wins. ({ratio})%")
