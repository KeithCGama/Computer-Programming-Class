def calculate_sum(number, product):
    #Changed += to *=, because
    #+= is a logic error
    #Program is expected to multiply the numbers
    product *= number
    
    return product

def main():
    #add colon after try
    try:
        numbers = [1, 2, 3, 4, 5, 6]
        #addes missing assignment operator
        product = 1
        
        for number in numbers:
            #change function name 
            product = calculate_sum(number, product)
        print(f'The product of the numbers is: {product}')

        #Chnaged index index from 6 to 5
        #list index range is 0-5
        print(f'The last number multipled was: {numbers[5]}')
     #added colon after e:   
    except IndexError as e:
        print(f'Run-time error: {e}')

if __name__ == '__main__':
    main()

    print("Debbuged, Completed by, Keith")
