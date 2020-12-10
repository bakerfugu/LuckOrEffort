import random

EFFORT_WEIGHT = 0.95     # selection considers 95 percent effort, feel free to try other numbers
LUCK_WEIGHT = 0.05      # selection considers 5 percent luck, feel free to try other numbers

PRINT_STAT_DETAILS = False  # change this to True to get some more interesting stat details

def make_astronaut():
    """
    Returns an astronaut with random luck and effort
    """
    effort = random.random()     # generates a random decimal between 0 and 1
    luck = random.random()      # generates a random decimal between 0 and 1
    return {'effort': effort, 'luck': luck}

def make_astronauts(wannabe_astronauts, passing_score):
    passing = []

    for i in range(wannabe_astronauts):
        astronaut = make_astronaut()
        if (astronaut['effort'] >= passing_score):
            passing.append(astronaut)

    return passing

def select_astronauts(astronauts, num_selected):
    """
    Returns the top X astronauts, as determined by
    the calc_score function, which incorporates a bit of luck
    """
    if PRINT_STAT_DETAILS:
        print("\nSelecting the top", num_selected, "astronauts out of", len(astronauts), "options.")
        print("Astronaut total score is calculated with", str(EFFORT_WEIGHT * 100) + "%", "effort and", str(LUCK_WEIGHT * 100) + "%", "luck.")

    # the key=calc_score arranges this list based on the combined score,
    # found it on google
    sorted_astronauts = sorted(astronauts, key=calc_score)

    # This gets the last NUM astronauts in the list, AKA the astronauts with the top scores
    selected_astronauts = sorted_astronauts[-num_selected:]

    return selected_astronauts

def analyze_astronauts(astronauts):
    sum_effort = 0
    sum_luck = 0

    min_effort = 1 # set minimums to max value first
    min_luck = 1

    for astronaut in astronauts:
        effort = astronaut['effort']
        luck = astronaut['luck']
        sum_effort += effort
        sum_luck += luck
        if luck < min_luck:
            min_luck = luck
        if effort < min_effort:
            min_effort = effort

    average_effort = sum_effort / len(astronauts)
    average_luck = sum_luck / len(astronauts)

    if PRINT_STAT_DETAILS:
        print("These astronauts had an average effort of", round(average_effort, 3), "and average luck of", round(average_luck, 3))
        print("The lowest effort found in this group is", round(min_effort, 3), "the lowest luck is", round(min_luck, 3))

    return [average_effort, average_luck]

def calc_score(astronaut):
    effort_portion = astronaut['effort'] * EFFORT_WEIGHT
    luck_portion = astronaut['luck'] * LUCK_WEIGHT
    return effort_portion + luck_portion

def calc_percent_increase(starting_value, final_value):
    decimal_increase = (final_value - starting_value) / starting_value
    percent_increase = round(decimal_increase * 100, 1)
    with_percent_sign = str(percent_increase) + "%"
    return with_percent_sign

def main():
    print("Welcome! This simulation explores a simplified comparison of luck and effort.")
    if not PRINT_STAT_DETAILS:
        print("Set the constant PRINT_STAT_DETAILS to True to see additional information.")
    print("\nWhen prompted, type numbers then hit enter to proceed.")
    print("Try: 18300 applicants, 90 effort score, and 11 astronauts selected.")
    print("-------------------------")

    wannabe_astronauts = int(input("\nHow many people apply to become an astronaut? "))
    passing_score = int(input("\nWhat's the lowest effort/skill score needed to pass the first cut? (1-100) "))

    passing = make_astronauts(wannabe_astronauts, passing_score/100)

    pass_percentage = round(len(passing) / wannabe_astronauts * 100, 1)
    print("\nThere are", len(passing), "applicants who put in enough effort/work to make the first cut (" + str(pass_percentage) + "%).")
    passing_averages = analyze_astronauts(passing)

    num_selected = int(input("\nHow many people are selected to become astronauts? "))
    selected = select_astronauts(passing, num_selected)
    selected_averages = analyze_astronauts(selected)

    effort_percent_increase = calc_percent_increase(passing_averages[0], selected_averages[0])
    luck_percent_increase = calc_percent_increase(passing_averages[1], selected_averages[1])

    print("\n-------------------------")
    print("--       SUMMARY       --")
    print("The selected astronauts are (on average):")
    print(" -", effort_percent_increase, "more \"effortful\" than the", len(passing), "people that passed the first cut")
    print(" -", luck_percent_increase, "luckier than the", len(passing), "people that passed the first cut")
    print("-------------------------\n")

    print("Experiment with different numbers, or change the effort/luck weights using EFFORT_WEIGHT and LUCK_WEIGHT. Ideas: select the number of billionaires in the US from the population of the US, or select the number of 2020 Stanford admits from the number of college freshmen in 2020.")

    print("\nInspired by Veritasium's video Is Success Luck or Hard Work?")
    print(" - https://www.youtube.com/watch?v=3LopI4YeC4I")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()