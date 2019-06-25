from function_matrix import evaluate

def generate(matrix, generators):
    rows = len(matrix[0])
    while True:
        try:
            values = []
            for i in range(rows):
                values.append(generators[i].generate())
            result = evaluate(matrix, values)
            return result
        except:
            # overflow error, ignore and try again
            pass