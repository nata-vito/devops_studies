from app.game_plat import CoursePlatform

def testFailStudentScoreToCripto():
    platform = CoursePlatform()
    assert platform.ScoreToCripto(
        5, 3) == 2, "O número de moedas especificadas não passaram no teste!"
