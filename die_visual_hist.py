from die import  Die
import pygal

#create a die of 6 sides
die1 = Die()
die2 = Die()

#Make some rolls and store as results
results = []
times_to_roll = int(input("Enter the number of times you want to roll the dice:"))
for roll_num in range(times_to_roll):
    number_rolled = die1.roll_die() + die2.roll_die()
    results.append(number_rolled)
#Analyze the results
frequencies = []
max_result = die1.num_of_sides + die2.num_of_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist._title = f"Results of rolling 2 dice {times_to_roll}"
hist.x_labels = range(2, max_result+1)
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add("2 X D6", frequencies)
hist.render_to_file("die_visual.svg")