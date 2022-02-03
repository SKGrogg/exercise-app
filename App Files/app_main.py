from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from classes import Athlete


app = FastAPI()
templates = Jinja2Templates(directory="templates")

#Global Declaration
athlete = Athlete("temp", 0, "temp", "temp", "temp", "temp")


@app.get("/")
def welcome(request: Request, name: Optional[str] = None, zipcode: Optional[int] = None , clothes: Optional[str] = None , gen_clothes: Optional[str] = None, shoes: Optional[str] = None ,\
    exercise: Optional[str] = None ):
  
    return templates.TemplateResponse("set_athlete.html", {"request": request, "name": name, "zipcode": zipcode, \
        "clothes": clothes, "gen_clothes": gen_clothes, "shoes": shoes, "exercise": exercise})
    
@app.post("/submission")
def submission_confirmation(request: Request, name: str = Form(...), zipcode: int = Form(...), clothes: str = Form(...), gen_clothes: str = Form(...), shoes: str = Form(...), exercise: str = Form(...)):
    
    global athlete
    athlete = Athlete(name, str(zipcode), shoes, clothes, gen_clothes, exercise)

    #redirect to appropriate addition information forms
    if exercise == "running":
        return templates.TemplateResponse("running_distance.html", {"request": request})
    elif exercise == "swimming":
        return templates.TemplateResponse("swimming_distance.html", {"request": request})
    elif exercise == "cycling":
        return templates.TemplateResponse("cycling_distance.html", {"request": request})
    elif exercise == "triathlon":
        return templates.TemplateResponse("triathlon_distance.html", {"request": request})
    elif exercise == "weightlifting":
        return templates.TemplateResponse("weightlifting_additional.html", {"request": request})
    elif exercise =="yoga":
        return templates.TemplateResponse("yoga_additional.html", {"request": request})
    else:
        raise ValueError #We should never get here


#RUNNER METHODS

@app.get("/runner_distance")
def runner_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("running_distance.html", {"request": request})

@app.post("/runner")
def runner(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)

    return templates.TemplateResponse("runner_control.html", {"request": request})

@app.get("/runner")
def runner(request: Request):
    
    return templates.TemplateResponse("runner_control.html", {"request": request})

@app.get(f'/runner/find_plan', response_class=HTMLResponse)
def runner_find_plan(): 

    text, link = athlete.exercise.find_plan()

    return f"""
    <html>
    <h1>
    <u><b>{athlete.exercise.distance.upper()} Training Plan:</b></u>
    </h1>
    <body>
        {text} Good luck, {athlete.name}!
    </body>
    <br>
    <br>
    <form action='{link}' target="_blank">
    <input type="submit" value="Offsite Training Plan" />
    </form>
    <br>
    <br>
    <form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """
    

@app.get('/runner/find_equipment', response_class=HTMLResponse)
def runner_find_equipment():

    lst = athlete.exercise.find_equipment(athlete)

    #If error raised during webscraping, kick out to Yelp
    if lst == []:
        return f"""
        <html>
        <h1>
        <u>Local shops that sell running shoes near {athlete.zipcode}</u>
        </h1>
        <body>
        <b><a href= "https://www.yelp.com/search?find_desc=running%20shoes&find_loc={athlete.zipcode}" target="_blank">See Shops</a></b>
        </body>
         <h1>
        <u>Shoes on Amazon</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+running+shoes+size+{athlete.shoes}&ref=nb_sb_noss_2" target="_blank">Shoes on Amazon</a></b>
            <br>
            <br>
        </body>
        <br>
        <br>
        <form action='/runner'>
        <input type="submit" value="Back To Runner Options" />
        </form>
        </html>
        """

    #If webscraping successful, display business names with links
    else:
        return f"""
        <html>
        <h1>
        <u>Local shops that sell running shoes near {athlete.zipcode}</u>
        </h1>
        <body>
            <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
        </body>
        <h1>
        <u>Shoes on Amazon</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+running+shoes+size+{athlete.shoes}&ref=nb_sb_noss_2" target="_blank">Shoes on Amazon</a></b>
            <br>
            <br>
        </body>
        <form action='/runner'>
        <input type="submit" value="Back To Runner Options" />
        </form>
        </html>
        """


