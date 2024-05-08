from replit import clear
import time

class Movie:
  def __init__(self, name, date):
    self.name = name
    self.date = date
    
movies = []

while True:
  clear()
  
  if len(movies) > 0:
    for movie in movies:
      print(f"[{movies.index(movie) + 1}] {movie.name}, {movie.date}")
    print("----------------")
  else:
    print("No books yet!")
    print("----------------")
  
  print("1 - Add a book | 2 - Remove a book | X - End")
  
  next = input()
  if next.upper() == "X":
    clear()
    print("Goodbye!")
    time.sleep(1)
    break
  
  # Next Step
  
  if next == "1":
    clear()
    
    newMovieName = input("Enter book name: ")
    newMovieDate = input("Enter book's date: ")
    
    newMovie = Movie(newMovieName, newMovieDate)
    
    movies.append(newMovie)
  
  elif next == "2":
    clear()
    for movie in movies:
      print(f"[{movies.index(movie) + 1}] {movie.name}, {movie.date}")
    print("----------------")
    removeBook = int(input("Enter book id: "))
    movies.pop(removeBook - 1)