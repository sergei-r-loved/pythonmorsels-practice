# Accept a number as a command-line argument
# Output that number spelled out in English along with the number of letters in that number
# Take the number of letters as the new number and repeat from step 1
# Once the four is reached (it will be fairly quickly), the program should print Done. and exit

import argparse

parser = argparse.ArgumentParser(
    "Turns a pipe-delimited file into a comma-delimited file."
)
parser.add_argument("start_number", type=int)
args = parser.parse_args()

result = object()
new_number = object()
counter = 0

numbers_spell_map = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

while result != "four":
    if counter > 0:
        if 100 <= new_number <= 1000:
            hund, remainder = divmod(new_number, 100)
            if remainder:
                if 0 <= remainder <= 19:
                    print(
                        f"The word {numbers_spell_map.get(hund) + " " + "hundred"} 
                        {numbers_spell_map.get(remainder)} has 
                        {len(str(numbers_spell_map.get(hund)) + 
                             "hundred" + 
                             str(numbers_spell_map.get(remainder)))} 
                             letters in it."
                    )
                    result = numbers_spell_map.get(new_number)
                    new_number = int(
                        len(
                            str(numbers_spell_map.get(hund))
                            + "hundred"
                            + str(numbers_spell_map.get(remainder))
                        )
                    )
                elif 20 <= remainder <= 99:
                    tens, remainder = divmod(remainder, 10)
                    print(
                        f"The word {numbers_spell_map.get(hund) + " " + "hundred"} {numbers_spell_map.get(tens*10) + '-' + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(tens*10)} has {len(str(numbers_spell_map.get(hund))+str(numbers_spell_map.get(tens*10) + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(tens*10)))} letters in it."
                    )
                    new_number = int(
                        len(
                            str(
                                numbers_spell_map.get(tens * 10)
                                + numbers_spell_map.get(remainder)
                                if remainder
                                else numbers_spell_map.get(tens * 10)
                            )
                        )
                    )
            else:
                print(
                    f"The word {numbers_spell_map.get(hund) + " " + "hundred"} has {len(str(numbers_spell_map.get(hund) + "hundred"))} letters in it."
                )
                result = numbers_spell_map.get(new_number)
                new_number = int(len(str(numbers_spell_map.get(hund) + "hundred")))
        elif 0 <= new_number <= 19:
            print(
                f"The word {numbers_spell_map.get(new_number)} has {len(str(numbers_spell_map.get(new_number)))} letters in it."
            )
            result = numbers_spell_map.get(new_number)
            new_number = int(len(str(numbers_spell_map.get(new_number))))
        elif 20 <= new_number <= 99:
            tens, remainder = divmod(new_number, 10)
            print(
                f"The word {numbers_spell_map.get(tens*10) + '-' + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(tens*10)} has {len(str(numbers_spell_map.get(tens*10) + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(tens*10)))} letters in it."
            )
            new_number = int(
                len(
                    str(
                        numbers_spell_map.get(tens * 10)
                        + numbers_spell_map.get(remainder)
                        if remainder
                        else numbers_spell_map.get(tens * 10)
                    )
                )
            )
    else:
        if 100 <= args.start_number <= 1000:
            hund, remainder = divmod(args.start_number, 100)
            if remainder:
                tens, remainder = divmod(remainder, 10)
                print(
                    f"The word {numbers_spell_map.get(hund) + " " + "hundred" + " " + numbers_spell_map.get(tens*10) + '-' + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(hund) + " " + "hundred" + " " + numbers_spell_map.get(tens*10)} has {len(str(numbers_spell_map.get(hund) + "hundred" + numbers_spell_map.get(tens*10) + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(hund) + "hundred" + numbers_spell_map.get(tens*10)))} letters in it."
                )
                new_number = int(
                    len(
                        str(
                            numbers_spell_map.get(hund)
                            + "hundred"
                            + numbers_spell_map.get(tens * 10)
                            + numbers_spell_map.get(remainder)
                            if remainder
                            else numbers_spell_map.get(hund)
                            + "hundred"
                            + numbers_spell_map.get(tens * 10)
                        )
                    )
                )
            else:
                print(
                    f"The word {numbers_spell_map.get(hund) + " " + "hundred"} has {len(str(numbers_spell_map.get(hund) + "hundred"))} letters in it."
                )

                result = numbers_spell_map.get(args.start_number)
                new_number = int(len(str(numbers_spell_map.get(hund) + "hundred")))
        elif 0 <= args.start_number <= 19:
            print(
                f"The word {numbers_spell_map.get(args.start_number)} has {len(str(numbers_spell_map.get(args.start_number)))} letters in it."
            )
            result = numbers_spell_map.get(args.start_number)
            new_number = int(len(str(numbers_spell_map.get(args.start_number))))
        elif 20 <= args.start_number <= 99:
            tens, remainder = divmod(args.start_number, 10)
            print(
                f"The word {numbers_spell_map.get(tens*10) + '-' + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(tens*10)} has {len(str(numbers_spell_map.get(tens*10) + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(tens*10)))} letters in it."
            )
            new_number = int(
                len(
                    str(
                        numbers_spell_map.get(tens * 10)
                        + numbers_spell_map.get(remainder)
                        if remainder
                        else numbers_spell_map.get(tens * 10)
                    )
                )
            )

    counter += 1

