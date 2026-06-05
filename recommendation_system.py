import tkinter as tk
from tkinter import messagebox
movies = {
    "Action": ["Avengers", "John Wick", "Mission Impossible"],
    "Comedy": ["Mr. Bean", "Home Alone", "The Mask"],
    "Science Fiction": ["Interstellar", "Avatar", "The Martian"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"]
}
def recommend():
    genre = genre_var.get()
    if genre in movies:
        recommendations = "\n".join(movies[genre])
        result_label.config(
            text=f"Recommended Movies:\n{recommendations}")
    else:
        messagebox.showinfo(
            "Recommendation",
            "Please select a genre.")
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("400x300")
title = tk.Label(
    root,
    text="Movie Recommendation System",
    font=("Arial", 14))
title.pack(pady=10)
genre_var = tk.StringVar()
genres = ["Action", "Comedy", "Science Fiction", "Horror"]
dropdown = tk.OptionMenu(
    root,
    genre_var,
    *genres)
dropdown.pack(pady=10)
btn = tk.Button(
    root,
    text="Get Recommendations",
    command=recommend)
btn.pack(pady=10)
result_label = tk.Label(
    root,
    text="Select a genre",
    font=("Arial", 12))
result_label.pack(pady=20)
root.mainloop()