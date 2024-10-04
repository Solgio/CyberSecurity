print("Inserisci il primo numero: ")
input1=input()
print("Inserisci un operatore (+, -, *, /, %, ^, rad): ")
operator=input()
print("Inserisci il secondo numero: ")
input2=input()

match operator:
    case "+":
        print( input1," + ", input2, " = ", int(input1)+int(input2))
        
    case "-":
        print( input1," - ", input2, " = ", int(input1)-int(input2))
         
    case "*":
        print( input1," * ", input2, " = ", int(input1)*int(input2))
         
    case "/":
        print( input1," / ", input2, " = ", int(input1)/int(input2))
    
    case "%":
        print( input1," % ", input2, " = ", int(input1)%int(input2))
        
    case "^":
        print( input1," ^ ", input2, " = ", int(input1)**int(input2))
        
    case "rad":
        print( "rad(", input2, ")", "di ", input1, " = ", int(input1)**(1/int(input2)))
        