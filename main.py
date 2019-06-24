import function
import function_matrix
from matrix_entry import MatrixEntry
from relation_symbol import RelationSymbol

matrix = [
    [MatrixEntry(2, function.sin), MatrixEntry(3, function.Power(3))],
    [MatrixEntry(-1, function.log2), MatrixEntry(100, function.arcsin)]
]

rel_symbols = [RelationSymbol.GreaterThanOrEqual, RelationSymbol.LessThanOrEqual]

values = [2, 3]

function_matrix.normalize(matrix, rel_symbols, values)

generators = function_matrix.obtain_generators(matrix)

res = function_matrix.evaluate(matrix, generators)