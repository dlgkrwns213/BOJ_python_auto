t1, e1, f1 = map(int, input().split())
time1 = t1 * 3 + e1 * 20 + f1 * 120

t2, e2, f2 = map(int, input().split())
time2 = t2 * 3 + e2 * 20 + f2 * 120

print(("Draw", "Max", "Mel")[(time1 > time2) - (time1 < time2)])