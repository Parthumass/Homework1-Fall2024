"""
ECE241 Fall 2024 - Homework1 Question2
"""

class Question2:
    @staticmethod
    def solveMonomial(a, b, c):
        """

        :param a:
        :param b:
        :param c:
        :return:
        """
        # fill in your logic here

        return -1

    @staticmethod
    def solvePolynomial(a, b, c):
        """

        :param a:
        :param b:
        :param c:
        :return:
        """
        # fill in your logic here

        return -1

    @staticmethod
    def autograder():
        monomial_result = "REPLACE_WITH_YOUR_RESULT_HERE"
        polynomial_result = "REPLACE_WITH_YOUR_RESULT_HERE"

        # Do NOT change the code below!
        return {
           "monomial": int(monomial_result),
            "polynomial": int(polynomial_result)
        }


if __name__ == "__main__":
    # Note: the following code is for local debugging only.
    # The result is NOT going to be graded by the autograder!
    # You need to have correct solving logic to get full marks!
    print(Question2.solveMonomial(1, 1, 4))
    print(Question2.solvePolynomial(1, 1, 4))

