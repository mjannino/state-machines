import time
from statemachine import StateMachine, State
from .assessment_states import (
    STATE_NOT_STARTED,
    STATE_QUESTION,
    STATE_QUESTION_ANSWERED,
    STATE_FINISHED,
)


class ScoringMachine(StateMachine):
    not_started = State(STATE_NOT_STARTED, initial=True)
    question = State(STATE_QUESTION)
    question_answered = State(STATE_QUESTION_ANSWERED)
    finished = State(STATE_FINISHED)

    start_assessment = not_started.to(question)
    answer_question = question.to(question_answered)
    new_question = question_answered.to(question)
    finish_assessment = question_answered.to(finished)
    restart_assessment = finished.to(not_started)

    def on_start_assessment(self):
        print("Starting assessment...")
        # This is where assessment starting actions go

    def on_answer_question(self):
        print("Answering question...")

    def on_new_question(self):
        print("Getting new question...")

    def on_finish_assessment(self):
        print("Completing assessment...")

    def on_enter_finished(self):
        print("Entering finished state")
        print("Restarting assessment")
        self.restart_assessment()


def python_statemachine_demo():
    print("This is the python-statemachine demo.")
    scoring_machine = ScoringMachine()
    time.sleep(2)
    print("\n")

    print("You can inspect the current state of the instance:")
    time.sleep(1)
    print("scoring_machine.current_state")
    print(scoring_machine.current_state)
    time.sleep(4)
    print("\n")

    print("You can assert what state it is in in a conditional:")
    time.sleep(1)
    print("scoring_machine.current_state == ScoringMachine.not_started")
    print(scoring_machine.current_state == ScoringMachine.not_started)
    time.sleep(4)
    print("\n")

    print("p_sm creates a dynamic 'is_<property>' field to assert on:")
    time.sleep(2)
    print("scoring_machine.is_not_started")
    print(scoring_machine.is_not_started)
    time.sleep(4)
    print("\n")

    print("To perform a transition, you call the transition:")
    print("scoring_machine.start_assessment()")
    scoring_machine.start_assessment()
    time.sleep(2)
    print("As you can see above, there was a function called with the transition.")
    time.sleep(4)
    print("\n")

    print("Running through the various states:")
    print("scoring_machine.answer_question()")
    scoring_machine.answer_question()
    time.sleep(2)
    print("scoring_machine.finish_assessment()")
    scoring_machine.finish_assessment()
    time.sleep(2)
    print("\n")

    print("As you can see above, you can transition inside of states.")
    print("We've restarted, so the current state should be not_started:")
    print(scoring_machine.current_state)
    time.sleep(4)
    print("\n")

    print("Demo over!")


def no_commentary():
    scoring_machine = ScoringMachine()

    print(scoring_machine.current_state)

    print(scoring_machine.current_state == ScoringMachine.not_started)
    print(scoring_machine.is_not_started)

    scoring_machine.start_assessment()
    scoring_machine.answer_question()
    scoring_machine.finish_assessment()

    print(scoring_machine.current_state)


if __name__ == "__main__":
    no_commentary()

