"""
Methods Exercise
Create a method, which takes the state and gross income as the arguments
and returns the net income after deducting tax based on the state.
Assume Federal Tax: 10%
Assume state tax on your wish
"""
"""
Calculate the next income after federal and state tax
:param gross: Gross Income
:param state: State Name
:return: Net Income 
"""
def calculateNetIncome(state, gross):
    state_tax = {'Ca': 10, 'NY': 23, 'TX': 20, 'NJ': 15}
    #Calculate net income after federal tax
    net = gross - (gross * .10)
    #Calculate net income after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
    else:
        print("Your state tax is zero")
    print("Your net income after all the heavy taxes is:" + str(net))
    return net

calculateNetIncome('hhh', 100000)