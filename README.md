# 📊 Ordinary Least Squares (OLS) Linear Regression — From Scratch

This project demonstrates how to implement **Ordinary Least Squares (OLS)** linear regression **without using any external libraries** like NumPy or pandas.  
It’s a simple and educational example of how linear regression works under the hood.

---

## 🚀 Features
- Calculates **slope (m)** and **intercept (b)** manually  
- Uses basic Python operations only  
- Predicts `y` values for given `x` inputs  
- Clean and minimal code — great for learning regression fundamentals  

---

## 🧠 Formula

The best-fit line is given by:

\[
y = m x + b
\]

Where:

\[
m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
\]
\[
b = \bar{y} - m \bar{x}
\]

---

## 🧩 Code Example

```python
x = [1, 2, 3, 4, 5, 6, 6]
y = [7, 8, 9, 6, 5, 4, 3]

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

upperPart = 0
lowerPart = 0

for i in range(len(x)):
    upperPart += (x[i] - x_mean) * (y[i] - y_mean)
    lowerPart += (x[i] - x_mean) ** 2

m = upperPart / lowerPart
b = y_mean - m * x_mean

def _predicted(x_val):
    return m * x_val + b

print("Slope of the Model (m):", m)
print("Intercept of the Model (b):", b)

for xi in x:
    print(f"x={xi}, Predicted ŷ={_predicted(xi):.2f}")
