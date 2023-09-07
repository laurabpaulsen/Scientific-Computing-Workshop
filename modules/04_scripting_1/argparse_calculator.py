from calculator import calculate
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", help="The first number", type=float)
    parser.add_argument("--second", help="The second number", type =float)
    parser.add_argument("--operator", help="The operator")
    
    return parser.parse_args()

def main():
    args = parse_args()
    output = calculate(args.first, args.second, args.operator)
    print(output)

if __name__ in "__main__":
    main()
