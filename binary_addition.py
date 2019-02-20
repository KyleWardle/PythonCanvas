bits = 16


def input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input


class Binary:
    def __init__(self, integer: int = None):
        self.binary_value = self.convert_int_to_binary(integer) if integer is not None else None

    def from_binary(self, binary: str):  # init from binary as opposed to an integer
        self.binary_value = self.allocate_bits(binary[::-1])[::-1]
        return self

    def __str__(self):
        return self.binary_value

    def __len__(self):
        return len(self.binary_value)

    def __add__(self, other):
        first = list(self.binary_value[::-1])  # flips both around to work with left to right rather than opposite
        second = list(other.binary_value[::-1])

        final_added = ""
        carry = False

        for i in range(0, len(first)):
            added_val = int(first[i]) + int(second[i])
            if carry:
                added_val = added_val + 1

            if added_val == 0 or added_val == 1:
                final_added = final_added + str(added_val)
                carry = False
            else:
                final_added = final_added + str(added_val - 2)
                carry = True

        return Binary().from_binary(final_added[::-1])

    def __sub__(self, other):
        return self + (- other)

    def __mul__(self, other):
        other_value_reversed = list(other.binary_value[::-1])
        total = Binary(0)
        for i in range(1, len(other_value_reversed) + 1):
            binary_val = int(self.binary_value) * int(other_value_reversed[i - 1]) * int(10 ** (i - 1))
            total = total + Binary().from_binary(str(binary_val))
        return total

    def __ge__(self, other):
        return self.denary() >= other.denary()  # I know this isn't ideal but will come back around to it.

    def __le__(self, other):
        return self.denary() <= other.denary()

    def __truediv__(self, divisor):
        dividend = self.binary_value
        cur_div = ""
        answer = ""

        for i in range(0, len(dividend)):
            cur_div = cur_div + dividend[i]
            if divisor <= Binary().from_binary(cur_div):
                answer = answer + "1"
                take_away = divisor * Binary().from_binary(answer)
                cur_div = (Binary().from_binary(cur_div) - take_away).binary_value

            else:
                answer = answer + "0"

        print(answer)
        answer = Binary().from_binary(answer)
        print(answer.denary())
        return self

    def __neg__(self):
        return self.change_state()

    def denary(self):
        binary = list(self.binary_value)  # flips string
        value = 0
        if binary[0] == "1":
            binary = list(self.change_state().binary_value[::-1])
            for i in range(0, len(binary) - 1):
                value += ((2 ** i) * int(binary[i]))
            return -int(value)
        elif binary[0] == "0":
            binary = list(self.binary_value[::-1])
            for i in range(0, len(binary) - 1):
                value += ((2 ** i) * int(binary[i]))
            return int(value)

    def convert_int_to_binary(self, number):
        neg = False
        if number < 0:
            neg = True
        binary = self.positive_binary_convert(abs(number))
        if neg:
            binary = binary.change_state()
        return binary.binary_value

    def positive_binary_convert(self, integer):
        before = ""
        finished = False
        while not finished:
            divided = int(int(integer) / 2)
            remainder = int(integer) % 2
            before = before + str(remainder)
            integer = divided
            if divided == 0:
                finished = True
        before = self.allocate_bits(before)
        binary = before[::-1]  # Flips the string
        return Binary().from_binary(binary)

    def change_state(self, binary=None):  # Change from negative to positive
        if binary is not None:
            flipped = Binary().from_binary(binary).flip_bits()
        else:
            flipped = self.flip_bits()

        return flipped + Binary(1)

    @staticmethod
    def allocate_bits(value):
        length = len(value)
        if length < bits:
            rem = bits - length
        else:
            rem = length % bits
        for i in range(0, rem):
            value = value + "0"
        return value

    def flip_bits(self):
        binary_list = list(self.binary_value)

        for i in range(0, len(self.binary_value)):
            binary_list[i] = "1" if binary_list[i] == "0" else "0"
        binary = "".join(binary_list)
        return Binary().from_binary(binary)


def test():
    print("Passed" if (Binary(5) + Binary(10)).denary() == 15 else "Failed")
    print("Passed" if (Binary(125) + Binary(125)).denary() == 250 else "Failed")
    print("Passed" if (Binary(5) - Binary(10)).denary() == -5 else "Failed")
    print("Passed" if (Binary(255) - Binary(120)).denary() == 135 else "Failed")
    print("Passed" if (Binary(4) * Binary(5)).denary() == 20 else "Failed")
    print("Passed" if (Binary(125) * Binary(1000)).denary() == 125000 else "Failed")


def main():
    test123 = Binary(12) / Binary(2)
    # print(test123)
    # sum_type = str(input("What do you want to do (add, take, divide, multiply)? "))
    #
    # first_denary = input_number("Enter your first Integer: ")
    # first_binary = Binary(first_denary)
    # print(first_binary)
    #
    # second_denary = input_number("Enter your second Integer: ")
    # second_binary = Binary(second_denary)
    # print(second_binary)
    #
    # print("--------")
    #
    # if sum_type in ["add", "+"]:
    #     calculated = first_binary + second_binary
    # elif sum_type in ['take', '-']:
    #     calculated = first_binary - second_binary
    # elif sum_type in ['multiply', 'times', 'x', '*']:
    #     calculated = first_binary * second_binary
    # else:
    #     calculated = None
    #     main()
    #
    # print(calculated)
    # print("--------")
    # print(calculated.denary())
    #
    # try_again = str(input("Do you want to try again? "))
    # if try_again.lower() in ["yes", "y", "yea"]:
    #     main()
    # else:
    #     print("Thanks.")


# test()

main()
