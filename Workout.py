"""
File: Workout.py
Author: Paul Garland, Sterling Foote

Description:  This program will use a queue structure to run a short exercise program which gives the user a selection
of workouts and lets them choose which exercise(s) to do and how many reps of each workout.
"""
from queueStruct import ListQueue
import time


def q_return(queue, adjustment):
    # Helper function to pop the first element and add it to the back of the queue.
    queue.pop()
    queue.add(adjustment)


def all_pop(names, times, sets):
    # Helper function to pop all elements from the queue.

    x = [names, times, sets]

    for i in x:
        i.pop(0)


def prompt(names, times, sets):
    # Prompts the User to input their exercise routine
    x = int(input("How many exercises are we planning today?"))
    i = 0
    while i < x:
        workout = input(f"Enter the name of workout {i + 1}: ")
        names.add(workout)
        seconds = int(input(f" How much time would you like to spend on {workout} per set, in seconds: "))
        times.add(seconds)
        y = int(input(f"How many sets are planned for {workout}: "))
        sets.add(y)
        print()

        i += 1


def display(names, times, sets):
    # Shows the user the workout they have selected.
    cnt = 1

    print("=====================")
    print("Today's Workout:")
    while cnt <= len(names):
        n = names.peek()
        t = times.peek()
        s = sets.peek()

        print(f"{n}: {s} Sets at {t} Seconds")

        cnt += 1
        q_return(names, n)
        q_return(times, t)
        q_return(sets, s)
    print("=====================")


def current(names, times, sets):
    # The bulk of the program, this method reads the queues creates a timer for the length of the t variable.
    # Decrements the timer before decrementing the number of sets.
    while not sets.isEmpty():
        # pulls the queue items relevant to the current exercise.
        n = names.peek()
        t = times.peek()
        s = sets.peek()
        t_return = t
        while t != 0:
            # timer to countdown how many seconds have passed on the current exercise.
            mins, secs = divmod(t, 60)
            timer = '{:02d} : {:02d}'.format(mins, secs)
            time.sleep(1)
            t -= 1

            print(f"\nCurrent Workout: {n}")
            print(f"Number of Seconds: ", timer)
            print(f"Set's left: {s}")

        s -= 1
        if s == 0:
            # Remove exercise once the set # becomes 0.
            print("\n====================================")
            print(f" Congratulations {n} is complete!")
            print("====================================")
            names.pop()
            times.pop()
            sets.pop()

        elif s >= 1:
            # Moves exercise to the end of the queue.
            print("\n========")
            print("End Set")
            print("=========")

            q_return(sets, s)
            q_return(names, n)
            q_return(times, t_return)


def main():
    names = ListQueue()
    times = ListQueue()
    sets = ListQueue()

    # Gather and display the data which the user inputs.
    prompt(names, times, sets)
    display(names, times, sets)
    # Starts the program
    any_key = input("\nPress any key to start your workout.")
    if any_key is not None:
        current(names, times, sets)

    else:
        print("Honestly, I don't know how this didn't work, It should've just hung "
              "until an input was given.")


def test():
    # For debugging purposes only.
    names_list = ['Push-ups', 'Sit-ups', 'Burpees']
    times_list = [2, 5, 7]
    sets_list = [2, 1, 3]

    names_queue = ListQueue(names_list)
    times_queue = ListQueue(times_list)
    sets_queue = ListQueue(sets_list)

    display(names_queue, times_queue, sets_queue)
    current(names_queue, times_queue, sets_queue)


main()
