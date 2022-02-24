from Task2B import task2b


def test_task2():
    #Test for task 2B - if a station is returned where the ratio is not greater than 0.8 then the
    #assertion will fail.
    point8 = task2b()
    state1 = True
    for tuple in point8:
        if tuple[1] < 0.8:
            state1 = False
            break
    assert state1 == True

    #Test for task 2C -
    return 