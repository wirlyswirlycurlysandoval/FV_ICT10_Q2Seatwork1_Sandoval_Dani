from pyscript import display
from js import document

club_members = [
    "Dani Sandoval",
    "Lance Catu",
    "Erin Rioflorido",
    "Inno Peña",
    "Chloe Adlawan",
    "Georgina Banal",
    "Audrey Tan",
    "Meyer Cruz",
    "Enzo Macaranas",
    "Chelsi Sibal",
    "Mandy Cajanding",
    "Julia Bermudez",
    "Chloe Gutierrez",
    "Aleynah Redillas",
    "Sam Bautista",
    "Jillian Eusebio",
] #names of people in the club

def checker_result(e):
    first_name = document.getElementById("first").value.strip().title()
    last_name = document.getElementById("last").value.strip().title()

    full_name = first_name + " " + last_name #variable for putting the first and last name together

    is_member = full_name in club_members #determines if the full name given is part of the club

    message = {
        True: f"Congratulations {full_name}! You are now part of the ZEPHYR!", #shows if inputted name is in the variable "club_members"
        False:  f"Sorry {full_name}, your name is not on the list." #shows if inputted name is not in the variable "club_members"
    }[is_member] 
    
    document.getElementById("output2").innerText = message #displays the results