# if 100 <= args.start_number <= 1000:
#     hund, remainder = divmod(args.start_number, 100)
#     if remainder:
#         if 0 <= remainder <= 19:
#             print(
#                 f"The word {numbers_spell_map.get(hund) + " " + "hundred"} {numbers_spell_map.get(remainder)} has {len(str(numbers_spell_map.get(hund)) + "hundred" + str(numbers_spell_map.get(remainder)))} letters in it."
#             )
#             result = numbers_spell_map.get(remainder)
#             new_number = int(len(str(numbers_spell_map.get(hund)) + "hundred" + str(numbers_spell_map.get(remainder))))
#         elif 20 <= remainder <= 99:
#             tens, remainder = divmod(remainder, 10)
#             print(
#                 f"The word {numbers_spell_map.get(hund) + " " + "hundred"} {numbers_spell_map.get(tens*10) + '-' + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(tens*10)} has {len(str(numbers_spell_map.get(hund))+str(numbers_spell_map.get(tens*10) + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(tens*10)))} letters in it."
#             )
#             new_number = int(
#                 len(
#                     str(
#                         numbers_spell_map.get(tens * 10)
#                         + numbers_spell_map.get(remainder)
#                         if remainder
#                         else numbers_spell_map.get(tens * 10)
#                     )
#                 )
#             )
# tens, remainder = divmod(remainder, 10)
# print(hund, tens, remainder)
# print(numbers_spell_map.get(hund))
# print(numbers_spell_map.get(tens * 10))
# print(numbers_spell_map.get(remainder))
# print(
#     f"The word {numbers_spell_map.get(hund) + " " + "hundred" + " " + numbers_spell_map.get(tens*10) + '-' + numbers_spell_map.get(remainder) if remainder else numbers_spell_map.get(hund) + " " + "hundred" + " " + numbers_spell_map.get(tens*10)} has "
# )
# else:
#     print(
#         f"The word {numbers_spell_map.get(hund) + " " + "hundred"} has {len(str(numbers_spell_map.get(hund) + "hundred"))} letters in it."
#     )

# else:
#     tens, remainder = divmod(args.start_number, 10)
#     print(tens, remainder)
# print(len(str(args.start_number)))
print("Done.")

# The word one has 3 letters in it.
# The word three has 5 letters in it.
# The word five has 4 letters in it.
# The word four has 4 letters in it.
# Done.
# The word twenty has 6 letters in it.
# The word six has 3 letters in it.
# The word three has 5 letters in it.
# The word five has 4 letters in it.
# The word four has 4 letters in it.
# Done.
