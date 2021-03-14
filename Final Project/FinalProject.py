total_point = 0

the_question_1 = "1) How many continents are there in the world?"
question1 = {"Question" : the_question_1, "A" : 5, "B" : 6, "C" : 7, "D" : 8, "Answer" : "C"}

the_question_2 = "2) Which is the largest continent?"
question2 = {"Question" : the_question_2, "A" : "Asia", "B" : "Africa", "C" : "Antartica", "D" : "Australia", "Answer" : "A"}

the_question_3 = "3) What is the molecular structure of water?"
question3 = {"Question" : the_question_3, "A" : "HCl", "B" : "H2O", "C" : "O2", "D" : "O3", "Answer" : "B"}

the_question_4 = "4) Who is the Turkish scientist who received the Nobel prize in chemistry?"
question4 = {"Question" : the_question_4, "A" : "Cahit Arf", "B" : "Ali Kuşçu", "C" : "Orhan Pamuk", "D" : "Aziz Sancar", "Answer" : "D"}

the_question_5 = "5) Which of the following is a renaissance artist?"
question5 = {"Question" : the_question_5, "A" : "Van Gogh", "B" : "Michelangelo", "C" : "Picasso", "D" : "Monet", "Answer" : "B"}

the_question_6 = "6) Which is not the primary color?"
question6 = {"Question" : the_question_6, "A" : "Red", "B" : "Yellow", "C" : "Orange", "D" : "Blue", "Answer" : "C"}

the_question_7 = "7) Who invented the light bulb?"
question7 = {"Question" : the_question_7, "A" : "Edison", "B" : "Tesla", "C" : "Milikan", "D" : "Roentgen", "Answer" : "A"}

the_question_8 = "8) Which is the largest planet in our solar system?"
question8 = {"Question" : the_question_8, "A" : "Earth", "B" : "Venus", "C" : "Saturn", "D" : "Jupiter", "Answer" : "D"}

the_question_9 = "9) Who founded apple?"
question9 = {"Question" : the_question_9, "A" : "Jack Dorsey", "B" : "Marc Zuckerburg", "C" : "Steve Jobs", "D" : "Bill Gates", "Answer" : "C"}

the_question_10 = "10) Which is not a prime number?"
question10 = {"Question" : the_question_10, "A" : "2131", "B" : "2401", "C" : "2557", "D" : "2699", "Answer" : "B"}

questions = [question1, question2, question3, question4, question5, question5, question6, question7, question8, question9, question10]

for i in range(11):
    print(questions[i]["Question"])
    print("A) " , questions[i]["A"], "\tB)", questions[i]["B"])
    print("C) " , questions[i]["C"], "\tD)", questions[i]["D"])

    given_answer = input("Cevabınızı giriniz: ")

    if questions[i]["Answer"] == given_answer.upper():
        total_point +=1

if total_point > 5:
    print("You make " , total_point , "trues, you are successful")
else:
    print("You make " , total_point , "trues, you are not successful")

