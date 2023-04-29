

class Movie():
    def __init__(self, title, director, duration):
      self.title = title
      self.director = director
      self.duration = duration
      print("Movie objesi oluşturuldu.")
      
    def __str__(self):
       return f"{self.title} by {self.director}"
   
    def __len__(self):
        print("Movie Duration")
        return self.duration
    
    def __del__(self):
        print("Movie Delete")
      
      
m = Movie("Movie name","Director name", 120)

print(m)
#print(str(m))


