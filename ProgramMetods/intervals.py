def Search_Interval(f, initialX, finalX, paso=0.1):
    interval = []

    actualX = initialX
    actualValue = f(actualX)

    for nextX in range(initialX + 1, finalX + 1):
        nextValue = f(nextX)

        if actualValue * nextValue < 0:
            interval.append((actualX, nextX))
        
        actualX = nextX
        actualValue = nextValue

    print("Intervalo encontrado:", interval)
    return interval