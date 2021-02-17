import webbrowser

print(' 1 Finished Animes \n 2 Waiting for new episodes \n 3 Episodes coming out steadily \n 4 Episodes exist \n 5 Watchlist')

number = int(input("Enter a number: "))

# Just paste your link between the '' and you are good to go

if number == 1:
    # Finished Animes
    webbrowser.open('')
if number == 2:
    # Waiting for new episodes
    webbrowser.open('')
if number == 3:
    # Episodes coming out steadily
    webbrowser.open('')
if number == 4:
    # Episodes exist
    webbrowser.open('')
if number == 5:
    # Watchlist
    webbrowser.open('')
