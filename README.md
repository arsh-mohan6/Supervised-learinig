#  Ordinary Least Squares (OLS) Linear Regression — From Scratch

This project demonstrates how to implement **Ordinary Least Squares (OLS)** linear regression **without using any external libraries** like NumPy or pandas.  
It’s a simple and educational example of how linear regression works under the hood.

---

##  Features
- Calculates **slope (m)** and **intercept (b)** manually  
- Uses basic Python operations only  
- Predicts `y` values for given `x` inputs  
- Clean and minimal code — great for learning regression fundamentals  

---

##  Formula

The best-fit line is given by:

\[
y = m x + b
\]

\[
x_mean = sum(x)/len(x)
\]


\[
y_mean = sum(y)/len(y)
\]


Where:

\[
m = \frac{\sum (x_i - x_mean)(y_i - y_mean)}{\sum (x_i - x_mean)^2}
\]


\[
b = y_mean - m*x_mean
\]

---
