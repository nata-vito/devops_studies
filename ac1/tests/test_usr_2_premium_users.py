from app.game_plat import CoursePlatform

def testIdUsers():
    platform = CoursePlatform()
    platform.RegisterUser(plan='Premium')
    assert platform.FindPremiumUsers(), "Não existe usuários premiuns"