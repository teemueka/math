import numpy as np

#Määrittele ja esitä 5-alkioinen kokonaislukutaulukko numpyn avulla. luvut voivat olla satunnaisia.

lukutaulukko = np.random.randint(1, 11, 5)
print(lukutaulukko)

#Sinulla on vektorit a) u = 2i + 3j, v =4i - 7j

u = np.array([2, 3])  # u = 2i + 3j
v = np.array([4, -7])  # v = 4i - 7j

# b) uu= i + j + k, vv 3i -3j + 2k.

uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

#Laske kunkin vektorin normi.

vektorit = [u, v, uu, vv]

for vektori in vektorit:
    normi = np.linalg.norm(vektori)
    print(f"Vektorin {vektori} normi on {normi:.2f}")
