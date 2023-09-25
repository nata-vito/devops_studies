from app.game_plat import CoursePlatform


def testPassIdUsers():
    platform = CoursePlatform()
    platform.RegisterUser(plan='Premium')
    assert platform.FindPremiumUsers(), "Não existe usuários premiuns"