def f(x):
    return 4 / (1 + x**2)

def simpson_1_3(a, b, n):
    if n % 2 == 1:
        raise ValueError("n harus genap untuk metode Simpson 1/3.")
    
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    integral *= h / 3
    return integral

a = 0
b = 1
n = 1000

pi_approx = simpson_1_3(a, b, n)
print(f"Nilai pi yang dihasilkan dengan metode Simpson 1/3 yaitu: {pi_approx}")
