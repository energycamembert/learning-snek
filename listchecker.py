# Program to check for missing items in the lists
# This can be used to check for missing files (f.e. client requests a list of photographs to edit and you need to double check all the edits are in the folder)

#energycamembert 2023


def main():

    # Two lists to be checked against each other
    files_demand = ['DSC101', 'DSC102', 'DSC103', 'DSC104', 'DSC105', 'DSC106']
    files_input = ['DSC101', 'DSC102', 'DSC107', 'DSC104', 'DSC106']
   
    print("Demanded list has", len(files_demand), "files.")
    print("Submitted list has", len(files_input), "files.")

    # Check for number of list elements to iterate for
    
    number_elements = 0
        
    if len(files_demand) > len(files_input):
        number_elements = len(files_demand)
    elif len (files_demand) <= len(files_input):
        number_elements = len(files_input)

    print("Number of elements to check:", number_elements)

    missing_elements = []
    n_missing_elements = 0

   # FOR -> picks demanded element from the list
   # WHILE -> searches the other list for this specific element

    i = 0
    for i in range(number_elements):
        
        #iterator comparing elements
        cache = 0
        match_found = False
        #print("For loop",i)

        # If demanded name match is found, match_found will switch to True
        #
        while cache != len(files_input):
                            
            if files_demand[i] == files_input[cache]:
                match_found = True
                print ("Match found = True")
                cache = cache +1
                print("Match:", files_demand[i])

            else:
                cache = cache +1
            
        # If at the end of the checker loop match_found still is False, the file is considered missing.
        #
        if match_found is False:
            print("Match_found = False")
            print("Missing element:", files_demand[i])
            n_missing_elements = n_missing_elements +1
            missing_elements.append(files_demand[i])
      
    # End prints

    print("\nMissing elements:", missing_elements)
    print("Number of missing elements:", n_missing_elements)

            

main()
