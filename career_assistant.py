print("=" *40)
print("Career Path AI assistant")
print("="*40)

Physics=0
Software=0
AI = 0

print("\nAnswer y/n")

Q1= input("Are you interested in programming? ")
if Q1.lower() == "y":
    Software +=2
    AI +=1

Q2= input("Are you interested in Mathematics? ")
if Q2.lower() == "y":
    Physics +=2
    AI +=1

Q3= input("Are you interested in solving complex technical problems? ")
if Q3.lower() == "y":
    Software +=2

Q4= input(" Are you interested in learning complex theoretical strucutures? ")
if Q4.lower() == "y":
    Physics += 2

Q5= input("Are you interested in building AI agents? ")
if Q5.lower() =="y":
    AI +=3

print("\n ANALYSIS")
print("-"*20)

print(f"Software Score :{Software}")
print(f"Physics Score:{Physics}")
print(f"AI Score:{AI}")

if Software>=Physics and Software>=AI:
    recommendation= "Software Engineering"
elif Physics>= Software and Physics>= AI:
    recommendation= "Theoretical Physicist"
else:
    recommendation= "Machine Learning Engineer"

print("\nRecommendation Path: ")
print(recommendation)

print("\nReasoning: ")
print("Recommendation generated from weighted decision logic")





