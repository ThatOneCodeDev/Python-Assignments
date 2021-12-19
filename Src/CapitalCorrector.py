### Programming Assignment #11: 
### Program name: CapitalCorrector

state_capitals = {}

# prints all states and capitals stored in the dictionary
def print_state_capitals():
    for state, capital in state_capitals.items():
        print(f'{state}, {capital}')

def main():
    file_name = 'StateCapitalsIncorrect.txt' # name of input file, in a prod program it is best to get this dynamically from the user.
    # take comma delimited file and split into state_capitals dictionary
    with open(file_name, 'r') as f:
        for line in f:
            state, capital = line.split(',') # split line into state and capital
            state = state.strip().title()
            capital = capital.strip().title() # sanitize the payload and strip any leading or trailing whitespace.
            state_capitals[state] = capital   # add state and capital to dictionary 
    print_state_capitals() # print incorrect dictionary items
    print('\nCorrecting errors in loaded dictionary...\n')
    # correct errors in dictionary
    state_capitals['South Dakota'] = 'Pierre'
    state_capitals['Oklahoma'] = 'Oklahoma City'
    del state_capitals['Ontario']
    state_capitals['Wyoming'] = 'Cheyenne'
    # print items from corrected dictionary
    print_state_capitals()
    # write corrected dictionary to a file
    with open('StateCapitals.txt', 'w') as f:
        for state, capital in state_capitals.items():
            if state == 'Wyoming': # if state is Wyoming, do not add a newline character to mach original file format.
                f.write(f'{state}, {capital}')
            else:
                f.write(f'{state}, {capital}\n')

if __name__ == '__main__':
    main()