import numpy as np 
import matplotlib.pyplot as plt 

# Given inputs and outputs
X = [0,1,2,3,4]
y = [1,3,7,13,21]

N = len(X)

sum_X = np.sum(X)
sum_y = np.sum(y)
sum_Xy = np.sum(np.multiply(X,y))
sum_X2 = np.sum(np.square(X))

print(sum_X,"	",sum_y,"	",sum_Xy,"		",sum_X2)

# Finding the coefficients for the best fit line
w1 = (sum_Xy-(sum_X*sum_y)/N)/(sum_X2-(sum_X*sum_X)/N)
w0 = (sum_y/N)-(w1*(sum_X/N))

print(w0,"		",w1) 
y_pred = []
for i in range(5):
	y_pred.append(w0+w1*X[i])

print(y_pred)

plt.scatter(X,y,color='Red')
plt.plot(X,y_pred,color='Blue')
plt.title("Regression")
plt.xlabel("X-label")
plt.ylabel("y-label")
plt.show()