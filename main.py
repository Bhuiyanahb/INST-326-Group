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
        Driver: Sriram (1st Function)
        Navigator: Daniel
        """      
        try:
            with open(self.filename, 'r') as file:
                recipes = []
                for line in file:
                    name, *ingredients = line.strip().split(',')
                    recipes.append(Recipe(name, ingredients))
                return recipes
        except FileNotFoundError:
            return []
        
    def add_recipe(self, recipe):
        """
        Driver: Sriram (2nd Function)
        Navigator: Daniel
        """          
        if any(existing_recipe.name.lower() == recipe.name.lower() for existing_recipe in self.recipes):
            print("This recipe already exists.")
            return
        
        with open(self.filename, 'a') as file:
            file.write(f"{recipe.name},{','.join(recipe.ingredients)}\n")
        print("Recipe added")

        self.recipes = self.load_recipes()
        print(f"Total recipes: {len(self.recipes)}")
        
    def delete_recipe(self, name):
        """
        Driver: Daniel (1st Function)
        Navigator: Sriram
        """    
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                self.recipes.remove(recipe)
                # Update the file with the modified list of recipes
                with open(self.filename, 'w') as file:
                    for recipe in self.recipes:
                        file.write(f"{recipe.name},{','.join(recipe.ingredients)}\n")
                print(f"Recipe '{name}' deleted.")
                return
            
        # Recipe not found
        print("Recipe not found.")
        
    def display_recipe(self, name):
        """
        Driver: Daniel (2nd Function)
        Navigator: Sriram
        """    
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                print(f"Recipe: {recipe.name}")
                print("Ingredients:")
                for ingredient in recipe.ingredients:
                    print("-", ingredient)
                return
        print("Recipe not found")   
          
    def list_recipes(self):
        """
        Driver: Arafat (1st Function)
        Navigator: Dimitri
        """  
        if not self.recipes:
            print("No recipes found.")
            return False
        
        print("Recipes:")
        for recipe in self.recipes:
            print(f"- {recipe.name}")
        print(" ")
        print("End of List")
        
        return True   
    
    def edit_recipe(self, name):
        """
        Driver: Arafat (2nd Function)
        Navigator: Dimitri
        """
        found_recipe = None
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                found_recipe = recipe
                break

        if found_recipe:
            print("Recipe found:")
            print(f"Name: {found_recipe.name}")
            print("Ingredients:")
            for ingredient in found_recipe.ingredients:
                print("-", ingredient)

            choice = input("Do you want to edit this recipe? (yes/no): ")
            if choice.lower() == 'yes':
                new_ingredients = input("Enter new ingredients (separated by commas): ").split(',')
                found_recipe.ingredients = new_ingredients

                # Update the file with the modified list of recipes
                with open(self.filename, 'w') as file:
                    for recipe in self.recipes:
                        file.write(f"{recipe.name},{','.join(recipe.ingredients)}\n")

                # Update the recipes list with the modified recipe
                self.recipes = self.load_recipes()

                print("Recipe updated successfully.")
            else:
                print("Recipe not modified.")
        else:
            print("Recipe not found.")
            
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