@app.get('/runner/find_events', response_class=HTMLResponse)
def runner_find_events():

    url = athlete.exercise.find_events(athlete)

    return f"""
    <html>
    <h1>
     <u><b>Upcoming Races In Your Area</b></u>
    </h1>
    <body>
     <u><a href= "{url}" target="_blank">{athlete.exercise.distance.upper()} Races Near {athlete.zipcode}</a></u>
    </body>
    <br>
    <br>
    <form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """


@app.get('/runner/find_books', response_class=HTMLResponse)
def runner_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    <u>Here are some books on running that might inspire you:</u>
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[2][1]}" target="_blank">{books[2][0]}</a></b></u>
         <br>{books[2][2]}
    </body>

    <br><br>
    <br><form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """


#Swimmer METHODS

@app.get("/swimmer_distance")
def swimmer_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("swimmer_distance.html", {"request": request})

@app.post("/swimmer")
def swimmer(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)

    return templates.TemplateResponse("swimmer_control.html", {"request": request})

@app.get("/swimmer")
def swimmer(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("swimmer_control.html", {"request": request})

@app.get('/swimmer/find_plan', response_class=HTMLResponse)
def swimmer_find_plan(): 


    text, link = athlete.exercise.find_plan()

    return f"""
    <html>
     <h1>
    <u><b>{athlete.exercise.distance.upper()} Training Plan:</b></u>
    </h1>
    <body>
        {text} Good luck, {athlete.name}!
    </body>
    <br>
    <br>
    <form action='{link}' target="_blank">
    <input type="submit" value="Offsite Training Plan" />
    </form>
    <br>
    <br>
    <form action='/swimmer'>
    <input type="submit" value="Back To Swimmer Options" />
    </form>
    </html>
    """

@app.get('/swimmer/find_equipment', response_class=HTMLResponse)
def swimmer_find_equipment():

    lst = athlete.exercise.find_equipment(athlete)

    return f"""
    <html>
    <h1>
    <u>Swim Suits</u>
    </h1>
    <body>
        <b><a href= "{lst[0]}" target="_blank">Suits on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    <u>Goggles</u>
    </h1>
    <body>
        <b><a href= "{lst[1]}" target="_blank">Goggles on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    <u>Swim Caps</u>
    </h1>
    <body>
        <b><a href= "{lst[2]}" target="_blank">Swim Caps on Amazon</a></b>
        <br>
        <br>
    </body>
     <h1>
    <u>Training Extras</u>
    </h1>
    <body>
        <b><a href= "{lst[3]}" target="_blank">Training Accessories on Amazon</a></b>
        <br>
        <br>
    </body>
    <form action='/swimmer'>
    <input type="submit" value="Back To Swimmer Options" />
    </form>
    </html>
    """

@app.get('/swimmer/find_facilities', response_class=HTMLResponse)
def swimmer_find_facilities():

    lst = athlete.exercise.find_facilities(athlete)

    #If an error is raised during webscraping, kick out to other site
    if lst == []:
        return f"""
        <html>
        <h1>
        <u>Find Facilities</u>
        </h1>
        <body>
        <u><a href= "https://www.yelp.com/search?find_desc=gym%20pools&find_loc={athlete.zipcode}" target="_blank">Spin Studios Near {athlete.zipcode}</a></u>
        </body>
        <br>
        <br>
        <form action='/swimmer'>
        <input type="submit" value="Back To Swimmer Options" />
        </form>
        </html>
        """
    #If webscraping sucessful, display results of individual businesses with links
    else:
        return f"""
        <html>
        <h1>
        <u>Here are some gyms that seem to have pools near {athlete.zipcode}. </u>
        </h1>
        <body>
            <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
        </body>
        <br>
        <br>
        <form action='/swimmer'>
        <input type="submit" value="Back To Swimmer Options" />
        </form>
        </html>
        """


@app.get('/swimmer/find_books', response_class=HTMLResponse)
def swimmer_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    <u>Here are some books on swimming that might inspire you:</u>
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[2][1]}" target="_blank">{books[2][0]}</a></b></u>
         <br>{books[2][2]}
    </body>

    <br><br>
    <br><form action='/swimmer'>
    <input type="submit" value="Back To Swimmer Options" />
    </form>
    </html>
    """



#Cyclist METHODS

