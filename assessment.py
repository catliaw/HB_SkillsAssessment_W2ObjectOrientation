"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Encapsulation - Having related data and behavior (methods) bound together.

Abstraction - Being able to use the methods and class structure without having
to know how it works exactly under the hood.

Polymorphism - Being able to use the same template for data and same methods
that have different results. For example, two different instances/subclasses
may use the same structure for data and method, but depending on more specific
information added to the instance/subclass, the method may have different results.


2. What is a class?

A class is a user-defined data structure built upon (under the hood) the dictionary
data structure, but a class is a much smarter dictionary. Classes are a way to bind
together related data and functionality (method). Instead of having nested dictionaries
to organize related data with its label, classes have "instances" or objects which
can have multiple connected attributes and values. Also, classes can also have related
functionality/methods.


3. What is an instance attribute?
An instance attribute is the like the a nested dictionary within a dictionary.
From a class, the user can create an instance or object using the class. With
that instance or object, the user can create attributes specific to that object.


4. What is a method?
A method is basically the same thing as a function but it specific to the class
and its members (instances/objects). It is used with the dot method.


5. What is an instance in object orientation?
An instance is a specific unit in object orientation that is created using the 
class template. This instance can have its own "instance" attributes and has
access to class attributes and methods. It can call upon class methods with the
dot method.


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is a general attribute (ex. characteristic) that applies to all
members/instances of the class. If the instance does not have a specified instance
attribute, it will have access to the class attribute. An instance can also have 
different value for the same attribute name. This instance attribute would be 
specific to the instance.

For example, in the class Girls, the class attribute hair length is long. Say Grace
is an instance in the Girls class, and she does not have a specific instance
attribute related to her hair length. When looking up her hair length in the class,
the user will see that she has long hair, because the class attribute for hair length
is long. However, if Grace gets a bob hair cut, her hair length attribute specific
to her can be changed to "short". This attribute would only apply to Grace, and would
not affect any of the other instances or members of the Girls class.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        response = raw_input(self.question + " > ")
        if response == self.correct_answer:
            return True
        else:
            return False


class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds a question/answer duo to the Questions class and then to the instance questions list."
        """
        # question_self = str(self)
        # question_self = Question(question, correct_answer)
        setattr(Question, question, correct_answer)
        self.questions = self.questions.append(self)
        # Cannot figure out how to instantiate an object of one class from the method
        # of another class. I tried setting a variable question_self to equal the
        # name of current instance in question (from Exam class) because just using
        # self will change the reference location in memory after I instantiate the 
        # question/answer in the Question class. So when I want to then set the question
        # to the Exam object's instance attribute, "self" has changed to another 
        # location in memory and to another data type.

    def administer(self):
        """Adds up the raw score of correctly answered questions."""
        score = 0

        for question in self.questions:
            result = Question.ask_and_evaluate()
            if result is True:
                score += 1

        return score


def take_test(exam, student):
    """Administers the exam and assigns the score as an instance attribute to the student."""
    score = exam.administer()
    student.score = score


def example(exam_name, student_first_name, student_last_name, student_address):
    """A sample exam, which creates an exam, adds questions, creates a student, administers the exam."""
    exam_name = Exam(exam_name)
    question_1 = exam_name.add_question("What is the capitol city of California?", "Sacramento")
    question_2 = exam_name.add_question("What is Cat's favorite color?", "Blue")
    question_3 = exam_name.add_question("What is Cat's favorite Disney character?", "Stitch")
    student_first_name = Student(student_first_name, student_last_name, student_address)
    exam_name.administer()
    # Couldn't figure out the add_question method, so this function also does not work.
    # Not sure if I am instantiating question_1, _2, and _3 effectively.

class Quiz(Exam):

    def administer(self):
        """Same as Exam's administer method, with addition to 50 percent or more to pass course/return True."""
        total_possible = len(self.questions)
        super(administer, self).administer()
        if score / total_possible >= 0.5:
            return True
        else:
            return False