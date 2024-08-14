# DICTIONARY AND NESTING LIST ANDDICTIONARIES
programming_dictionary = {
    "name":"Oluwaseun",
    "age":26,
    21: "Day of birth"
}

# Accesing Dictionary
programming_dictionary[21]
programming_dictionary["name"]


# Addijng new Item
programming_dictionary["Loop"] = "for performing a repeitive task"

programming_list = ["asdfg","werty",12,21]
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Test1
student_grades = {}
student_scores = {"Mr Wahab" :80,"SIs Nafisat": 90,"akowe":20,"Oluwaseun":99,"Mr Akeem":50,"Ayo": 35}
for student in student_scores:
    if student_scores[student] < 40:
        student_grades[student] = "Poor"
    elif student_scores[student] > 40 and student_scores[student] <= 60:
        student_grades[student] = "Good"
    elif student_scores[student] > 60 and student_scores[student] <= 70:
        student_grades[student] = "Very Good"
    elif student_scores[student] > 70 and student_scores[student] <= 80:
        student_grades[student] = "Execellent"
    elif student_scores[student] > 80 and student_scores[student] <= 90:
        student_grades[student] = "Exceed Expectation"
    elif student_scores[student] > 90 and student_scores[student] <= 100:
        student_grades[student] = "Oustanding!"

print(student_grades)

# NESTING
cities = {
    "France":"Paris",
    "Germany": "Berlin"
}

cities["Europe"] = ["Italy","England","Spain"]
cities["European_cities"] = {"Italy":"Napoli","England":"London","Spain":"Madrid"}
# print{cities}
print(cities)

# Teszt2
biding_Dic = {}
biding = False

def find_d_highest_bidder(bidding_dictionaries):
  highest_bidder = 0
  bid_winner = ""
#   winner= {}
  for each_bidder in bidding_dictionaries:
   new_bidder_amout = bidding_dictionaries[each_bidder]
   if new_bidder_amout > highest_bidder:
      highest_bidder = new_bidder_amout
      bid_winner = each_bidder

  print(f"The winner is {bid_winner} with the bid of ${highest_bidder}")
#    print(each_bidder)


while  not biding: # if biding is still going on, continue this loop
    name = input("What is your Name?:")
    price  = int(input("What is your bid?: \n $"))
    biding_Dic[name] =  price
    # biding_List.append(biding_Dic)

    continue_biding = input("do u still want to bid? type 'yes' or 'no':  ")
    if continue_biding == "no": # if biding ends, stop this loop
        biding = True
        find_d_highest_bidder(biding_Dic)



