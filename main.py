import string


def middle(n):
    return n[0]


def sort_tp(list_of_tuples):
    return sorted(list_of_tuples, key=middle)


def sort_first_elements(minterms):
    minterms = sort_tp(minterms)
    return minterms


def generate_first_elements(minterms, weights):
    first_minterms = list()
    for i in range(0, len(minterms)):
        tp = (weights[i], minterms[i])
        first_minterms.append(tp)
    return sort_first_elements(first_minterms)


def print_weights(minterms, weights):
    print("Sulyszamok: ")
    for i in minterms:
        print(i, end="\t")
    print()
    for i in minterms:
        print("|", end="\t")
    print()
    for i in weights:
        print(i, end="\t")
    print()
    print()
    print()


def get_unique_weightcount(tuples):
    counter = 1
    x, _ = tuples[0]
    for i in range(0, len(tuples)):
        y, _ = tuples[i]
        if x != y:
            x = y
            counter += 1
    return counter


def generate_weight_groups(minterms):
    groups = dict()
    weights = set()
    helper = list()
    for p in range(0, len(minterms)):
        s, _ = minterms[p]
        weights.add(s)
    for z in weights:
        helper = []
        for j in minterms:
            a, b = j
            if a == z:
                helper.append(b)
        groups[z] = helper
    return groups


def quine_mccluskey(minterm_numbers, variable_count):
    minterm_numbers.sort()
    weights = [calc_weight(x, variable_count) for x in minterm_numbers]
    print_weights(minterm_numbers, weights)
    first_column = generate_weight_groups(sort_first_elements(generate_first_elements(minterm_numbers, weights)))
    print("Sulyszam\t" + "Minterm sorszamok")
    print("---" * 10)


def calc_weight(min_num, var_num):
    in_binary = list(decimal_to_binary(min_num, var_num))
    weight = 0
    for i in in_binary:
        if i == '1':
            weight += 1
    return weight


def binary_to_char(binary):
    characters = list(string.ascii_uppercase)
    binary_str = list(binary)
    result = ""
    for i in range(0, len(binary)):
        if binary_str[i] == '0':
            result += "!" + characters[i]
        else:
            result += characters[i]
    return result


def decimal_to_binary(num, var_num):
    binary = bin(num).replace("0b", "")
    if var_num > len(binary):
        difference = var_num - len(binary)
        fill = '0' * difference
        binary = fill + binary
    return binary


if __name__ == '__main__':
    """print("Q(ABC....F)=Σmi(i=x,y,z....)")
    minterms = input("Minterm szamok(i): ")
    variablecount = int(input("Valtozok szama: "))

    minterms = minterms.split(',')
    minterms = [int(x) for x in minterms]
    print(minterms)
"""
    testcase = [1, 3, 12, 13, 14, 15, 17, 19, 28, 29, 30, 31]
    testcase_num = 5
    quine_mccluskey(testcase, testcase_num)
