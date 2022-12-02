def roots_of_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return(["all"])
            else:
                return []
        else:
            if c == 0:
                return(["0"])
            else:
                return[-c / b]
    else:
        d = b ** 2 - 4 * a * c
        if d >= 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            if x1 == x2:
                return [x1]
            else:
                return [x1, x2]
        else:
            return []


def solve(*coefficients):
    if len(coefficients) > 3:
        return None
    elif len(coefficients) <= 0:
        return None
    if len(coefficients) == 3:
        return roots_of_quadratic_equation(*coefficients)
    elif len(coefficients) == 2:
        b, c = coefficients[0], coefficients[1]
        return [-c / b]
    elif len(coefficients) == 1:
        if coefficients[0] == 0:
            return ['all']
        else:
            return []


coeff = [int(i) for i in input().split()]
if len(coeff) == 1:
    print(*sorted(solve(coeff[0])))
elif len(coeff) == 2:
    print(*sorted(solve(coeff[0], coeff[1])))
elif len(coeff) == 3:
    print(*sorted(solve(coeff[0], coeff[1], coeff[2])))