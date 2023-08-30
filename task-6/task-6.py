import os
import telebot
import requests
import csv
import tempfile

# TODO: 1.1 Get your environment variables
yourkey = "48d7ca7b"
bot_id = "6196380352:AAHx5TUnJbUqX8qvLQNuM603U-_Nch_a9E8"
bot = telebot.TeleBot(bot_id)
moviesinfo = []


@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    bot.reply_to(message,
                 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    bot.reply_to(message, 'Bye!\nHave a good time')


@bot.message_handler(commands=['help'])
def helpProvider(message):
    bot.reply_to(message, ('1.0 You can use "/movie MOVIE_NAME" command to get the details of a particular movie.'
                           '\n2.0. You can use "/export" command to export all the movie data in CSV format.'
                           '\n3.0. You can use "/stop" or the command "/bye" to stop the bot.'))


@bot.message_handler(commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    mName = ' '.join(message.text.split()[1:])
    response = requests.get(f'http://www.omdbapi.com/?t={mName}&apikey={yourkey}')
    data = response.json()
    if data['Response'] == 'True':
        title = data['Title']
        plot = data['Plot']
        genre = data['Genre']
        imdb = data['imdbRating']
        year = data['Year']
        pic = data['Poster']
# TODO: 2.1 Create a CSV file and dump the movie information in it
        moviesinfo.append([title, plot, genre, imdb, year,])
       # TODO: 1.3 Show the movie information in the chat window
        bot.send_photo(message.chat.id, pic)
        bot.reply_to(message, f"Title: {title}\nPlot: {plot}\nGenre: {genre}\nYear: {year}\nimdbRating: {imdb}")
    else:
        bot.reply_to(message, "Sorry, we couldn't find the particular movie.")


@bot.message_handler(commands=['export'])
def getFile(message):
    bot.reply_to(message, 'Generating file...')
    # TODO: 2.2 Send downlodable CSV file to telegram chat
    with open("movies_list.csv", "w") as file:
        movie_list = file.name
        movies = csv.writer(file)
        movies.writerow(['Title', 'Year', 'Plot', 'Genre', 'imdbRating'])
        movies.writerows(moviesinfo)
    with open(movie_list, 'rb') as file:
        bot.send_document(message.chat.id, file)
        bot.reply_to(message, "Download the CSV file here")
    os.remove(movie_list)

@bot.message_handler(func=lambda m: True)
def default(message):
    bot.reply_to(message, 'I did not understand \N{confused face}')

bot.infinity_polling()