@app.get("/cycling_distance")
def cyclist_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("cycling_distance.html", {"request": request})

@app.post("/cyclist")
def cyclist(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)
    
    return templates.TemplateResponse("cyclist_control.html", {"request": request})

@app.get("/cyclist")
def cyclist(request: Request):
    
    return templates.TemplateResponse("cyclist_control.html", {"request": request})

@app.get('/cyclist/find_plan', response_class=HTMLResponse)
def cyclist_find_plan(): 


    text, link = athlete.exercise.find_plan()

    return f"""
    <html>
    <h1>
    <u><b>{athlete.exercise.distance.upper()} Training Plan:</b></u>
    </h1>
    <body>
        {text} Good luck, {athlete.name}!
    </body>
    <br>
    <br>
    <form action='{link}' target="_blank">
    <input type="submit" value="Offsite Training Plan" />
    </form>
    <br>
    <br>
    <form action='/cyclist'>
    <input type="submit" value="Back To Cyclist Options" />
    </form>
    </html>
    """

@app.get('/cyclist/find_equipment', response_class=HTMLResponse)
def cyclist_find_equipment():

    lst = athlete.exercise.find_equipment(athlete)

    str = ""

    #If Error in WebScraping, Add a Link Directly to Yelp
    if lst == []:
        str = str + f"""
        <html>
        <h1>
        <u>Picking out a bike is best done in person. Here are some local Bike Shops near you.</u>
        </h1>
        <body>
        <u><a href= "https://www.yelp.com/search?find_desc=bike+shops&find_loc={athlete.zipcode}&ns=1" target="_blank">Bike Shops Near {athlete.zipcode}</a></u>
        </body>
        <br>
        <br>
        """

    #If webscraping successful, display the individual businesses
    else:
        str = str + f"""
        <html>
        <h1>
        <u>Picking out a bike is best done in person. Here are some local shops near you.</u>
        </h1>
        <body>
            <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
        </body>
        """

    #add standard links to other equipment regardless of webscraping success
    str = str + f"""
        <h1>
        <u>Here are some helmets on Amazon.</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+helments&ref=nb_sb_noss_2" target="_blank">Helmets on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are cycling shoes on Amazon.</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+shoes+size+{athlete.shoes}&ref=nb_sb_noss_1" target="_blank">Shoes on Amazon</a></b>
            <br>
            <br>
        </body>
        <form action='/cyclist'>
        <input type="submit" value="Back To Cyclist Options" />
        </form>
        </html>
        """
    
    return str

@app.get('/cyclist/find_facilities', response_class=HTMLResponse)
def cylist_find_facilities():

    lst = athlete.exercise.find_facilities(athlete)

    #If Error in WebScraping, Add a Link Directly to Yelp
    if lst == []:
        return f"""
        <html>
        <h1>
        <u>Spin Studios</u>
        </h1>
        <body>
        <u><a href= "https://www.yelp.com/search?find_desc=spin+studios&find_loc={athlete.zipcode}&ns=1" target="_blank">Spin Studios Near {athlete.zipcode}</a></u>
        </body>
        <br>
        <br>
        <form action='/cyclist'>
        <input type="submit" value="Back To Cyclist Options" />
        </form>
        </html>
        """

    #If Webscraping Successful
    else:
        return f"""
        <html>
        <h1>
        <u>Here are some Spin Studios near you.</u>
        </h1>
        <body>
            <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
        </body>
        <br>
        <br>
        <form action='/cyclist'>
        <input type="submit" value="Back To Cyclist Options" />
        </form>
        </html>
        """

