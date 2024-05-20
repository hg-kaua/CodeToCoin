from User import User
from Video.Video import Video
from Video.Film import Film
from Video.Series import Series



user_hugo = User('Hugo Medeiros', 'hugokaua2002@gmail.com', 'Hugo@2323', 'rua tantan', 55)

user_hugo.verifyBilling()
print(f'Your plan: {user_hugo.plan} \nYour credit: ${user_hugo.card}')

user_hugo.changePlan()
print(f'Your plan: {user_hugo.plan} \nYour credit: ${user_hugo.card}')

video = Video('Homem de ferro', 100, 2008)


video.play()
video.advance()
video.comeBack()
video.comeBack()
video.advance()

batman = Film('Batman - Cavaleiro das trevas', 70, 2010)

print(batman.title)
batman.play()
batman.stop()
batman.advance()
batman.advance()
batman.advance()
batman.advance()
batman.comeBack()


series_data = Series('The flash', 40, 2014)
series_data2 = Series('Suits', 40, 2016)
series_data3 = Series('Greys anatomy', 40, 2004)

print(Series.all)


