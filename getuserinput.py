#try get user input with the inf. arg parameter

def main():
    def sum(*kwargs):
        total = 0;
        for v in kwargs:
            total += v
        return total
    print(sum(1,2,3,4,6,7,8,9))
    
if __name__ == "__main__" :
    main()