# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil

# Sample bock lists
site0 = [2,5,5,6]
site1 = [3 ,3 ,5,7,7,9]

def form_column(height,block_sizes):
    """
    determines whether or not it is possible to form a column of
    a given height using only the blocks whose sizes are given in list

    :param height: an integer giving the desired height of a column
    :param block_sizes: a list of the sizes of the available blocks at a site
    :return: True if it is possible to build a column of the desired height,
    and False if it is not possible

    """

    if len(block_sizes)  == 0:
        return False
    elif block_sizes[0] == height or height == 0:
        return True
    else:
        include = form_column(height-block_sizes[0],block_sizes[1:])
        exclude = form_column(height,block_sizes[1:])
        if include or exclude:
            return True
        else:
            return False

def run(lis,start,end, lis_out):
    """
    creates a list of column heights between 1 and 50 that can be constructed.

    :param lis: a list of the sizes of the available blocks at a site
    :param start: integer value of the smallest desired height (1)
    :param end: integer value of the largest desired height (50)
    :param lis_out: empty list, return after the heights are appended.
    :return: list of column heights between 1 and 50 that can be constructed
    """

    if start == end:
        return []
    else:
        if form_column(start,lis):
            lis_out.append(start)
        run(lis,start+1,end,lis_out)
        return lis_out


# create an empty list and call the run function.
output = []
output = run(site0,1,50,output)

print("The heights of columns that can be built from blocks found at site 0 are")
print (output)
