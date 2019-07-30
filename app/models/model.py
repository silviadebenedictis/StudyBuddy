
McGill_University = [{"course": "Math 222: Multivariable calculus",
                    "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm",
                    "date" : "Tuesday's and Thursday's" ,
                    "location": "Le James McGill Bookstore"}]




University_of_Michgan = [{"course": "CS 101: Intro to CS" ,
                        "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm",
                        "date" : "Wednesday's Friday's" ,
                        "location": "Gerlad R. Ford Presidental Library, Willam L. Clements Library"}]




Hunter = [{"course": "Pre 101: Precalculus" ,
                    "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
                    "date" : "Monday's and Thursdays" ,
                    "location": "Leon & Toby Cooperman Library"}]
[{"course": "WGS 10000 : Women Gender Studies" ,
                    "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
                    "date" : "Wednesday's and Friday's" ,
                    "location": "Leon & Toby Cooperman Library"}]



City= [{"course": "PHIL 20100 - Philosophy",
                "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm",
                "date" : "Tuesday's and Thursday's" ,
                "location": "Cohen Library"}]

Baruch= [{"course": "CIS 2300" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : "Tuesday's and Thursday's" ,
            "location": "Newman Library"}]

Harvard = [{"course": "CS50: Intro to CS" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : "Monday's Wednesday's Friday's" ,
            "location": "Widener Library , Lamont Library"}]
            

BMCC= [{"course": "CSC 101: Intro to CS" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : "Tuesday's Thursday's" ,
            "location": "A.Philp Randolph Library"}]
        
CityTech = [{"course": "MAT 1375: Precalculus" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : "Monday's and Wednesday's " ,
            "location": "Ursula C. Schwerin Library"}]
[{"course": "MAT 1475 Calculus" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
             "date" : "Thursday's and Tuesday's" ,
            "location": "Ursula C. Schwerin Library"}]

Utica = [{"course": "CRJ 333: Information Security" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : " Tuesday's and Thursday's" ,
            "location": "Frank E. Gannett Memorial Library"}]
            
BrownUni = [{"course": "Math 0350: Multivariable Calculus " ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : "Monday's, Wednesday's,Friday's " ,
            "location": "John Carter Brown Library,John D. Rockefeller Jr Library "}]


Babson = [{"course": "DES 3600: Design and System Thinking" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : "Monday's and Wednesday's " ,
            "location": "Horn Library"}]

Howard= [{"course": "HIST 005/006 Intro to Black Diaspora" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : "Thursday's and Tuesday's" ,
            "location": "Founders Library, School of Divinity Collection at HU Law Library"}]


Columbia= [{"course": "Calculus 2" ,
            "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
            "date" : "Monday's and Friday's" ,
            "location": "Butler Library"}]
[{"course": "COMS W1004:Intro to CS" ,
                    "time" : "10:30 am 12:30 pm 2:30pm 4:30pm 6:30pm 8:30pm" ,
                    "date" : "Monday's and Thursdays" ,
                    "location": "Leon & Toby Cooperman Library"}]

            

def search(college,course):
    for x in college:
        if x ['course'] == course:
            return x
    
