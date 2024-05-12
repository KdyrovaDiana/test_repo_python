def elem(*args):
    my_elements = sorted(*args)
    print(f' Minimum element: {my_elements[0]}, maximum element: {my_elements[-1]}')


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 16, -44, -445, 0, 2, ]
    b = (1, 2, 3, 4, 5, 16, -44, -445, 0, 16, 2)
    c = 1, 2, 3, 4, 5, 16, -44, -445, 0, 16, 2
    print(elem(a))
    print(elem(b))
    print(elem(c))
