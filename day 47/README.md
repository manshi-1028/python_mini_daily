# Day 46 - Spotify Time Machine

A Python project that creates a Spotify playlist containing the top songs from a specific date in the past.

## What This Project Does

The program asks the user for a date and then:

1. Searches the Billboard Hot 100 chart for that date.
2. Extracts the top 100 song titles.
3. Uses the Spotify API to search for those songs.
4. Creates a new private Spotify playlist.
5. Adds the songs to the playlist.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Spotify Web API
- Spotipy

## Music Time Machine
![day46](spotify_playlist.gif) 

## Project Structure

```text
Day-46-Spotify-Time-Machine/
│
├── main.py
├── README.md
└── requirements.txt
