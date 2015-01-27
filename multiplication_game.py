'a simple script to test mulitplication speeds'
import sys
from random import randint
#TODO change time to datetime
import time


def get_difficult_multiplier(max_num_tested):
    'get a non-trivial multiplier'

    result = 0
    while(result % 10 == 0 or result == 2):
        result = randint(2, max_number_tested)
    return result

def report_time(time_in_sec):
    'represent time in hrs min sec or min sec. whichever is pretty'
    m,s = divmod(time_in_sec, 60)
    h,m = divmod(m, 60)
    if h > 0:
        return "{:.0f} hr {:2.0f} min {:5.2f} sec".format(h, m, s).strip()
    else:
        if m > 0:
            return "{:2.0f} min {:5.2f} sec".format(m, s).strip()
        else:
            return "{:5.2f} sec".format(s).strip()


if __name__ == '__main__':
    print "hi welcome to the program"

    #TODO put database support so that there is no need to enter name many times
    name = raw_input("please enter your name -> ")
    print "Hi {}".format(name)

    max_number_tested = int(raw_input(
        "please enter the maximum number table you want to test yourself in"\
         "(should be greater than 2) "))
    assert max_number_tested > 2

    total_questions = 20
    correct_answers = 0
    start_time = time.time()
    for i in range(total_questions):
        a = get_difficult_multiplier(max_number_tested)
        b = get_difficult_multiplier(max_number_tested)

        expected_product = a * b
        product_entered = int(raw_input("{} * {} = ".format(a, b)))
        if(product_entered == expected_product):
            print "right answer! :)"
            correct_answers += 1
        else:
            print "wrong answer! :("


    total_time_taken = time.time() - start_time

    print "number of correct answers = {}".format(correct_answers)
    print "number of wrong answers = {}".format(
        total_questions - correct_answers)

    print "total time taken  = {}".format(report_time(total_time_taken))
    print "time per question = {}".format(report_time(
        total_time_taken / total_questions))

        

