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
    def setUp(self):
        # Create a temporary file with some initial recipes for testing
        self.filename = "test_recipes.txt"
        with open(self.filename, 'w') as file:
            file.write("Pasta,Spaghetti\n")
            file.write("Salad,Lettuce,Tomato,Cucumber\n")

    def tearDown(self):
        # Delete the temporary file after testing
        import os
        os.remove(self.filename)

    def test_load_recipes(self): #Sriram
        
    def test_add_recipe(self): #Sriram
        
    def test_delete_recipe(self): #Daniel
        
    def test_display_recipe(self): #Daniel
        
    def test_list_recipes(self): #Arafat
        
    def test_edit_recipe(self): #Arafat
        
    def test_search_recipe_book(self): #Dimitri
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
