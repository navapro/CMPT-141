# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil

# CMPT 116/141 -maplabeling

def intersection_2sq(s1,s2):
    """
    This function determines whether or not the two given squares intersect. The two
    squares are given by the integer coordinates of their lower left corner.
    Both squares have side length 2.
    Parameters: s1,s2: Each is a 2 by 2 square whose lower left corner coordinates
    is given as a tuple of two integers
    Returns Boolean: True if the two squares intersect, and False if they do not.
    """
    return s1[0]-1 <= s2[0] and s2[0] <= s1[0] + 1 and \
           s1[1] - 1 <= s2[1] and s2[1] <= s1[1] + 1


def intersection_inlist(test_square,List):

    """
    This function determines if a given test_square intersects with any of the squares
    in the given list of squares. All of the squares have side length 2.
    Parameter1 test_square:A 2 by 2 square whose lower left corner coordinates is
    given as a tuple of two integers
    Parameter2 List: A list of 2 by 2 squares whose lower left corner coordinates
    are given as a tuple of two integers
    Returns Boolean:  True is the test_square intersects with any of the squares
    in the given list of squares,
    False if there is no intersection.
    """

    for sq in List:
        if intersection_2sq(test_square,sq):
            return True
    return False

def add(potential_labels,confirmed_labels):
    """
    determines which squares (potential labels), from a given list of squares,
    should be added to another list of non-intersecting squares (confirmed labels) so as to display the maximum number of labels
    :param potential_labels: Squares(labels) that has not been checked and confirmed
    :param confirmed_labels: Squares that have been confirmed and are non intersecting.
    :return:  a list of labels that includes the intially confirmed labels plus as many as possible of the potential labels.
    """

    if len(potential_labels) != 0:

        if len(confirmed_labels) == 0:
            collide = False
        else:
            collide = intersection_inlist(potential_labels[0],confirmed_labels)

        if not collide:
            copy_confirm = confirmed_labels.copy()
            copy_confirm2 = confirmed_labels.copy()
            copy_confirm.append(potential_labels[0])
            include = add(potential_labels[1:],copy_confirm)
            exclude = add(potential_labels[1:],copy_confirm2)

            if len(include) > len(exclude):
                return include
            else:
                return exclude
        else:
            return add(potential_labels[1:],confirmed_labels)
    else:
        return confirmed_labels


squarelist1 = [(-1,-1),(0,0),(1,1)]
squarelist2 = [(2,3),(6,8),(6,9),(9,1),(3,4),(2,4)]
squarelist3 = [(-3,0),(-2,1),(-1,2),(0,1),(1,0),(0,-1),(-1,-2),(-2,-1)]

emt = []
print("From among the labels", squarelist1)
emt = add(squarelist1,emt)
print("The following can be drawn without intersection",emt)

emt = []
print("From among the labels", squarelist2)
emt = add(squarelist2,emt)
print("The following can be drawn without intersection",emt)

emt = []
print("From among the labels", squarelist3)
emt = add(squarelist3,emt)
print("The following can be drawn without intersection",emt)