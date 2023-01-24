"""

    Roman Numerals Encoder

    Create a function taking a positive integer as its parameter 
    and returning a string containing the Roman Numeral representation 
    of that integer.

    Modern Roman numerals are written by expressing each digit separately 
    starting with the left most digit and skipping any digit with a value of zero. 

    In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
    
    2008 is written as 2000=MM, 8=VIII, or MMVIII. 

    1666 uses each Roman symbol in descending order: MDCLXVI.


    Example:

    solution(1000) -> should return 'M'

    Help:

    Symbol    Value
    I          1
    V          5
    X          10
    L          50
    C          100
    D          500
    M          1000

    Remember that there can't be more than 3 identical symbols in a row.

    Task URL: https://www.codewars.com/kata/51b62bf6a9c58071c600001b

"""

# assert.strictEqual(solution(1000), 'M', '1000 should, "M"')
# assert.strictEqual(solution(1001), 'MI', '1001 should, "MI"')
# assert.strictEqual(solution(1990), 'MCMXC', '1990 should, "MCMXC"')
# assert.strictEqual(solution(2007), 'MMVII', '2007 should, "MMVII"')
# assert.strictEqual(solution(2008), 'MMVIII', '2008 should, "MMVIII"')

import math


def solution(number: int) -> None:

    symbol: dict[str, int] = {

        1:      "I",
        5:      "V",
        10:     "X",
        50:     "L",
        100:    "C",
        500:    "D",
        1000:   "M"
    }

    # Simple Case

    result = ''
    for key, value in symbol.items():
        if key == number:
            result += value
            return result

    # Hard Case

    value = ''
    remainder = number
    for i in sorted(symbol.keys(), reverse=True):
        if remainder > 0:
            multiple = i
            roman_number = symbol[i]
            divider = remainder // multiple
            remainder = remainder % multiple
            value += roman_number * divider
    return value


print(solution(2008))
