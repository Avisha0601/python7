import matplotlib.pyplot as plt

animals = ['dog', 'cat', 'kangaroo', 'rabbit']
slices = [8, 3, 2, 5]
colors = ['cyan', 'lavender', 'maroon', 'green']

plt.pie(slices, labels = animals, colors=colors,
        startangle=90, shadow=False, explode=(0,0,0,0),
        radius = 1.4, autopct = '%3.3f%%')
plt.legend()
plt.show()
