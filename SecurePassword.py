class BinaryOperations:

    def __init__(self, binary) -> None:
        self.binary = binary

    def bin_to_den(self):
        power = len(self.binary) - 1
        denary = 0
        for i in self.binary:
            if i == "1":
                denary += 2**power
            power -= 1
        return denary

    # Resource:
    # https://www.youtube.com/watch?v=m_08FbT0_WY
    # Video shows how to rotate right with no code
    def rotate_right(self, amount):
        right_most_bin = self.binary[-amount:]
        rotated_bin = right_most_bin + self.binary[:-amount]
        return rotated_bin

    # Resource:
    # https://byjus.com/gate/right-shift-operator-in-c/
    # Website that teaches right shift with code
    def right_shift(self, amount):
        significant_bin = self.binary[:-amount]
        shifted_bin = "0" * amount + significant_bin
        return shifted_bin

    def split_binary(self, amount):
        lst = []
        for i in range(0, len(self.binary) + 1, amount):
            if i != len(self.binary):
                start_position = i
                end_position = amount + i
                lst.append(self.binary[start_position:end_position])
        return lst

    # This function only works when length of binary is divisible by 4
    # Since sha-256 always return a 256 binary and 256 % 4 == 0
    # The function does not need to be more complex
    def bin_to_hexadecimal(self):
        hexa_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        key_lst = list(hexa_dict.keys())
        val_lst = list(hexa_dict.values())
        lst = self.split_binary(4)
        answer = []
        for i in lst:
            base_power = 8
            store = 0
            for j in i:
                if j == "1":
                    store += base_power
                base_power //= 2
            if store >= 10:
                position = val_lst.index(store)
                get_key = key_lst[position]
                answer.append(get_key)
            else:
                answer.append(str(store))
        return "".join(answer)


