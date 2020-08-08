
# Reader imports
from codesummary import *

# disable warnings
import warnings
warnings.filterwarnings("ignore")


def main():  # type: () -> None
    path = input('enter path: ')
    print('start analysis to ' + path )
    doSummary(path)

if __name__ == "__main__":
    main()
