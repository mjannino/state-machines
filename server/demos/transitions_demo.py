import time
from transitions import Machine
from .assessment_states import (
    STATE_NOT_STARTED,
    STATE_QUESTION,
    STATE_QUESTION_ANSWERED,
    STATE_FINISHED,
)

NUM_QUESTIONS = 3


class ScoringMachine(object):
    # define states upfront
    states = [
        STATE_NOT_STARTED,
        STATE_QUESTION,
        STATE_QUESTION_ANSWERED,
        STATE_FINISHED,
    ]

    # initialization function that can take parameters
    def __init__(self, session_data):
        self.session_data = session_data

        self.questions_answered = session_data.get("questions_answered", 0)
        self.user_rd = session_data.get("user_rd", 50)
        self.user_ranking = session_data.get("user_ranking", 1500)

        self.machine = Machine(
            model=self,
            states=ScoringMachine.states,
            initial=session_data.get("initial_state", STATE_NOT_STARTED),
        )

        self.machine.add_transition(
            "start_assessment", STATE_NOT_STARTED, STATE_QUESTION
        )
        self.machine.add_transition(
            "answer_question",
            STATE_QUESTION,
            STATE_QUESTION_ANSWERED,
            before="answer_question",
        )
        # You can go from any state to a specific state
        self.machine.add_transition("get_new_question", "*", STATE_QUESTION)

        # You can also overload the same name property, and only allow a certain transition if a condition is met
        self.machine.add_transition(
            "finish_assessment",
            "*",
            STATE_FINISHED,
            conditions=["answered_enough_questions"],
            after="restart_assessment_after_finish",
        )
        self.machine.add_transition("finish_assessment", "*", STATE_QUESTION)

        self.machine.add_transition(
            "restart_assessment", STATE_FINISHED, STATE_NOT_STARTED
        )

    def answer_question(self):
        print("Answering Question")
        self.questions_answered += 1

    def restart_assessment_after_finish(self):
        print("Restarting assessment")
        # Can do data manipulation here
        self.restart_assessment()

    @property
    def answered_enough_questions(self):
        return self.questions_answered > NUM_QUESTIONS


def answer_question():
    print("Answering question.")


EXAMPLE_SESSION_DATA = {
    "questions_answered": 0,
    "user_rd": 25,
    "user_ranking": 1550,
    "initial_state": STATE_NOT_STARTED,
}


def transitions_demo():
    print("This is the transitions demo.")
    scoring_machine = ScoringMachine(EXAMPLE_SESSION_DATA)
    time.sleep(2)
    print("\n")

    print("You can inspect the current state...")
    time.sleep(1)
    print("scoring_machine.state")
    print(scoring_machine.state)
    time.sleep(4)
    print("\n")

    print("...or you can assert with built-in dynamic assert functions.")
    time.sleep(2)
    print("format: instance.is_<name-of-state>")
    print("scoring_machine.is_question-answered()")
    is_question_answered = getattr(scoring_machine, "is_question-answered")
    print(is_question_answered())
    time.sleep(4)
    print("\n")

    print("You can perform a transition by calling the transition:")
    time.sleep(2)
    print("current state:", scoring_machine.state)
    print("scoring_machine.start_assessment()")
    scoring_machine.start_assessment()
    print("new state:", scoring_machine.state)
    time.sleep(4)
    print("\n")

    print("Some states can be protected by conditionals automatically:")
    print("current state:", scoring_machine.state)
    print("scoring_machine.answer_question()")
    scoring_machine.answer_question()
    print("current state:", scoring_machine.state)
    time.sleep(4)
    print("questions answered: ", scoring_machine.questions_answered)
    print("get new question:")
    scoring_machine.get_new_question()
    print("current state:", scoring_machine.state)
    time.sleep(4)
    scoring_machine.answer_question()
    print("questions answered: ", scoring_machine.questions_answered)
    print("current state:", scoring_machine.state)
    print("attempt to finish assessment:")
    print("scoring_machine.finish_assessment()")
    scoring_machine.finish_assessment()
    print("this is a protected action with < 3 questions answered")
    print("it will prevent us from finishing the assessment and return us to question")
    print("\n")
    time.sleep(4)

    print("current state:", scoring_machine.state)
    time.sleep(4)
    print("scoring_machine.answer_question()")
    scoring_machine.answer_question()
    print("questions answered: ", scoring_machine.questions_answered)
    print("get new question:")
    scoring_machine.get_new_question()
    time.sleep(2)
    print("\n")

    print("scoring_machine.answer_question()")
    scoring_machine.answer_question()
    print("questions answered: ", scoring_machine.questions_answered)
    print("current state:", scoring_machine.state)
    print("attempt to finish assessment:")
    print("scoring_machine.finish_assessment()")
    scoring_machine.finish_assessment()
    print("\n")
    print("current state:", scoring_machine.state)
    print("\n")

    print("Demo over!")


def no_commentary():
    scoring_machine = ScoringMachine(EXAMPLE_SESSION_DATA)

    print(scoring_machine.state)
    is_question_answered = getattr(scoring_machine, "is_question-answered")
    print(is_question_answered())
    scoring_machine.start_assessment()

    print("current state:", scoring_machine.state)
    scoring_machine.answer_question()
    print("current state:", scoring_machine.state)
    print("questions answered: ", scoring_machine.questions_answered)
    scoring_machine.get_new_question()
    print("current state:", scoring_machine.state)
    scoring_machine.answer_question()
    print("questions answered: ", scoring_machine.questions_answered)
    print("current state:", scoring_machine.state)
    scoring_machine.finish_assessment()

    print("current state:", scoring_machine.state)
    scoring_machine.answer_question()
    print("questions answered: ", scoring_machine.questions_answered)
    scoring_machine.get_new_question()
    scoring_machine.answer_question()
    print("questions answered: ", scoring_machine.questions_answered)
    print("current state:", scoring_machine.state)
    scoring_machine.finish_assessment()
    print("current state:", scoring_machine.state)


if __name__ == "__main__":
    no_commentary()
