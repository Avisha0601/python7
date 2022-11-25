import matplotlib.pyplot as plt

left = [1,2,3,4,5]
height = [32, 44, 27, 19, 36]

tick_label = ['English', 'Maths', 'Science', 'Geography', 'History & Civics']

plt.bar(left, height, tick_label = tick_label,
        width=0.9, color=['purple', 'cyan', 'green', 'brown', 'red'])

plt.xlabel('x-Subject Name')
plt.ylabel('y-Rate')
plt.title('Subjects')
plt.show()