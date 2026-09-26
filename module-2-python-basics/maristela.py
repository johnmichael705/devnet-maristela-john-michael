"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: [Maristela, John Michael]
"""
add_pet = 1
view_all_pet = 2
count_available_adopted = 3
find_pet = 4


def display_menu():
 print("=== Pet Adoption Record===")
 print("1. add pet")
 print("2. view all pets")
 print("3. count available and adopted")
 print("4. find pet by a name") 
 pass
   
 pass

def add_pet(pet_list):
    name = input("Name of pet: ")
    if name == 1:
        pet_list.append(name)
    else:
        print("Input a name of pet")

def view_pets(pet_list):

    pet_list = ["Hamter", "Cat", "Dog", "Rabit"]
    
    pass

def count_available_adopted(pet_list):
  pet_list_available = ["Hamter", "Cat", "Dog",]
  pet_list_available.count(pet_list)
  pet_list_adopted = ["rabit"]
  pet_list_adopted.count(pet_list)

  pass

def find_pet(pet_list):
    pet_list = ["Hamter", "Cat", "Dog", "Rabit"]
    print("find pet")
    print(pet_list.find("Cat"))
  
    pass

def remove_pet(pet_list):
    print("Remove Pet")
    pet_list = ["Hamter", "Cat", "Dog", "Rabit"]
    pet_list.remove("Hamster")
    print(pet_list)
    
    pass

def main():
    running = True
    while running:
        choice = display_menu()
    print("=== Pet Adoption Record===")
    print("1. add pet")
    print("2. view all pets")
    print("3. count available and adopted")
    print("4. find pet by a name") 
    pass
        
main()