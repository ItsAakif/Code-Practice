def repeared_multiplication(base, exp):
    if exp == 0:
        return 1
    else:
        return base * repeared_multiplication(base, exp -1)
def main():
    print(repeared_multiplication(3,4))
main()