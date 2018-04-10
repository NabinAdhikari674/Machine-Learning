from sklearn import tree
features =[[10,0],[12,0],[20,1],[25,1]]
labels=['a','a','b','b']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print (clf.predict([[13,0]]))
