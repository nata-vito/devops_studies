from app.main import CoursePlatform


def testPassScoreToCourse():
    platform = CoursePlatform()
    platform.RegisterUser()
    platform.RegisterUser()
    platform.users[0].forum = 2
    platform.RegisterUser()
    platform.users[1].forum = 5
    assert platform.Bonus(), 'Não há usuários ativos no forum'