# Python has a match-case statement, similar to switch-case in languages like C, C++, Java, or JavaScript.

# match value:
#     case pattern1:
#         # code
#     case pattern2:
#         # code
#     case _:
#         # default case

# "Match if the value is an instance of int."

value = 2j

match value:
    case int():
        print('Numeric')
    case float():
        print('Float')
    case str():
        print('String')
    case _:
        print('Other')


country = "USA"

match country:
    case "India":
        print('Ind')
    case "pakistan":
        print('pak')
    case "United State" | "USA": # Muiltiple cases we can write with | operator
        print('US')
    case _:
        print('Not a country')

        