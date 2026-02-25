import numpy as np
import time

N = 10**8
rng = np.random.default_rng()

# float32 reduces memory pressure (faster on many systems)
a = rng.random(N, dtype=np.float32)
b = rng.random(N, dtype=np.float32)

# warm-up
_ = np.dot(a, b)

repeats = 5
times = []

for i in range(repeats):
    start = time.perf_counter()
    result = np.dot(a, b)
    end = time.perf_counter()
    times.append(end - start)

best_time = min(times)  # best-case timing is usually most stable
gflops = (2 * N) / (best_time * 1e9)

print(f"Inner product: {result}")
print(f"Best time: {best_time:.6f} s")
print(f"Estimated performance: {gflops:.2f} GFLOPS/s")