# The class SecurePassword is a simplified version
# of sha-256 that only handles up to 512 bits not anything
# above that to reduce complexity
# Resource:
# https://www.youtube.com/watch?v=orIgy2MjqrA
# The video breaks down SHA-256 algorithm with no code
class SecurePassword:

    # A table of 64 constants each representing
    # the first 32 bits of the cube roots
    # of the first 64 primes
    K = [
        "01000010100010100010111110011000",
        "01110001001101110100010010010001",
        "10110101110000001111101111001111",
        "11101001101101011101101110100101",
        "00111001010101101100001001011011",
        "01011001111100010001000111110001",
        "10010010001111111000001010100100",
        "10101011000111000101111011010101",
        "11011000000001111010101010011000",
        "00010010100000110101101100000001",
        "00100100001100011000010110111110",
        "01010101000011000111110111000011",
        "01110010101111100101110101110100",
        "10000000110111101011000111111110",
        "10011011110111000000011010100111",
        "11000001100110111111000101110100",
        "11100100100110110110100111000001",
        "11101111101111100100011110000110",
        "00001111110000011001110111000110",
        "00100100000011001010000111001100",
        "00101101111010010010110001101111",
        "01001010011101001000010010101010",
        "01011100101100001010100111011100",
        "01110110111110011000100011011010",
        "10011000001111100101000101010010",
        "10101000001100011100011001101101",
        "10110000000000110010011111001000",
        "10111111010110010111111111000111",
        "11000110111000000000101111110011",
        "11010101101001111001000101000111",
        "00000110110010100110001101010001",
        "00010100001010010010100101100111",
        "00100111101101110000101010000101",
        "00101110000110110010000100111000",
        "01001101001011000110110111111100",
        "01010011001110000000110100010011",
        "01100101000010100111001101010100",
        "01110110011010100000101010111011",
        "10000001110000101100100100101110",
        "10010010011100100010110010000101",
        "10100010101111111110100010100001",
        "10101000000110100110011001001011",
        "11000010010010111000101101110000",
        "11000111011011000101000110100011",
        "11010001100100101110100000011001",
        "11010110100110010000011000100100",
        "11110100000011100011010110000101",
        "00010000011010101010000001110000",
        "00011001101001001100000100010110",
        "00011110001101110110110000001000",
        "00100111010010000111011101001100",
        "00110100101100001011110010110101",
        "00111001000111000000110010110011",
        "01001110110110001010101001001010",
        "01011011100111001100101001001111",
        "01101000001011100110111111110011",
        "01110100100011111000001011101110",
        "01111000101001010110001101101111",
        "10000100110010000111100000010100",
        "10001100110001110000001000001000",
        "10010000101111101111111111111010",
        "10100100010100000110110011101011",
        "10111110111110011010001111110111",
        "11000110011100010111100011110010",
    ]

    def __init__(self, password) -> None:
        self.password = password

    # staticmethod decorators are used because they rely solely
    # on the argument given to them and are independant of the class
    # # Resource:
    # https://www.bbc.co.uk/bitesize/guides/zd88jty/revision/3
    # Website that teaches an easier way to convert
    # from denary to binary
    @staticmethod
    def den_to_bin(denary):
        binary = ""
        if denary == 0:
            return "0"
        while denary > 0:
            if denary % 2 == 1:
                binary += "1"
            else:
                binary += "0"
            denary //= 2
        return binary[::-1]

    # *arguments is used to take in multiple values
    @staticmethod
    def xor(*arguments):
        # Binary addition followed by mod 2 is equivalent to XOR
        binary = ""
        for i in range(len(arguments[0])):
            add = 0
            for j in range(len(arguments)):
                add += int(arguments[j][i])
            binary += str(add % 2)
        return binary

    @staticmethod
    def sigma_zero(binary):
        instance = BinaryOperations(binary)
        rotate_seven = instance.rotate_right(7)
        rotate_eighteen = instance.rotate_right(18)
        right_three = instance.right_shift(3)
        answer = SecurePassword.xor(rotate_seven, rotate_eighteen, right_three)
        return answer

    @staticmethod
    def sigma_one(binary):
        instance = BinaryOperations(binary)
        rotate_seventeen = instance.rotate_right(17)
        rotate_nineteen = instance.rotate_right(19)
        right_ten = instance.right_shift(10)
        answer = SecurePassword.xor(rotate_seventeen, rotate_nineteen, right_ten)
        return answer

    @staticmethod
    def capital_sigma_zero(binary):
        instance = BinaryOperations(binary)
        rotate_two = instance.rotate_right(2)
        rotate_thirteen = instance.rotate_right(13)
        rotate_twenty_two = instance.rotate_right(22)
        answer = SecurePassword.xor(rotate_two, rotate_thirteen, rotate_twenty_two)
        return answer

    @staticmethod
    def capital_sigma_one(binary):
        instance = BinaryOperations(binary)
        rotate_six = instance.rotate_right(6)
        rotate_eleven = instance.rotate_right(11)
        rotate_twenty_five = instance.rotate_right(25)
        answer = SecurePassword.xor(rotate_six, rotate_eleven, rotate_twenty_five)
        return answer

    # The choose function takes in three binary numbers
    # If the binary of the first number is "0"
    # Then the binary of the third number is stored
    # Else, the binary of the second number is stored
    @staticmethod
    def choose(e, f, g):
        binary = ""
        for i in range(len(e)):
            if e[i] == "0":
                binary += g[i]
            else:
                binary += f[i]
        return binary

    # The majority function takes in three binary numbers
    # It checks all the binary in the same position for the three numbers
    # Eg. "0" , "1" , "0" -> "0" is stored because it appears more
    @staticmethod
    def majority(a, b, c):
        binary = ""
        for i in range(len(a)):
            add = int(a[i]) + int(b[i]) + int(c[i])
            if add >= 2:
                binary += "1"
            else:
                binary += "0"
        return binary

    # Does not take into account of overflows
    # This helps to ensure the answer will always be 32 bit
    @staticmethod
    def binary_addition(num1, num2):
        carry = False
        binary = ""
        for i in range(len(num1) - 1, -1, -1):
            add = int(num1[i]) + int(num2[i])
            if carry:
                add += 1
            if add >= 2:
                carry = True
            else:
                carry = False
            if add == 3:
                binary += "1"
            elif add == 2:
                binary += "0"
            else:
                binary += str(add)
        return binary[::-1]

    # Defined as Wt
    def make_msg_schedule(self, binary):
        instance = BinaryOperations(binary)
        # From Wt = 0 to Wt = 15, no changes are needed
        message_schedule = instance.split_binary(32)
        # Message schedule must be from Wt = 0 to Wt = 63
        for i in range(16, 64):
            word_t_minus_two = message_schedule[i - 2]
            word_t_minus_seven = message_schedule[i - 7]
            word_t_minus_fifteen = message_schedule[i - 15]
            word_t_minus_sixteen = message_schedule[i - 16]
            # The formula is
            # Wt = σ1(Wt-2) + Wt-7 + σ0(Wt-15) + Wt-16
            formula = (
                SecurePassword.sigma_one(word_t_minus_two)
                + word_t_minus_seven
                + SecurePassword.sigma_zero(word_t_minus_fifteen)
                + word_t_minus_sixteen
            )
            instance = BinaryOperations(formula)
            # After this modulo 2^32 is needed for 32-bit length
            mod_formula = SecurePassword.den_to_bin(instance.bin_to_den() % (2**32))
            # Adding some front 0 padding to ensure it is 32 bit long
            pad_formula = "0" * (32 - len(mod_formula)) + mod_formula
            message_schedule.append(pad_formula)
        return message_schedule

    def compute_msg_schedule(self, msg_schedule):
        initial_hash_values = [
            "01101010000010011110011001100111",
            "10111011011001111010111010000101",
            "00111100011011101111001101110010",
            "10100101010011111111010100111010",
            "01010001000011100101001001111111",
            "10011011000001010110100010001100",
            "00011111100000111101100110101011",
            "01011011111000001100110100011001",
        ]
        a, b, c, d, e, f, g, h = initial_hash_values
        binary = ""
        for t in range(63):
            sigma_e = SecurePassword.capital_sigma_one(e)
            choose_vals = SecurePassword.choose(e, f, g)
            # Formula is
            # T1 = (h + Σ(e) + Ch(e,f,g) + K[t] + W[t]) mod 2
            t_one = SecurePassword.xor(
                h, sigma_e, choose_vals, SecurePassword.K[t], msg_schedule[t]
            )
            sigma_a = SecurePassword.capital_sigma_zero(a)
            major = SecurePassword.majority(a, b, c)
            # Formula is
            # T2 = (Σ(a) + Maj(a,b,c)) mod 2
            t_two = SecurePassword.xor(sigma_a, major)
            h = g
            g = f
            f = e
            e = SecurePassword.binary_addition(d, t_one)
            d = c
            c = b
            b = a
            a = SecurePassword.binary_addition(t_one, t_two)
        # Updating all the initial hash values
        initial_hash_values[0] = SecurePassword.binary_addition(
            initial_hash_values[0], a
        )
        initial_hash_values[1] = SecurePassword.binary_addition(
            initial_hash_values[1], b
        )
        initial_hash_values[2] = SecurePassword.binary_addition(
            initial_hash_values[2], c
        )
        initial_hash_values[3] = SecurePassword.binary_addition(
            initial_hash_values[3], d
        )
        initial_hash_values[4] = SecurePassword.binary_addition(
            initial_hash_values[4], e
        )
        initial_hash_values[5] = SecurePassword.binary_addition(
            initial_hash_values[5], f
        )
        initial_hash_values[6] = SecurePassword.binary_addition(
            initial_hash_values[6], g
        )
        initial_hash_values[7] = SecurePassword.binary_addition(
            initial_hash_values[7], a
        )
        for i in initial_hash_values:
            binary += i
        return binary

    # 55 is the upper limit for password length
    def secure(self):
        sha_binary = ""
        for i in self.password:
            bin_ascii = self.den_to_bin(ord(i))
            pad_ascii = (8 - len(bin_ascii)) * "0" + bin_ascii
            sha_binary += pad_ascii
        initial_bin = self.den_to_bin(len(sha_binary))
        # Makes the binary to length of 448
        # 55 * 8 = 440 so anything > 55 will have binary length
        # > 448 hence 55 being the upper limit
        sha_binary += "1" + (448 - len(sha_binary) - 1) * "0"
        # Makes the binary to length of 512
        sha_binary += (64 - len(initial_bin)) * "0" + initial_bin
        message_schedule = self.make_msg_schedule(sha_binary)
        password_hashed = self.compute_msg_schedule(message_schedule)
        instance = BinaryOperations(password_hashed)
        return instance.bin_to_hexadecimal()
