from app.game_plat import CoursePlatform 
  
def testStudentScoreToCripto():
    platform = CoursePlatform()
    assert platform.ScoreToCripto(3, 5) == 2, "O número de moedas especificadas não passaram no teste!"