@app.get('/cyclist/find_books', response_class=HTMLResponse)
def cyclist_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    <u>Here are some books on cyling that might inspire you:</u>
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>

    <br><br>
    <br><form action='/cyclist'>
    <input type="submit" value="Back To Cyclist Options" />
    </form>
    </html>
    """

#Triathlete METHODS

@app.get("/triathlon_distance")
def triathlete_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("triathlete_distance.html", {"request": request})

@app.post("/triathlete")
def triathlete(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)
    
    return templates.TemplateResponse("triathlete_control.html", {"request": request})

@app.get("/triathlete")
def triathlete(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("triathlete_control.html", {"request": request})

@app.get('/triathlete/find_plan', response_class=HTMLResponse)
def triathlete_find_plan(): 


    text, link = athlete.exercise.find_plan()

    return f"""
    <html>
    <h1>
    <u><b>{athlete.exercise.distance.upper()} Training Plan:</b></u>
    </h1>
    <body>
        {text} Good luck, {athlete.name}!
    </body>
    <br>
    <br>
    <form action='{link}' target="_blank">
    <input type="submit" value="Offsite Training Plan" />
    </form>
    <br>
    <br>
    <form action='/triathlete'>
    <input type="submit" value="Back To Triathlete Options" />
    </form>
    </html>
    """

@app.get('/triathlete/find_equipment', response_class=HTMLResponse)
def triathlete_find_equipment():

    run_lst, bike_lst, swim_lst = athlete.exercise.find_equipment(athlete)

    if run_lst == [] or bike_lst == []:
        return f"""
        <html>
        <h1>
        <u>Local shops that sell running shoes near {athlete.zipcode}</u>
        </h1>
        <body>
        <b><a href= "https://www.yelp.com/search?find_desc=running%20shoes&find_loc={athlete.zipcode}" target="_blank">See Shops</a></b>
        </body>
        <br>
        <h1>
        <u>Running Shoes on Amazon.</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+running+shoes+size+{athlete.shoes}&ref=nb_sb_noss_2" target="_blank">Shoes on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Picking out a bike is best done in person. Here are some local shops near you.</u>
        </h1>
        <body>
        <u><a href= "https://www.yelp.com/search?find_desc=bike+shops&find_loc={athlete.zipcode}&ns=1" target="_blank">Bike Shops Near {athlete.zipcode}</a></u>
        </body>
        <h1>
        <u>Here are some helmets on Amazon.</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+helments&ref=nb_sb_noss_2" target="_blank">Helmets on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are cycling shoes on Amazon.</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+shoes+size+{athlete.shoes}&ref=nb_sb_noss_1" target="_blank">Shoes on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are swim suits on Amazon.</u>
        </h1>
        <body>
            <b><a href= "{swim_lst[0]}" target="_blank">Suits on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are goggles on Amazon.</u>
        </h1>
        <body>
            <b><a href= "{swim_lst[1]}" target="_blank">Goggles on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are swim caps on Amazon.</u>
        </h1>
        <body>
            <b><a href= "{swim_lst[2]}" target="_blank">Swim Caps on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are some swim training extras.</u>
        </h1>
        <body>
            <b><a href= "{swim_lst[3]}" target="_blank">Training Accessories on Amazon</a></b>
            <br>
            <br>
        </body>
        <form action='/triathlete'>
        <input type="submit" value="Back To Triathlete Options" />
        </form>
        </html>
        """

    else:
        return f"""
        <html>
        <h1>
        <u>Here are some local shops that sell running shoes near you.</u>
        </h1>
        <body>
            <b><a href= "https://{run_lst[0][1]}" target="_blank">{run_lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{run_lst[1][1]}" target="_blank">{run_lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{run_lst[2][1]}" target="_blank">{run_lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{run_lst[3][1]}" target="_blank">{run_lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{run_lst[4][1]}" target="_blank">{run_lst[4][0]}</a></b>
        </body>
        <h1>
        <u>Running shoes on Amazon.</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+running+shoes+size+{athlete.shoes}&ref=nb_sb_noss_2" target="_blank">Shoes on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Picking out a bike is best done in person. Here are some local shops near you. </u>
        </h1>
        <body>
            <b><a href= "https://{bike_lst[0][1]}" target="_blank">{bike_lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{bike_lst[1][1]}" target="_blank">{bike_lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{bike_lst[2][1]}" target="_blank">{bike_lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{bike_lst[3][1]}" target="_blank">{bike_lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{bike_lst[4][1]}" target="_blank">{bike_lst[4][0]}</a></b>
        </body>
        <h1>
        <u>Here are some helmets on Amazon.</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+helments&ref=nb_sb_noss_2" target="_blank">Helmets on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are cycling shoes on Amazon.</u>
        </h1>
        <body>
            <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+shoes+size+{athlete.shoes}&ref=nb_sb_noss_1" target="_blank">Shoes on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are swim suits on Amazon.</u>
        </h1>
        <body>
            <b><a href= "{swim_lst[0]}" target="_blank">Suits on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are goggles on Amazon.</u>
        </h1>
        <body>
            <b><a href= "{swim_lst[1]}" target="_blank">Goggles on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are Swim Caps on Amazon.</u>
        </h1>
        <body>
            <b><a href= "{swim_lst[2]}" target="_blank">Swim Caps on Amazon</a></b>
            <br>
            <br>
        </body>
        <h1>
        <u>Here are some swim training extras.</u>
        </h1>
        <body>
            <b><a href= "{swim_lst[3]}" target="_blank">Training Accessories on Amazon</a></b>
            <br>
            <br>
        </body>
        <form action='/triathlete'>
        <input type="submit" value="Back To Triathlete Options" />
        </form>
        </html>
        """
    

@app.get('/triathlete/find_facilities', response_class=HTMLResponse)
def triathlete_find_facilities():

    swim_lst, bike_lst = athlete.exercise.find_facilities(athlete)

    #If webscraping fails, kick out to other site
    if swim_lst == [] or bike_lst == []:
            return f"""
        <html>
        <h1>
        <u>Here are some places near you that may have Spin Classes.</u>
        </h1>
        <body>
        <u><a href= "https://www.yelp.com/search?find_desc=spin+studios&find_loc={athlete.zipcode}&ns=1" target="_blank">Spin Studios Near {athlete.zipcode}</a></u>
        </body>
        <br>
        <br>
        <h1>
        <u>Here are some gyms that seem to have pools.</u>
        </h1>
        <body>
        <u><a href= "https://www.yelp.com/search?find_desc=gym%20pools&find_loc={athlete.zipcode}" target="_blank">Pools Near {athlete.zipcode}</a></u>
        </body>
        <br>
        <br>
        <form action='/triathlete'>
        <input type="submit" value="Back To Triathlete Options" />
        </form>
        </html>
        """

    #If webscraping successful, display individual business names
    else:
        return f"""
        <html>
        <h1>
        <u>Here are some places near you that may have Spin Classes.</u>
        </h1>
        <body>
            <b><a href= "https://{bike_lst[0][1]}" target="_blank">{bike_lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{bike_lst[1][1]}" target="_blank">{bike_lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{bike_lst[2][1]}" target="_blank">{bike_lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{bike_lst[3][1]}" target="_blank">{bike_lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{bike_lst[4][1]}" target="_blank">{bike_lst[4][0]}</a></b>
        </body>
        <br>
        <h1>
        <u>Here are some gyms that seem to have pools.</u>
        </h1>
        <body>
            <b><a href= "https://{swim_lst[0][1]}" target="_blank">{swim_lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{swim_lst[1][1]}" target="_blank">{swim_lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{swim_lst[2][1]}" target="_blank">{swim_lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{swim_lst[3][1]}" target="_blank">{swim_lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{swim_lst[4][1]}" target="_blank">{swim_lst[4][0]}</a></b>
        </body>
        <br>
        <br>
        <form action='/triathlete'>
        <input type="submit" value="Back To Triathlete Options" />
        </form>
        </html>
        """

@app.get('/triathlete/find_events', response_class=HTMLResponse)
def triathlete_find_events():

    url, state = athlete.exercise.find_events(athlete)

    return f"""
    <html>
    <h1>
     <u><b>Upcoming Races In Your Area</b></u>
    </h1>
    <body>
     <u><a href= "{url}" target="_blank">{athlete.exercise.distance.upper()} Triathlon In {state}</a></u>
    </body>
    <br>
    <br><form action='/triathlete'>
    <input type="submit" value="Back To Triathlete Options" />
    </form>
    </html>
    """

@app.get('/triathlete/find_books', response_class=HTMLResponse)
def triathlete_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    Here are some books on Triathlons that might inspire you:
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>

    <br><br>
    <br><form action='/triathlete'>
    <input type="submit" value="Back To Triathlete Options" />
    </form>
    </html>
    """

#WeightLifter METHODS

@app.get("/weightlifter_additional")
def weightlifter_additional(request: Request, weight: Optional[str] = None, budget: Optional[str] = None):

    return templates.TemplateResponse("weightlifter_additional.html", {"request": request})

@app.post("/weightlifter")
def weightlifter(request: Request, weight: str = Form(...), budget: str = Form(...)):

    athlete.exercise.set_additional(weight, budget)
    
    return templates.TemplateResponse("weightlifter_control.html", {"request": request})

@app.get("/weightlifter")
def weightlifter(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("weightlifter_control.html", {"request": request})

@app.get('/weightlifter/find_plan', response_class=HTMLResponse)
def weightlifter_find_plan(): 

    if athlete.exercise.weight == "bodyweight":
        one, two, three = athlete.exercise.find_plan()
        str = f"""
                <html>
                <h1>
                <u><b>{athlete.exercise.weight.upper()} Training Plan:</b></u>
                </h1>
                <h2>
                {one[0]}
                </h2>
                <form action='{one[1]}' target="_blank">
                <input type="submit" value="Six-Week Beginners Plan" />
                </form>
                <br>
                <h2>
                    {two[0]}
                </h2>
                <form action='{two[1]}' target="_blank">
                <input type="submit" value="Plan with Video Examples" />
                </form>
                <br>
                <h2>
                {three[0]}
                </h2>
                <form action='{three[1]}' target="_blank">
                <input type="submit" value="Collection of Bodyweight Exercises" />
                </form>
                <br>
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                </html>
                """
    elif athlete.exercise.weight == "highrep" or athlete.exercise.weight == "heavy":
        text, link = athlete.exercise.find_plan()
        str = f"""
                <html>
                <h1>
                <u><b>{athlete.exercise.weight.upper()} Training Plan:</b></u>
                </h1>
                <body>
                {text}
                </body>
                <br>
                <br>
                <form action='{link}' target="_blank">
                <input type="submit" value="Offsite Training Plan" />
                </form>
                <br>
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                </html>
                """
    else: #Should never get here
        str = f"""
        <form action='/'>
        <input type="submit" value="Start Over!" />
        </form>
        """
    
    return str

@app.get('/weightlifter/find_equipment', response_class=HTMLResponse)
def weightlifter_find_equipment():

    results = athlete.exercise.find_equipment()


    #Standard header
    str = f"""
                <html>
                <h1>
                <u>{results[0]}</u>
                </h1>
            """

    #Amount of items returned/displayed will vary depending on Athlete's Budget
    for equip in results[1:]:
        str = str + f"""<body>
                    <u><b><a href= "{equip[1]}" target="_blank">{equip[0]}</a></b></u>
                    </body>
                    <br>
                    <br>
                    """
    
    #Standard Bottom ont the page
    str = str + f"""
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                </html>
                """

    return str
    
  
@app.get('/weightlifter/find_books', response_class=HTMLResponse)
def weightlifter_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    <u>Here are some books on weightlifting that might inspire you:</u>
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>

    <br><br>
    <br><form action='/weightlifter'>
    <input type="submit" value="Back To Weightlifter Options" />
    </form>
    </html>
    """

@app.get('/weightlifter/find_facilities', response_class=HTMLResponse)
def weightlifter_find_facilities():

    lst = athlete.exercise.find_facilities(athlete)

    #If Webscraping fails, kick out to Yelp
    if lst == []:
        return f"""
        <html>
        <h1>
        <u>Here are some gyms near you.</u>
        </h1>
        <body>
        <u><a href= "https://www.yelp.com/search?find_desc=gyms&find_loc={athlete.zipcode}&ns=1" target="_blank">Gyms Near {athlete.zipcode}</a></u>
        </body>
        <br>
        <br>
        <form action='/weightlifter'>
        <input type="submit" value="Back To Weightlifter Options" />
        </form>
        </html>
        """
    
    #If webscraping succeeds, display local gyms with links
    else:
        return f"""
        <html>
        <h1>
        <u>Here are some gyms near you.</u>
        </h1>
        <body>
            <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
        </body>
        <br>
        <br>
        <form action='/weightlifter'>
        <input type="submit" value="Back To Weightlifter Options" />
        </form>
        </html>
        """

#Yogi METHODS

@app.get("/yogi_additional")
def yogi_additional(request: Request, practice: Optional[str] = None, budget: Optional[str] = None):

    return templates.TemplateResponse("yoga_additional.html", {"request": request})

@app.post("/yogi")
def yogi(request: Request, practice: str = Form(...), budget: str = Form(...)):

    athlete.exercise.set_additional(practice, budget)
    return templates.TemplateResponse("yogi_control.html", {"request": request})

@app.get("/yogi")
def yogi(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("yogi_control.html", {"request": request})


@app.get("/yogi/find_plan", response_class=HTMLResponse)
def yogi_find_plan():

    vid1, vid2, vid3, web1, web2 = athlete.exercise.find_plan()
    
    return f"""
            <html>
            <h1>
            <u><b>{athlete.exercise.practice.upper()} Practice Plans:</b></u>
            </h1>
            <h2>
            {athlete.name}, here are some routines on Youtube you can follow along with:
            </h2>
            <body>
            <b><a href= "{vid1[1]}" target="_blank">Courtesy of the {vid1[0]} channel</a></b>
            <br>
             <br>
             <b><a href= "{vid2[1]}" target="_blank">Courtesy of the {vid2[0]} channel</a></b>
            <br>
             <br>
             <b><a href= "{vid3[1]}" target="_blank">Courtesy of the {vid3[0]} channel</a></b>
            <br>
            <h2>
            Here are some links to sights with a collection of poses, for when you begin create your own routines!
            </h2>
            <body>
            <b><a href= "{web1[1]}" target="_blank">{web1[0]}</a></b>
            <br>
            <br>
            <b><a href= "{web2[1]}" target="_blank">{web2[0]}</a></b>
            <br>
            <br>
            <form action='/yogi'>
            <input type="submit" value="Back To Yogi Options" />
            </form>
            </html>
            """

@app.get('/yogi/find_equipment', response_class=HTMLResponse)
def yogi_find_equipment():

    mat_url, clothes_url = athlete.exercise.find_equipment(athlete)

    return f"""
    <html>
    <h1>
    <u>Yoga Mats</u>
    </h1>
    <body>
        <b><a href= "{mat_url}" target="_blank">Yoga Mats on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    <u>Clothing</u>
    </h1>
    <body>
        You can practice Yoga in anything loose and comfortable, but if you feel you need to look the part, you can find some clothing below:
        <br>
        <br>
        <b><a href= "{clothes_url}" target="_blank">Yoga Attire on Amazon</a></b>
        <br>
        <br>
    </body>
    
    <form action='/yogi'>
    <input type="submit" value="Back To Yogi Options" />
    </form>
    </html>
    """

@app.get('/yogi/find_books', response_class=HTMLResponse)
def yogi_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    <u>Here are some books on Yoga that might inspire you:</u>
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[2][1]}" target="_blank">{books[2][0]}</a></b></u>
         <br>{books[2][2]}
    </body>

    <br><br>
    <br><form action='/yogi'>
    <input type="submit" value="Back To Yogi Options" />
    </form>
    </html>
    """

@app.get('/yogi/find_facilities', response_class=HTMLResponse)
def yogi_find_facilities():

    lst = athlete.exercise.find_facilities(athlete)

    #If webscraping fails, kick out to Yelp
    if lst == []:
        return f"""
        <html>
        <h1>
        <u>Here are some yoga studios near you.</u>
        </h1>
        <body>
            <b><a href= "https://www.yelp.com/search?find_desc=yoga%20studios&find_loc={athlete.zipcode}" target="_blank">Yoga Studios Near {athlete.zipcode}</a></b>
        
        </body>
        <br>
        <br>
        <form action='/yogi'>
        <input type="submit" value="Back To Yogi Options" />
        </form>
        </html>
        """

    #If webscraping succeeds, display local Yoga studios with links
    else:
        return f"""
        <html>
        <h1>
        <u>Here are some yoga studios near you.</u>
        </h1>
        <body>
            <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
        </body>
        <body>
            <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
        </body>
        <body>
        <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
        </body>
        <br>
        <br>
        <form action='/yogi'>
        <input type="submit" value="Back To Yogi Options" />
        </form>
        </html>
        """

@app.get('/yogi/find_events', response_class=HTMLResponse)
def yogi_find_events():

    url = athlete.exercise.find_events()

    return f"""
    <html>
    <h1>
     <u><b>Upcoming Retreats</b></u>
    </h1>
    <body>
     <u><b><a href= "{url}" target="_blank">Retreats Under ${athlete.exercise.budget}</a></b></u>
    <br><br>
    </body>
    <br><form action='/yogi'>
    <input type="submit" value="Back To Yogi Options" />
    </form>
    </html>
    """