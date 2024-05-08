import unittest
from unittest.mock import patch
from io import StringIO
from main import Recipe, RecipeBook
"""
This file is the Unit Testing file for our main program. Unit tests should have
thorough comments to ensure we can easily trace issues back to the source and 
read what we are testing.
"""

class TestRecipeBook(unittest.TestCase):
    def setUp(self): #Dimitri
        # Create a temporary file with some initial recipes for testing
        self.filename = "test_recipes.txt"
        with open(self.filename, 'w') as file:
            file.write("Pasta,Spaghetti\n")
            file.write("Salad,Lettuce,Tomato,Cucumber\n")

    def tearDown(self): #Dimitri
        # Delete the temporary file after testing
        import os
        os.remove(self.filename)

    def test_load_recipes(self): #Sriram, 1st Unit Test
        
        
    def test_add_recipe(self): #Sriram, 2nd Unit Test
        
        
    def test_delete_recipe(self): #Daniel, 1st Unit Test
        # Create a RecipeBook object

        recipe_book = RecipeBook(self.filename)

 

        # Test deleting an existing recipe

        recipe_book.delete_recipe("Salad")

        self.assertEqual(len(recipe_book.recipes), 1)  # Check if the recipe is deleted

 

        # Test deleting a non-existing recipe

        recipe_book.delete_recipe("Burger")  # Burger recipe doesn't exist

        self.assertEqual(len(recipe_book.recipes), 1)  # Check if the recipes remain unchanged
        
    def test_display_recipe(self): #Daniel, 2nd Unit Test
          # Create a RecipeBook object

        recipe_book = RecipeBook(self.filename)

 

        # Test displaying an existing recipe

        with patch('sys.stdout', new=StringIO()) as fake_out:

            recipe_book.display_recipe("Pasta")

            output = fake_out.getvalue().strip()

            self.assertIn("Recipe: Pasta", output)  # Check if the recipe is found
        
    def test_list_recipes(self): #Arafat, 1st Unit Test
          # Create a RecipeBook object
        recipe_book = RecipeBook(self.filename)
        # Test listing recipes
        with patch('sys.stdout', new=StringIO()) as fake_out:
            recipe_book.list_recipes()
            output = fake_out.getvalue().strip()
            self.assertIn("Recipes:", output)  # Check if recipes are listed
        
    def test_edit_recipe(self): #Arafat, 2nd Unit Test
         # Create a RecipeBook object
        recipe_book = RecipeBook(self.filename)
        # Test editing an existing recipe
        with patch('builtins.input', side_effect=["yes", "Cheese, Pepperoni"]):
            recipe_book.edit_recipe("Pasta")
            self.assertEqual([ingredient.strip() for ingredient in recipe_book.recipes[0].ingredients], ["Cheese", "Pepperoni"])


    def test_search_recipe_book(self): #Dimitri, Only Unit Test
        # Create a RecipeBook object
        recipe_book = RecipeBook(self.filename)

        # Test searching for an existing recipe
        with patch('sys.stdout', new=StringIO()) as fake_out:
            recipe_book.search_recipe_book("Pasta")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "Recipe 'Pasta' is in Recipe Book.")

        # Test searching for a non-existing recipe
        with patch('sys.stdout', new=StringIO()) as fake_out:
            recipe_book.search_recipe_book("Burger")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "Recipe 'Burger' not found in Recipe Book.")

if __name__ == '__main__':
    unittest.main()
