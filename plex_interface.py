import tkinter as tk
from tkinter import messagebox, filedialog
from plexapi.server import PlexServer
import pandas as pd

# Function to fetch titles from Plex
def fetch_titles():
    try:
        plex = PlexServer(url_entry.get(), token_entry.get())
        movies = plex.library.section('Movies').all()
        shows = plex.library.section('TV Shows').all()

        movie_titles = [movie.title for movie in movies]
        show_titles = [show.title for show in shows]

        titles = {
            'Movies': movie_titles,
            'TV Shows': show_titles
        }

        return titles

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to export titles to CSV
def export_to_csv():
    titles = fetch_titles()
    if titles:
        # Ask user for file location
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                                   filetypes=[("CSV files", "*.csv")])
        if file_path:
            # Create DataFrame and save to CSV
            df_movies = pd.DataFrame(titles['Movies'], columns=["Movies"])
            df_shows = pd.DataFrame(titles['TV Shows'], columns=["TV Shows"])

            # Concatenate DataFrames
            result = pd.concat([df_movies, df_shows], axis=1)

            result.to_csv(file_path, index=False)
            messagebox.showinfo("Success", "Titles exported successfully!")

# GUI setup
root = tk.Tk()
root.title("Plex Titles Exporter")

# Plex Server URL
url_label = tk.Label(root, text="Plex Server URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Plex Server Token
token_label = tk.Label(root, text="Plex Token:")
token_label.pack(pady=5)
token_entry = tk.Entry(root, width=50)
token_entry.pack(pady=5)

# Export Button
export_button = tk.Button(root, text="Export Titles to CSV", command=export_to_csv)
export_button.pack(pady=20)

# Run the GUI
root.mainloop()
