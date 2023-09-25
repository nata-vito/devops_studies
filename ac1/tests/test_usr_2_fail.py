from app.game_plat import CoursePlatform


def testFailIdUsers():
    platform = CoursePlatform()
    platform.RegisterUser()
    assert platform.FindPremiumUsers(), "Não existe usuários premiuns"
