import tkinter as tk
from tkinter import simpledialog

def add_recipe():
    # Prompt the user to add a recipe to a text file
    recipe_name = simpledialog.askstring("Add Recipe", "Enter recipe name:")
    if recipe_name:
        with open("recipes.txt", "a") as file:
            file.write(recipe_name + "\n")
        print(f"Recipe '{recipe_name}' added successfully!")

def search_recipes():
    # Prompt the user to search for a recipe name
    search_term = simpledialog.askstring("Search Recipe", "Enter recipe name to search:")
    if search_term:
        with open("recipes.txt", "r") as file:
            recipes = file.readlines()
            found_recipes = [recipe.strip() for recipe in recipes if search_term.lower() in recipe.lower()]
            if found_recipes:
                print(f"Found recipes containing '{search_term}':")
                for recipe in found_recipes:
                    print(recipe)
            else:
                print(f"No recipes found containing '{search_term}'.")

# Create the main window
root = tk.Tk()
root.title("Recipe App")

# Set the size of the window
root.geometry("400x300")  # Set width to 400 pixels and height to 300 pixels

# Create a frame to hold the welcome label
welcome_frame = tk.Frame(root)
welcome_frame.pack(padx=20, pady=10)

# Create the welcome label with white text
welcome_label = tk.Label(welcome_frame, text="Welcome", font=("Arial", 14), fg='white')
welcome_label.pack()

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=20, pady=10)

# Create the "Add Recipe" button with white background and black text
add_button = tk.Button(button_frame, text="Add Recipe", command=add_recipe, bg='white', fg='black')
add_button.pack(side=tk.TOP, padx=5, pady=5)

# Create the "Search Recipes" button with white background and black text
search_button = tk.Button(button_frame, text="Search Recipes", command=search_recipes, bg='white', fg='black')
search_button.pack(side=tk.TOP, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
