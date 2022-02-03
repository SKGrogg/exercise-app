# Overview

This app served as my final project for Intermediate Python Programming at the University of Chicago in August of 2021.

The app was built using FastAPI, and runs on Python and HTML. It was completed over the span of roughly four weeks, with the focus being primarily on back-end functionality. See below for the outlines of the original proposals and instructions on using the app.

A video walkthrough of the app and its expected functionality can be found here: https://www.youtube.com/watch?v=Wh1XKuhHl7Q

# Original Proposal

 I would like to create an API that helps introduce people into new exercising routines. I've found that starting to get into a fitness routine can be very intimidating, and I am hopeful my app will help to centralize the process.

My app will handle a select list of exercise modalities, which is currently restricted to the following: Running, Cycling, Swimming, Triathlon, Weight Lifting, Yoga, Cross-Training. It will have methods to:

- Take in one's general fitness goals and find online workout plans that might fit one (run a certain distance, do a certain type of yoga, heavy vs high rep lifting, etc). A stretch goal for this would be adding that plan to one’s Google Calendar using the Google Calender API mentioned in the Project Proposal Example, though I am unsure if I will be able to achieve this in time.
- Return a list of equipment/apparel one might need to begin exercise. If people would like to explore buying certain equipment, they can input their size and price restrictions per item and the program will return links to possible items.
- Take in a zip-code/city and return local groups (names, contact info) pertaining to that fitness routine
- Take in a zip-code and find local fitness facilities (locations, pricing if available) where one might go to workout
- Return a list of (and links to) popular books on the exercise with brief descriptions
- For race-based exercises (running, cycling, tri, etc), take in date range and zipcode to return a list of upcoming events

I will start by gathering all the different sites and data sources I will need. For example, sites like trifind.com, which can be used to find triathlon races close to a given zip code, datasets relating to zip codes that will allow me to calculate distances and restrict searches on that, and compiling my own relatively limited datasets regarding equipment for each exercise. After that, I will work on  getting the logic and methods up and running, and then work on the web searches/API integration.


My execution plan for the Project will follow this timeline:

End of Week 4: I will research and decide upon a web framework, and create a basic web app that allows the user to input their name, zipcode, shoe/clothing sizes, and desired type of exercise. I will also work to aggregate all external sites that my site will be referencing (i.e. sites to buy equipment/apparel, find gyms/pools, find races, workout plans)

End of Week 5: I will have a basic homepage, as well as classes for each type of exercise, which will include attributes for equipment/apparel of that each of the exercises, as well as writing out (but not implementing) the methods of each class.

End of Week 6: Finish writing all the methods for each class, returning stock answers for now just to ensure the logic works. I will also try to ensure I've made good progress with working out how to seach other sites based on user input and returning the results, though I may not be able to implement this week. Begin working on code for calculating adjacent zip-codes of the user.

End of Week 7: Continue figuring out how to return a specified range of search results from other websites (Amazon for materials, race websites for upcoming events, etc) and adding these external searches to the otherwise finished methods. Finish Zipcode search function. Begin work on Stretch Goal of adding workout plan/races to Google Calendar Via API.

End of Week 8: Finish external search result aspect of project. Clean up site appearance. Continue on Google Calendar stretch goal if time permits.

Final Touch-Ups: Work on User-Interface, finish any loose string, alter functionality of any methods I been unable to successfully create.

README FINAL


# GETTING STARTED

Ensure that you download the entirety of the "Final Project" folder from Github, which contains files app_main.py,
classes.py, Pipfile, Pipfile.lock, a "README final.txt" (which is a copy of this information), and a subfolder called Templates. All of those files are needed for
this app to run, so be sure they are all there.

This app is reliant on a the Pipenv virtual environment tool. Please be sure you have it installed on your
machine. If it it not, you can read how to install it here:

https://pipenv.pypa.io/en/latest/

Once you've ensure this step is complete and indexed into the "Final Project" Folder, initiate the virtual
environment with the following command:

$ pipenv shell


Once the shell has been launched, enter the following command to launch the app:

$ hypercorn app_main:app

This should result in a message along the lines of "Running on http://127.0.0.1:8000". Copy and paste that
URL into your browser.


# USING THE APP

The app is quite straightforward. Enter all requested information on the landing page. Zipcode is
restricted to inputs consisting of 5 numeric characters. Regardless of which exercise is chosen, once you
submit the first form, you will be brought to a page that asks for you to select some additional,
exercise-specific information. Select this and submit.

At this point, you will land on the exercise-specific page of the site. There will be some collection of
the following functionalities: "Find a Training Plan", "Find Equipment", "Find Books", "Find Facilities",
"Find Events". The specifics of which appear will be determined by which exercise you choose. For example,
there is no "Find Facilities" option for Running, and no "Find Events" option for Cycling, Swimming, or
Weightlifting.

The Training Plan returned will be dependent on the distance goals (Running, Swimming, Cycling, Triathlon)
or exercise type (Yoga, Weightlifting). There will be a hyperlink out to various sites on the Internet
where these plans can be found.

The Equipment that is returned will be based on your inputs to the previous forms, such as your shoe and
clothing sizes, gender category of clothing, and, in the case of Weightlifting, the budget. Hyperlinks to
all of these buying options will be included. In the event that you may need to buy equipment in a store
(running shoes, a bicycle), local shops near your zipcode will be displayed with hyperlinks to their Yelp
reviews.

The Books that are returned are specific to each exercise, but identical for all variations of a given
exercise. In other words, regardless of your aforementioned distance goals for exercise type, you will be
recommended the same books on your exercise. The page will display the book titles, the authors, and blurb
for the book, and a hyperlink to a site to buy a copy.

Find Facilities is tied exclusively to the zipcode that has been input. The results returned are based on
a Yelp search of the appropriate facilities (i.e. Spin Studios for Cycling, Gyms with Pools for Swimming,
etc). The names of the businesses will be displayed, with a hyperlink to their Yelp review pages.

The Events that a returned for the race-based exercises (Running, Triathlon) will be based on the user's
zip code and the distance they've chosen. The Events for Yoga are retreats across the country that cost
less than the budget specified by the user. A hyperlink is included to a site with a comprehensive list of
these events. 


# FINAL NOTE/CHANGES FROM ORIGINAL PROPOSAL

My original proposal include one more function for the exercises: Find_Groups. Unfortunately, my app is
heavily reliant on other sites that house the content needed by our users. I was unable to find sites that
helped with the search, and creating a database of these groups was outside the scope of this project, as
that would essentially be a final product in its own right. 

Similarly, though Swimming and Cycling may have benefitted from a Find_Events function, the sites that
were available invariably returned lackluster (and oftentimes unusable) results. With this in mind, I
decided to exclude this function for these two events.






