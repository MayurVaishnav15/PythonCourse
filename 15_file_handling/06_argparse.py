import argparse
parser = argparse.ArgumentParser(description="Simple Calculator :-")

parser.add_argument("num1",type=float,help ="First Number")
parser.add_argument("num2",type=float,help="Second Number")
parser.add_argument("Operation",choices=["add","sub","mul","div"],help="Operation to Perform")
args = parser.parse_args()
print(args)

if args.Operation == "add":
    print(f"The result is {args.num1 + args.num2}")
if args.Operation == "sub":
    print(f"The result is {args.num1 - args.num2}")
if args.Operation == "mul":
    print(f"The result is {args.num1 * args.num2}")
if args.Operation == "div ":
    print(f"The result is {args.num1 / args.num2}")