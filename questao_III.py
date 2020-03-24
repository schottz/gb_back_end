acao = [7,1,5,3,6,4]

def get_smaller(array):

    val = 100

    for a in array:
        if a < val:
            val = a

    return val, array.index(val)

def get_bigger(array, smaller_index):

    smaller = array[smaller_index]
    val = None

    for a in array:
        if array.index(a) > smaller_index:
            if val is None:
                if a > smaller:
                    val = a
                else: pass
            elif a > val:
                val = a
            elif a <= val:
                pass
        else:
            pass

    return val

def main():

    smaller, smaller_index = get_smaller(acao)
    bigger = get_bigger(acao, smaller_index)

    if bigger is not None:
        print(f"Lucro máximo: {bigger - smaller}.\nComprou no dia {acao.index(smaller) + 1} (Preço igual a {smaller}) e vendeu no dia {acao.index(bigger) + 1} (Preço igual a {bigger})\nLucro foi de {bigger} - {smaller} igual a {bigger - smaller}")
    else:
        print("Lucro 0, pois nenhuma transação foi feita")

if __name__ == "__main__":
    main()