# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil

# CMPT 116/141 - Matryoshka Dolls


chest1 = {
    "Dafna" : ["Vera", "Lada", "Alla","Zoe"],
    "Yana" : ["Zoe"],
    "Vera" : ["Inga"],
    "Alla" : ["Zoe"]
}
chest2 = {
    "Dina" : ["Zlata","Olga"],
    "Erene" : ["Veronika","Olga","Zlata","Nina"],
    "Veronika" : ["Zlata","Olga"],
    "Zlata" : ["Olga"],
    "Tamara" : ["Olga"],
}



def maximum(chest,doll_name):
    """
    determines the maximum number in a set of matyoshka dolls whose outermost doll’s name is given
    :param chest: The python dictionary containing the information about doll containment in the indicated chest
    :param doll_name: Name of the outermost doll.
    :return: The maximum number of dolls in a set of matyoshka dolls, that can be formed from dolls in the given chest,
    whose outermost doll has the given name.
    """

    if not doll_name in chest:
        return 1
    for i in chest[doll_name]:
        if i in chest:
            return maximum(chest,i) + 1
        else:
            return 2

def fuction_call(chest):
    """
    prints the maximum number in a set of matyoshka dolls, that includes at least two dolls, for each outermost doll in
    the given chest.
    :param chest: The python dictionary containing the information about doll containment in the indicated chest
    :return:None
    """

    for i in chest:
        max_i = maximum(chest,i)
        if  max_i >= 2:
            print("The maximum size of a set Matyoshka Dolls with outermost doll",i,"is",max_i)



fuction_call(chest1)
