def fizz_buzz(limit):
    for i in range(1, limit+1):
        if i % 5 == 0:
            print('fizz')
            if i % 3 == 0:
                print('buzz')

def main():
    import sys
    t = int(sys.argv[1])
    fizz_buzz(t)

main()
