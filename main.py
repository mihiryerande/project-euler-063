# Problem 63:
#     Powerful Digit Counts
#
# Description:
#     The 5-digit number, 16807 = 7^5, is also a fifth power.
#     Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.
#
#     How many n-digit positive integers exist which are also an n'th power?

from math import ceil, floor, log10


def main():
    """
    Returns the count of positive integers
      which are each n-digits and an n'th power.

    Returns:
        (int): Count of n-digit numbers which are also n'th powers.
    """

    # Problem:
    #     Want to count all `x` such that
    #       x is `n` digits, and
    #       x is an n'th power, for some n.
    #     Let x = b^n, for some b and n.

    # Idea 1:
    #     Suppose we are given some `n`.
    #     For x to be an n-digit number, we must have:
    #         10^(n-1) ≤ x = b^n < 10^n
    #
    #     What are the possible values of `b`?
    #       * b must be positive
    #           => 0 < b
    #       * b^n < 10^n
    #           => b < 10
    #
    #     Most simple bounds:
    #         0 < b < 10
    #
    #     Also must satisfy the following:
    #            10^(n-1) ≤ b^n
    #         => (10^(n-1))^(1/n) ≤ (b^n)^(1/n)
    #         => 10^((n-1)/n) ≤ b
    #
    #     Thus we have:
    #         10^((n-1)/n) ≤ b < 10
    #

    # Idea 2:
    #     What are the possible values of `n`?
    #     As n increases, the lower bound on b also increases.
    #     Find n such that there is no longer any possible range for b.
    #
    #     This happens when:
    #         10^((n-1)/n) > 9
    #
    #     Solving for bound on n:
    #            10^((n-1)/n) > 9
    #         => log10(10^((n-1)/n)) > log10(9)
    #         => (n-1)/n > log10(9)
    #         => n-1 > n*log10(9)
    #         => n - n*log10(9) > 1
    #         => n*(1-log10(9)) > 1
    #         => n > 1/(1-log10(9))
    #
    #     Thus we have:
    #         1 ≤ n ≤ 1/(1-log10(9))
    #

    count = 0
    n_max = floor(1/(1-log10(9))) + 1
    for n in range(1, n_max):
        b_min = ceil(10 ** ((n - 1) / n))
        count += 10 - b_min

        # for b in range(b_min, 10):
        #     x = b ** n
        #     print('{}^{} = {} ({} digits)'.format(b, n, x, len(str(x))))
    return count


if __name__ == '__main__':
    powerful_number_count = main()
    print('Count of n-digit numbers which are n\'th powers:')
    print('  {}'.format(powerful_number_count))
