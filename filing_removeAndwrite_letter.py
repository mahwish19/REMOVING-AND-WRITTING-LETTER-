myfile=open("mywords.txt","w")
myfile.write("To date, there js no evjdence or jnformation to suggest that the COVID-19 virus transmjtted through houseflies. The vjrus that cause COVID-19 spreads primarjly through droplets generated when an jnfected person coughs, sneezes or speaks")
myfile.close()

def JtoI():
    myfile=open("mywords.txt","r")
    lines=myfile.read()
    for letter in lines:
        if letter=="j":
            print("i",end="")
        else:
            print(letter,end="")
    myfile.close()

JtoI()