#import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

#print(aaron_judge.type.unique())
#print(aaron_judge.head())
david_ortiz['type'] = david_ortiz['type'].map({'S': 1, 'B': 0})
#print(aaron_judge.type)
#print(aaron_judge['plate_x'])
#print(aaron_judge['plate_z'])
david_ortiz = david_ortiz.dropna(subset = ['type', 'plate_x', 'plate_z', 'events'])
#print(david_ortiz)

fig, ax = plt.subplots()
plt.scatter(david_ortiz['plate_x'], david_ortiz['plate_z'], c = david_ortiz['type'], cmap = plt.cm.coolwarm, alpha = 0.25)

training_set, validation_set = train_test_split(david_ortiz, random_state = 1)
classifier = SVC(kernel = 'rbf', gamma = 3.3, C = 1)
classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])
print(classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type']))
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 6)
draw_boundary(ax, classifier)

plt.show()
