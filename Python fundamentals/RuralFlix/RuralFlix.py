from User import User
from Video import Video



user_hugo = User('Hugo Medeiros', 'hugokaua2002@gmail.com', 'Hugo@2323', 'rua tantan', 55)

user_hugo.verifyBilling()
print(f'Your plan: {user_hugo.plan} \nYour credit: ${user_hugo.card}')

user_hugo.changePlan()
print(f'Your plan: {user_hugo.plan} \nYour credit: ${user_hugo.card}')

video = Video('Homem de ferro', 100)


video.play()
video.advance()
video.comeBack()
video.comeBack()
video.advance()
video.advance()
video.advance()
video.advance()
video.advance()
video.advance()
video.advance()
video.advance()
