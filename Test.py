def main():
    """
    Сложность: O(n)
    """
    import numpy as p

    print(f'Enter number matrix A:')
    matrixA = p.matrix([[int(input()), int(input()), int(input())],
                        [int(input()), int(input()), int(input())]])
    print(f'Matrix A: {matrixA}')

    print(f'Enter number matrix B:')
    matrixB = p.matrix([[int(input()), int(input())],
                        [int(input()), int(input())],
                        [int(input()), int(input())]])
    print(f'Matrix B: {matrixB}')

    print(f'Multi: {matrixA * matrixB}')


if __name__ == '__main__':
    main()
