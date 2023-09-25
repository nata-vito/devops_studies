from app.game_plat import CoursePlatform


def testScoreToCourse():
    platform = CoursePlatform()
    platform.RegisterUser()
    platform.RegisterUser()
    platform.users[0].forum = 2
    platform.RegisterUser()
    platform.users[1].forum = 5
    assert platform.Bonus(), 'Não há usuários ativos no forum'
