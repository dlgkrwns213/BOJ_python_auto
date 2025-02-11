while True:
    x = float(input())
    if x < 0:
        break

    print(f'Objects weighing {x:.2f} on Earth will weigh {0.167*x:.2f} on the moon.')