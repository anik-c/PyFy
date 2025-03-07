
# PyFy Music Player

PyFy is a Python-based music player application built upon a **circular doubly linked list** data structure - a sophisticated implementation choice that creates a perpetual, bidirectional playlist experience. This advanced data structure forms the foundation of the entire application, enabling a seamless, loop-friendly music playback experience with efficient navigation in both directions.

## Core Data Structure: Circular Doubly Linked List

The application's architecture fundamentally revolves around a **circular doubly linked list** implementation which:
- Connects each song to both its previous and next songs, creating a complete circular chain
- Provides constant O(1) time complexity for both forward and backward traversal operations
- Enables perfect playlist looping - when reaching the last song, the next operation seamlessly returns to the first song
- Creates a continuous, never-ending playback experience through circular connections
- Allows songs to be added or removed from any position while maintaining the circular integrity

## Features Powered by Circular Doubly Linked List

- **Seamless Looping**: The circular nature ensures continuous playback without manual restart
- **Bidirectional Navigation**: Move forward or backward through songs with identical performance
- **Efficient Playlist Manipulation**: Add or remove songs anywhere in the playlist while preserving circular connections
- **Position Memory**: The current node tracks playback position in the circular structure
- **Intuitive Controls**: User-friendly interface that leverages the circular doubly linked list implementation

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies using the following command:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your MP3 files in the same directory as the `main.py` file.
2. Run the `main.py` script using the following command:
    ```sh
    python main.py
    ```
3. Use the graphical interface to control your circular playlist.

## Controls

- **Play**: Begin playback from current position in the circular list
- **Pause/Resume**: Pause or resume the current song without losing position in the list
- **Next**: Traverse forward to the next node in the circular linked list
- **Prev**: Traverse backward to the previous node in the circular linked list
- **Exit**: Close the application

