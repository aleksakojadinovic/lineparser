from src.abstractions.abstractparser import ParseSystem
from src.common.basic import NOfParser, SingleOfParser, MNOfMatrixParser

if __name__ == '__main__':
    p = ParseSystem()
    p += NOfParser(fcast=int, n=2) > ['m', 'n']
    p += MNOfMatrixParser(fcast=int, m=p['m'], n=p['n'], scope=p['m']) > 'matrix'

    p(filepath='src/test_files/dim_and_matrix_1.txt')

    print(p.saved_data)






