class Bignum:
    """Representation of arbitrary precision integer.

    self.digits    : Low significant digit is first and high significant
                     digit is last.
    self.lastdigit : Index of most significant (last) digit in self.digits
    self.signbit   : Sign PLUS == 1 for positive and MINUS == -1 for negative
    """

    PLUS, MINUS, MAXDIGITS = 1, -1, 100

    def __init__(self):
        """Instanciate a big num with at most `maxdigits` digits."""
        self.digits = [0] * MAXDIGITS
        self.signbit = Bignum.PLUS
        self.lastdigit = 0

    def __str__(self):
        """String representation of Bignum instance."""
        s = ''
        if self.signbit == Bignum.MINUS:
            s = '- '

        for d in reversed(self.digits[:lastdigit]):
            s += s + str(d)

        return s


    # Rich comparison functions

    def _compare_bignum(self, other):
        """Return PLUS, MINUS, 0 respectively if self <, > or == other."""
        if self.signbit == MINUS and other.signbit == PLUS:
            return PLUS
        if self.signbit == PLUS and other.signbit == MINUS:
            return MINUS

        if other.lastdigit > self.lastdigit:
            return PLUS * self.signbit
        if self.lastdigit  > other.lastdigit:
            return MINUS * self.signbit

        return 0

    def __lt__(self, other):
        return self._compare_bignum(other) == PLUS

    def __gt__(self, other):
        return self._compare_bignum(other) == MINUS

    def __eq__(self, other):
        return self._compare_bignum(other) == 0

    def __lte__(self, other):
        return not self > other

    def __gte__(self, other):
        return not self < other

    def __bool__(self):
        """True if non nul."""
        return self.lastdigit > 0 or self.digits[0] > 0

    # Arithmetic operations
    def _zero_justify(self):
        """Adjust self.lastdigit to avoid leading zeros."""
        while self.lastdigit > 0 and self.digits[lastdigit] == 0:
            self.lastdigit -= 1

        # avoid -0
        if self.lastdigit == 0 and self.digits[0] == 0:
            self.signbit = PLUS


    def _shift_digits(self, n):
        """Self = self * 10^n."""
        if not self: # self == 0
            return

        for i in reversed(range(self.lastdigit+1)):
            self.digits[i+n] = self.digits[i]

        for i in range(n):
            self.digits[i] = 0

        self.lastdigit += n

    def __copy__(self):
        n = Bignum()
        n.signbit = self.signbit
        n.lastdigit = self.lastdigit
        n.digits = self.digits.copy()

        return n


    def __add__(self, other):
        if self.signbit != other.signbit:
            if self.signbit == MINUS: # self is negative: ans = other - self
                self.signbit = PLUS
                ans = other - self
                self.signbit = MINUS
            else: # b is negative, ans = self - other
                other.signbit = PLUS
                ans = self - other
                other.signbit = MINUS
            ans._zero_justify()
            return ans

        # self and other have same sign
        ans = Bignum()
        ans.signbit = self.signbit
        ans.lastdigit = max(self.lastdigit, other.lastdigit)+1
        carry = 0

        for i in range(ans.lastdigit+1):
            ans.digits[i] = (self.digits[i] + other.digits[i] + carry) % 10
            carry         = (self.digits[i] + other.digits[i] + carry) // 10

        ans._zero_justify()

        return ans


    def __sub__(self, other):
        if self.signbit == MINUS or other.signbit == MINUS:
            other.signbit = -1 * other.signbit
            ans = self + other
            other.signbit = -1 * other.signbit
            ans._zero_justify()
            return ans

        if self < other:
            ans = other - self
            ans.signbit = MINUS

        # self >= other: do self - other
        ans = Bignum()
        ans.lastdigit = max(self.lastdigit, other.lastdigit)
        borrow = 0
        for i in range(ans.lastdigit+1):
            tmp = self.digits[i] - borrow - other.digits[i]
            if self.digits[i] > 0:
                borrow = 0
            if tmp < 0:
                tmp += 10
                borrow = 1
            ans.digits[i] = tmp % 10

        ans._zero_justify()

        return ans

    def __mult__(self, other):
        ans = Bignum()
        row = self.__copy__() # represent shifted row

        for d in b.digits[:lastdigit+1]:
            for _ in range(d):
                ans += row
            row._shift_digits(1)

        ans.signbit = self.signbit * other.signbit

        ans._zero_justify()
        return ans

    def __div__(self, other):
        ans = Bignum()
        ans.signbit = self.signbit * other.signbit

        self_sign, other_sign = self.signbit, other.signbit

        self.signbit, other.signbit = PLUS, PLUS

        row = Bignum()  # represent shifted row

        for i in reversed(range(self.lastdigit+1)):
            row._shift_digits(1)
            row.digits[0] = self.digits[i]
            ans.digits[i] = 0
            while row > other:
                ans.digits[i] += 1
                row = row - b


        self.signbit, other.signbit = self_sign, other_sign

        ans._zero_justify()
        return ans
