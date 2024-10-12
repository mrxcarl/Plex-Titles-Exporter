# Plex Titles Exporter

**Plex Titles Exporter** is a Python application that allows users to easily extract movie and TV show titles from a Plex Media Server and export them to a CSV file. This simple GUI-based tool utilizes the `tkinter` library for the user interface and the `plexapi` library to interact with the Plex server.

## Features

- Connect to your Plex Media Server using the server URL and authentication token.
- Retrieve and list all movie and TV show titles from your library.
- Export the retrieved titles to a CSV file for easy access and sharing.

## Requirements

- Python 3.x
- `plexapi`
- `pandas`
- `tkinter` (included with standard Python installations)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/plex-titles-exporter.git
   cd plex-titles-exporter
   ```

2. Install the required packages:
   ```bash
   pip install plexapi pandas
   ```

## Usage

1. Run the application:
   ```bash
   python plex_exporter.py
   ```

2. Enter your Plex Server URL and authentication token in the provided fields.

3. Click the "Export Titles to CSV" button and choose a location to save the CSV file containing your movie and TV show titles.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
