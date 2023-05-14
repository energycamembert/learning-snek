## Vowel Counter
## Assigned by ChatGPT
#
##Sure! Here's a simple programming exercise where you can apply the concepts you mentioned:
## Exercise: Vowel Counter
#
## Write a program that takes a sentence as input from the user and counts the number of vowels (a, e, i, o, u) in the sentence. The program should then print the total count of vowels.


def main():


    RESET = "\033[0m"
    GREEN = "\033[31m"

    vow_total = 0
    vowa = 0
    vowe = 0
    vowi = 0
    vowo = 0
    vowu = 0

    print(GREEN + "VOWEL COUNTER" +  RESET)
    string = input("Please enter a sentence: ")

    for _ in range(len(string)):
        if string[_] == "a":
            vowa = vowa +1
        elif string[_] == "e":
            vowe = vowe +1
        elif string[_] == "i":
            vowi = vowi +1
        elif string[_] == "o":
            vowo = vowo +1
        elif string[_] == "u":
            vowu = vowu +1
    
    print("\n")
    print(f"Vowel A: {vowa}")
    print(f"Vowel E: {vowe}")
    print(f"Vowel I: {vowi}")
    print(f"Vowel O: {vowo}")
    print(f"Vowel U: {vowu}")
    print("______________")

    vow_total = vowa + vowe + vowi + vowo + vowu
    print("Vowels found (total): ",vow_total )

main()