import time
import numpy as np

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

pi_ref = 3.14159265358979323846

N_values = [10, 100, 1000, 10000]

def rms_error(estimates, reference):
    return np.sqrt(np.mean((np.array(estimates) - reference) ** 2))

results = []
errors = []
times = []

for N in N_values:
    start_time = time.time()
    pi_approx = simpson_1_3(a, b, N)
    end_time = time.time()
    
    exec_time = end_time - start_time
    error = pi_ref - pi_approx
    
    results.append(pi_approx)
    errors.append(error)
    times.append(exec_time)

    print(f"N = {N}")
    print(f"Nilai pi yang dihasilkan: {pi_approx}")
    print(f"Galat: {error}")
    print(f"Waktu eksekusi: {exec_time} detik")
    print()

rms = rms_error(results, pi_ref)
print(f"Galat RMS: {rms}")
