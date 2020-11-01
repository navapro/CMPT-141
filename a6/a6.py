# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil


import matplotlib.pyplot as mplt

def fnSperateLine(line):
    """
    eliminate whitespaces from a line of text file.

    :param line: A string of a raw line from a text file
    :return:  A list of strings containing each element from the input line by eliminating whitespaces (spaces or
new line characters) and separators
    """
    re = line.rstrip()
    re = re.split(",")
    return re

def fnReadInParameters(file_name):
    """
    Read the parameter file and store all of the data in a dictionary.

    :param file_name: a string indicating the name of the parameter file
    :return:  a dictionary that stores all of the parameter file data of the SIR model.
    """
    f = open(file_name, "r")
    re = {}
    for i in f:
        j = fnSperateLine(i)
        re[j[0]] = float(j[1])
    f.close()
    return re

def fnReadInInitialState(file_name):
    """
    Read the state file and store necessary data on a list of dictionaries.
    :param file_name: a string indicating the name of the state input file
    :return: A list of records (dictionaries) that stores state (values of S, I and R) of all days.
    """
    f = open(file_name , "r")
    lis = []
    for i in f:
        if not i[0].isalpha():
            current = {}
            line = fnSperateLine(i)
            current["S"] = float(line[1])
            current["I"] = float(line[2])
            current["R"] = float(line[3])
            lis.append(current)
    f.close()
    return lis

def simulation(parameters,states, intervention):
    """
    Simulate the calculation of SIR model by calculating the values of S,I and R.
    :param parameters: A dictionary of the parameters.
    :param states: A list of records of the beginning day's state.
    :param intervention: A boolean indicates whether a run of the simulation is performing intervention or not.
    :return: None
    """
    # Calculate beta based on boolean input for intervention.
    if intervention == True:
        beta = parameters["beta_intervention"]
    else:
        beta = parameters["beta_normal"]

    simulation_days = parameters["simulation_days"]

    # loop iterating “simulation_days" times
    for i in range(int(simulation_days)):

        S_last_day = states[-1]["S"]
        I_last_day = states[-1]["I"]
        R_last_day = states[-1]["R"]

        # calculate the new infected and recovered data.
        new_infected = beta * I_last_day * S_last_day / parameters["N"]
        new_recovered = I_last_day /parameters["gamma"]

        # calculate the new S,I and R data.
        S_new_day = S_last_day - new_infected
        I_new_day = I_last_day + new_infected - new_recovered
        R_new_day = R_last_day + new_recovered

        current = {}
        current["S"] = S_new_day
        current["I"] = I_new_day
        current["R"] = R_new_day

        # Add the new information to the list of dictionaries.
        states.append(current)

def fnWriteState(states,path_name):

    """
    Write the list of states to a tabular file.
    :param states: A list of records (the list of state of all days)
    :param path_name: A string of a path name of the output le
    :return: None
    """
    f = open(path_name,"w")

    f.write('time(day),S,I,R \n')
    for i in range(len(states)):
        f.write(str(i) + ',')
        f. write (','. join ([ str(states[i][x]) for x in states[i]])+ '\n')
    f.close()

def fnPlotState(states):
    """
    Plot the data in the list of records.
    :param states: A list of records (the list of state of all days)
    :return: None
    """

    for i in range(len(states)):
        mplt.plot(i,states[i]["S"],"go")
        mplt.plot(i,states[i]["I"],"ro")
        mplt.plot(i, states[i]["R"], "bo")

    mplt.title("SIR model")
    mplt.xlabel("Time (days)")
    mplt.ylabel("Population")
    mplt.show()

# Calling all the required functions.
parameters = fnReadInParameters("parameters.txt")
states = fnReadInInitialState("state_input.txt")
intervention = True
simulation(parameters,states, intervention)
fnWriteState(states,"state_output.txt")
fnPlotState(states)