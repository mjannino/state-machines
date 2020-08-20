import time
import random
from automat import MethodicalMachine
from .assessment_states import (
    STATE_NOT_STARTED,
    STATE_QUESTION,
    STATE_QUESTION_ANSWERED,
    STATE_FINISHED,
)


class ScoringMachine(object):
    _machine = MethodicalMachine()

    # states
    @_machine.state(initial=True)
    def not_started(self):
        STATE_NOT_STARTED

    @_machine.state()
    def question(self):
        STATE_QUESTION

    @_machine.state()
    def question_answered(self):
        STATE_QUESTION_ANSWERED

    @_machine.state()
    def finished(self):
        STATE_FINISHED

    # inputs and outputs
    @_machine.input()
    def start_assessment(self):
        "start the assessment"

    @_machine.input()
    def answer_question(self, choice_idx):
        "answer a question"

    @_machine.output()
    def _return_answer_result(self, choice_idx):
        if choice_idx == random.randint(0, 3):
            return True
        return False

    @_machine.input()
    def get_next_question(self):
        "get the next question"

    @_machine.output()
    def _get_next_question(self):
        return "This is the content of the next question"

    @_machine.input()
    def finish_assessment(self):
        "finish the assessment"

    # state transitions
    not_started.upon(start_assessment, enter=question, outputs=[_get_next_question])
    question.upon(
        answer_question, enter=question_answered, outputs=[_return_answer_result]
    )
    question_answered.upon(
        get_next_question, enter=question, outputs=[_get_next_question]
    )
    question_answered.upon(finish_assessment, enter=finished, outputs=[])


def automat_demo():
    print("This is the automat demo.")
    scoring_machine = ScoringMachine()
    time.sleep(2)
    print("\n")

    print("You cannot inspect the state external to the machine.")
    print("You can simply call 'actions' that are state transitions.")
    time.sleep(2)
    print("scoring_machine.start_assessment()")
    print(scoring_machine.start_assessment())
    time.sleep(4)
    print("\n")

    print("Automat state machines can easily take inputs and give outputs")
    print("result = scoring_machine.answer_question(2)")
    result = scoring_machine.answer_question(2)
    print(result)
    time.sleep(4)
    print("\n")

    print("They can also just give new information and work like a module")
    print("new_question = scoring_machine.get_next_question()")
    new_question = scoring_machine.get_next_question()
    print(new_question)
    time.sleep(4)
    print("\n")

    print("result = scoring_machine.answer_question(1)")
    result = scoring_machine.answer_question(1)
    print(result)
    time.sleep(4)
    print("\n")

    print("scoring_machine.finish_assessment()")
    scoring_machine.finish_assessment()
    time.sleep(4)
    print("\n")

    print(
        "The design of Automata prevents you from writing code that can"
        " even get you into a bad state, \nby removing your ability to check the state. \nI think this is"
        " powerful, but it is admittedly very opinionated \nand makes testing a case of only"
        " testing side effects."
    )

    print("\n")

    print("Demo over!")


def no_commentary():
    scoring_machine = ScoringMachine()

    print(scoring_machine.start_assessment())

    result = scoring_machine.answer_question(2)
    print(result)

    new_question = scoring_machine.get_next_question()
    print(new_question)

    result = scoring_machine.answer_question(1)
    print(result)

    scoring_machine.finish_assessment()
    time.sleep(4)

