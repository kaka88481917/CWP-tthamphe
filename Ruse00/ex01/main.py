import sys
from checkmate import checkmate

def main():
    file = sys.argv[1:]
    for path in file:
        try:
            with open(path, 'r') as f:
                content = f.read()
                checkmate(content)
        except FileNotFoundError:
            print("Error")

if __name__ == "__main__":
    main()