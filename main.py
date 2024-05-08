class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class RecipeBook:
    def __init__(self, filename):
        self.filename = filename
        self.recipes = self.load_recipes()

    def load_recipes(self):
        """
        Driver: Sriram
        Navigator: Daniel
        """      
        
    def add_recipe(self, recipe):
        """
        Driver: Sriram
        Navigator: Daniel
        """          
        
    def delete_recipe(self, name):
        """
        Driver: Daniel
        Navigator: Sriram
        """    
        
    def display_recipe(self, name):
        """
        Driver: Daniel
        Navigator: Sriram
        """    
             
    def list_recipes(self):
        """
        Driver: Arafat 
        Navigator: Dimitri
        """  
              
    def edit_recipe(self, name):
        """
        Driver: Arafat 
        Navigator: Dimitri
        """
    def search_recipe_book(self, name):
        """
        Driver: Dimitri 
        Navigator: Arafat
        """
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                print(f"Recipe '{name}' is in Recipe Book.")
                return
        print(f"Recipe '{name}' not found in Recipe Book.")
        
def main():
    """
    Driver: Dimitri 
    Navigator: Arafat
    """
    recipe_book = RecipeBook("recipes.txt")

    while True:
        print("-------------------------------")
        print("1. List Recipes")
        print("2. Search Recipe Book")
        print("3. Display Recipe")
        print("4. Add Recipe")
        print("5. Edit Recipe")
        print("6. Delete Recipe")
        print("7. Exit")
        choice = input("Enter your choice: ")
        print("-------------------------------")
        if choice == '1':
            recipe_book.list_recipes()
        elif choice == '2':
            name = input("Enter recipe name to search in Recipe Book: ")
            recipe_book.search_recipe_book(name)
        elif choice == '3':
            name = input("Enter recipe name to display: ")
            recipe_book.display_recipe(name)
        elif choice == '4':
            name = input("Enter recipe name to add: ")
            ingredients = input("Enter ingredients (separated by commas): ").split(',')
            recipe = Recipe(name, ingredients)
            recipe_book.add_recipe(recipe)
        elif choice == '5':
            name = input("Enter recipe name to edit: ")
            recipe_book.edit_recipe(name)
        elif choice == '6':
            name = input("Enter recipe name to delete: ")
            recipe_book.delete_recipe(name)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please select valid option.")

if __name__ == "__main__":
    main()
