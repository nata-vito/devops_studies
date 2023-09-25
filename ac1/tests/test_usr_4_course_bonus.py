from app.game_plat import CoursePlatform

def testScoreToCourse():
    platform = CoursePlatform()
    platform.RegisterUser()
    assert platform.Bonus(), 'Não há usuários ativos no forum'