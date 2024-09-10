# One way of import packages is by calling the whole package and access the function
# by something like "utility.multiply()"
# import utility

# Another way is to simply import the function from the package and
# use the function as it was created here.
from utility import multiply, divide

from shopping.more_shopping.shopping_cart import addToCart

print(__name__)

# __name__ returns the name of the file.
# __main__ is the file that is being run.
if __name__ == '__main__':

    print(multiply(2, 5))
    print(divide(20, 5))

    print(addToCart('sneakers'))
