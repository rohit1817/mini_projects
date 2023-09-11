def num_to_text(num):
    ones=['zero','one','two','three','four','five','six','seven','eight','nine','ten']
    teens=['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']             
    digits = [int(num) for num in str(num)]   #1,2,3,4

    if num <10:
        print(ones[num])
    elif num <20:
        print(teens[num-10])
    elif num <100:
        print(tens[digits[0]] + " " + ones[digits[1]])
    elif num <1000:
        print(f"{ones[digits[0]]} hundred {tens[digits[1]]} {ones[digits[2]]}")
    if len(digits) == 4:
        if digits[2]==1:
            print(f"{ones[digits[0]]} thousands {ones[digits[1]]} hundred {teens[digits[3]]}")
        else:    
            print(f"{ones[digits[0]]} thousands {ones[digits[1]]} hundred {tens[digits[2]]} {ones[digits[3]]}")
    if len(digits) == 5:
        if digits[0]==1:
            if digits[3]==1:
                print(f"{teens[digits[1]]} thousand {ones[digits[2]]} hundred {teens[digits[4]]}")
            else:
                print(f"{teens[digits[1]]} thousand {ones[digits[2]]} hundred {tens[digits[3]]} {ones[digits[4]]}")
        else:
            print(f"{tens[digits[0]]} {ones[digits[1]]} thousand {ones[digits[2]]} hundred {tens[digits[3]]} {ones[digits[4]]}")
                
                
            
num_to_text(22325)
num_to_text(12345)
num_to_text(12312)