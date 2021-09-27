if __name__ == "__main__":
    sum = 0
    nums = input("Hello, please enter two or more numbers seperated by spaces:\t").split()
    if len(nums) < 2:
        print("Error: Atleast 2 numbers required")
        raise SyntaxError
    for elems in nums:
        try:
            sum += eval(elems)
        except:
            print("Error: Unexpected character detected")
            raise
    print(sum)

