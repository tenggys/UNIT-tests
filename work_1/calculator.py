def calculate(first_operand: int, second_operand: int, operator: str) -> int | float:
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
        case '/':
            if second_operand != 0:
                result = first_operand / second_operand
            else:
                raise ArithmeticError("Делить на ноль нельзя!")
        case _:
            raise ValueError("Оператора с неожиданным значением: " + operator)
    return result


def calculateDiscount(purchase_amount: float, discount_amount: int) -> float:
    if discount_amount < 0:
        raise ArithmeticError("Скидки ниже 0 быть не может")
    elif discount_amount > 100:
        raise ArithmeticError("Скидка не ожет быть больше 100")

    return purchase_amount - discount_amount / 100 * purchase_amount