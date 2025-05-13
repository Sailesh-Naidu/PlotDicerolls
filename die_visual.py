from die import  Die
import plotly.express as px

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

#visualize the results
title = f"Results of Rolling two D6 {times_to_roll} Times"
labels = {'x':'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y= frequencies, title =title,
             labels = labels, color = frequencies,
             color_discrete_sequence=px.colors.qualitative.Safe
            )
# customize chart
fig.update_layout(xaxis_dtick = 1,
                  title_font_size = 30,
                  font = dict(size = 25),
                  hoverlabel = dict(font_size = 18))

fig.show()
