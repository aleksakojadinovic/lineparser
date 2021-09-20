from src.abstractions.abstractparser import ParseSystem
from src.common.parsers.basic import MNOfMatrixParser
from src.common.parsers.simple import NIntsParser

if __name__ == '__main__':
    p = ParseSystem()
    p += NIntsParser(n=2) > ['m', 'n']
    p += MNOfMatrixParser(fcast=int, n=p['n'], scope=p['m']) > 'matrix'


    p(filepath='src/test_files/dim_and_matrix_1.txt')

    print(p.saved_data)






