import fractions
import math

first_fraction_numerator = int(input("please enter first fraction numerator: "))
first_fraction_denominator = int(input("please enter first fraction denominator: "))
second_fraction_numerator = int(input("please enter second fraction numerator: "))
second_fraction_denominator = int(input("please enter second fraction denominator: "))


def sum_of_fractions(first_fr_num: int, first_fr_denom: int,
                     second_fr_num: int, sec_fr_denom: int) -> str:
    sum_fraction_numerator = first_fr_num * sec_fr_denom + \
                             second_fr_num * first_fr_denom

    sum_fraction_denominator = first_fr_denom * sec_fr_denom
    fraction_reducer = int(math.gcd(sum_fraction_numerator, sum_fraction_denominator))

    return str(f'{int(sum_fraction_numerator / fraction_reducer)}/'
               f'{int(sum_fraction_denominator / fraction_reducer)}')


def product_of_fractions(first_fr_num: int, first_fr_denom: int,
                         second_fr_num: int, sec_fr_denom: int) -> str:
    product_fraction_numerator = first_fr_num * second_fr_num
    product_fraction_denominator = first_fr_denom * sec_fr_denom
    fraction_reducer = math.gcd(product_fraction_numerator, product_fraction_denominator)

    return str(f'{int(product_fraction_numerator / fraction_reducer)}/'
               f'{int(product_fraction_denominator / fraction_reducer)}')


print(sum_of_fractions(first_fraction_numerator, first_fraction_denominator, second_fraction_numerator,
                       second_fraction_denominator))

print(product_of_fractions(first_fraction_numerator, first_fraction_denominator, second_fraction_numerator,
                           second_fraction_denominator))

print(fractions.Fraction(first_fraction_numerator, first_fraction_denominator) +
      fractions.Fraction(second_fraction_numerator, second_fraction_denominator))

print(fractions.Fraction(first_fraction_numerator, first_fraction_denominator) *
      fractions.Fraction(second_fraction_numerator, second_fraction_denominator))
