import requests
from uszipcode import SearchEngine



class Exercise():

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def find_plan():
        pass

    def find_equipment():
        pass

    def find_books():
        pass

    def find_facilities():
        pass

    def find_events():
        pass

class Running (Exercise):

    def __init__(self):

        super().__init__()

    def __repr__(self):
       return f"Running, {self.distance}"

    def set_distance(self, distance):
        self.distance = distance

    #Return Plan based on Race Distance
    def find_plan(self):

        if self.distance == "mile":
            return "You can find a training program courtesy of verywellfit.com at the link below. Make sure to start slow, walk when needed, and have fun!",\
                 "https://www.verywellfit.com/learn-to-run-continuously-2911965"
        elif self.distance == "5k":
            return "You can find a training program courtesy of The Mayo Clinic at the link below.",\
                 "https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/5k-run/art-20050962"
        elif self.distance == "10k":
            return "You can find a training program courtesy of Brooks Running at the link below.",\
                 "https://www.brooksrunning.com/en_us/blog/training-workouts/10k-training-for-beginner-and-advanced-runners.html"
        elif self.distance == "half+marathon":
            return "You can find a training program courtesy of Runners' World at the link below.",\
                 "https://www.runnersworld.com/uk/training/half-marathon/a25887045/beginner-half-marathon-training-schedule/"
        elif self.distance == "marathon":
            return "You can find a training program courtesy of Runners' World at the link below.", "https://www.runnersworld.com/uk/training/a760108/rws-basic-marathon-schedules-get-you-round/"
        elif self.distance == "ultra+marathon":
            return "You can find a training program courtesy of Runners' World at the link below. Please be warned: An ultra-marathon is not recommended for inexperiences runners. Proceed with caution",\
                "https://www.runnersworld.com/uk/training/ultra/a774983/16-week-50-mile-ultra-marathon-training-schedule/"


     #Just Shoes
    
    #Returns local shoes stores and online options
    def find_equipment(self, athlete):

        #Sometimes the web scraping here does not work. Error handle just in case
        try:
            url = "https://www.yelp.com/search/snippet?find_desc=running%20shoes&find_loc="+str(athlete.zipcode)+"&request_origin=user"

            response = requests.get(url)
            response_data = response.json()
            searchPageProps = response_data['searchPageProps']
            consumerHeaderProps = searchPageProps['mainContentComponentsListProps']

            lst = []
            for i in range(3,8):
                cur_dict = consumerHeaderProps[i]
                lst.append((f'Store Name: {cur_dict.get("searchResultBusiness").get("name")}', \
                f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))
            
            return lst

        except:
            return []

    #Static list of books, with URL and description
    def find_books(self):

        lst = [["'Born To Run', by Christopher McDougall", "https://www.amazon.com/Born-Run-Hidden-Superathletes-Greatest/dp/0307279189/ref=sr_1_5?keywords=Books+on+Running&qid=1636644863&qsid=140-5700113-7714932&sr=8-5&sres=0307279189%2C1465489576%2C0936070854%2C014312319X%2C0578230437%2C1937715418%2C0345528808%2C1579659888%2CB073Z4CXFZ%2C1609618025%2CB09K1WVDJ3%2C1609619196%2C0764207598%2C173352\
            7303%2CB078PMQPH7%2C0593231716%2C1782551654%2C1482046628%2C161448242X%2C1635651832&srpt=ABIS_BOOK", "At the heart of Born to Run lies a mysterious tribe of Mexican Indians, the Tarahumara, who live quietly in canyons and are reputed to be the best distance runners in the world; in 1993, one of them, aged 57, came first in a prestigious 100-mile race wearing a toga and sandals. A small \
                group of the world's top ultra-runners (and the awe-inspiring author) make the treacherous journey into the canyons to try to learn the tribe's secrets and then take them on over a course 50 miles long. \n\
                With incredible energy and smart observation, McDougall tells this story while asking what the secrets are to being an incredible runner. Travelling to labs at Harvard, Nike, and elsewhere, he comes across an incredible cast of characters, including the woman who recently broke the world record for 100 miles and for her encore ran a 2:50 marathon in a bikini, pausing to down a beer at the 20 mile mark."],\
                ["'The Ultimate Beginner's Guide to Running', by Ryan Roberts", "https://www.amazon.com/Ultimate-Beginners-Running-Guide-Inspired/dp/1482046628/ref=sr_1_1_sspa?crid=3U9F0SUS8KV2T&keywords=books+on+running+for+beginners&qid=1636644926&sprefix=Books+on+Running+for+%2Caps%2C173&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyV1VBODRXMFg2QU5EJmVuY3J5cHRlZElkPUEwODczMjE1MjQxQUVOR0lZM1FNTiZlbmNyeXB0ZWRBZElkPUEwNjMxMDMyM0ZFVzJGQlpOSk1IMSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",\
                     "Several years ago Ryan Robert noticed his niece was having body image issues. She obsessed about her weight and let it take control of her life. Eventually she even lost the confidence she once effortlessly displayed.\n\
                        As an avid runner, Ryan knew if he was able to get his niece to start running she would gain self-confidence, better mental and physical acuity. It would also allow her a better focus on health rather than weight. Ryan started writing notes to his niece about different aspects of running. These notes became the impetus for his book Running Inspired.\n\
                            Running Inspired provides a wealth of information for the non-runner and beginning runner. The book covers everything from proper form, to shoes, to running plans, and food. There is also information on how to stay motivated including visualization exercises. These are the tools Ryan used to teach his niece to run inspired and they will help you too."],
                            ["'What I Talk About When I Talk About Running', by Haruki Murakami", "https://www.amazon.com/dp/B0015DWJ8W/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1",\
                                "An intimate look at writing, running, and the incredible way they intersect, What I Talk About When I Talk About Running is an illuminating glimpse into the solitary passions of one of our greatest artists.\n\
                                    While training for the New York City Marathon, Haruki Murakami decided to keep a journal of his progress. The result is a memoir about his intertwined obsessions with running and writing, full of vivid recollections and insights, including the eureka moment when he decided to become a writer. By turns funny and sobering, playful and philosophical, here is a rich and revelatory work that elevates the human need for motion to an art form."]]

        return lst

    #racefinder
    def find_events(self, athlete):

        url = f"https://www.active.com/search?keywords={self.distance}+race&include_virtual_events=1&location={athlete.zipcode}&category=Activities&daterange=All+future+dates"
        
        return url

class Swimming(Exercise):
    def __init__(self,):
        super().__init__()
       
    def __repr__(self):
        return f"Swimming, {self.distance}"

    def set_distance(self, distance):
       self.distance = distance

    #Return Plan based on Race Distance
    def find_plan(self):
        
        if self.distance == "mile":
            return "You can find a training program courtesy of outdoorswimmer.com at the link below. Make sure to start slow, take breaks when needed, and have fun!",\
                 "https://outdoorswimmer.com/guides/couch-to-1-mile-training-plan"
        elif self.distance == "5k":
            return "You can find a training program courtesy of MacMillion Cancer Support at the link below.",\
                 "https://www.macmillan.org.uk/assets/swim-training-plan-5k-improver.pdf"
        elif self.distance == "10k":
            return "You can find a training program courtesy of outdoorswimmer.com at the link below.",\
                 "https://outdoorswimmer.com/guides/10k-training-plan"

    #Swim suits based on clothing size and gender category, goggles, swim caps
    def find_equipment(self, athlete):
        
        return [f"https://www.amazon.com/s?k={athlete.gen_clothes}+competitive+swimsuits+{athlete.clothes}&ref=nb_sb_noss", \
            "https://www.amazon.com/s?k=swim+goggles+competitive&crid=32YJIV94RJNIO&sprefix=swim+goggles+compe%2Caps%2C169&ref=nb_sb_ss_ts-doa-p_1_18", \
                "https://www.amazon.com/s?k=Swim+Caps&ref=nb_sb_noss_2",\
                    "https://www.amazon.com/s?k=swim+accessories+for+lap+swimming&crid=LSFIQRMWDXLR&sprefix=Swim+ac%2Caps%2C165&ref=nb_sb_ss_ts-doa-p_3_7"]

    def find_books(self):

        lst = [["'Why We Swim', by Bonnie Tsui", "https://www.amazon.com/dp/B07WJ1NH6N/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1", "We swim in freezing Arctic waters and piranha-infested rivers to test our limits. \
            We swim for pleasure, for exercise, for healing. But humans, unlike other animals that are drawn to water, are not naturalborn swimmers. We must be taught. Our evolutionary ancestors learned for survival;\
                 today, swimming is one of the most popular activities in the world. Why We Swim is propelled by stories of Olympic champions, a Baghdad swim club that meets in Saddam Hussein’s former palace pool,\
                      modern-day Japanese samurai swimmers, and even an Icelandic fisherman who improbably survives a wintry six-hour swim after a shipwreck. New York Times contributor Bonnie Tsui, a swimmer herself, dives into the deep, \
                          from the San Francisco Bay to the South China Sea, investigating what it is about water that seduces us, and why we come back to it again and again."],\
                ["'Swimming to Antarctica: Tales of a Long-Distance Swimmer', by Lynne Cox", "https://www.amazon.com/dp/B002NXORCE/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1",\
                     "Lynne Cox trained hard from age nine, working with an Olympic coach, swimming five to twelve miles each day in the Pacific. At age eleven, she swam even when hail made the water “like cold tapioca pudding” and was told\
                          she would one day swim the English Channel. Four years later—not yet out of high school—she broke the men’s and women’s world records for the Channel swim. In 1987, she swam the Bering Strait from America to the Soviet \
                              Union—a feat that, according to Gorbachev, helped diminish tensions between Russia and the United States.\n\
                         Lynne Cox’s relationship with the water is almost mystical: she describes swimming as flying, and remembers swimming at night through flocks of flying fish the size of mockingbirds, remembers being escorted by a pod of\
                              dolphins that came to her off New Zealand.\n\
                             She has a photographic memory of her swims. She tells us how she conceived of, planned, and trained for each, and re-creates for us the experience of swimming (almost) unswimmable bodies of water, including her most\
                                  recent astonishing one-mile swim to Antarctica in thirty-two-degree water without a wet suit. She tells us how, through training and by taking advantage of her naturally plump physique, she is able to create more\
                                       heat in the water than she loses."],
                            ["'Swimming Studies', by Leanne Shapton", "https://www.amazon.com/dp/B0072NWK88/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1",\
                                "Swimming Studies is a brilliantly original, meditative memoir that explores the worlds of competitive and recreational swimming. From her training for the Olympic trials as a teenager to enjoying pools and beaches \
                                    around the world as an adult, Leanne Shapton offers a fascinating glimpse into the private, often solitary, realm of swimming. Her spare and elegant writing reveals an intimate narrative of suburban adolescence, \
                                        spent underwater in a discipline that continues to inspire Shapton’s work as an artist and author. Her illustrations throughout the book offer an intuitive perspective on the landscapes and imagery of the sport.\
                                             Shapton’s emphasis is on the smaller moments of athletic pursuit rather than its triumphs. For the accomplished athlete, aspiring amateur, or habitual practicer, this remarkable work of written and visual \
                                                 sketches propels the reader through a beautifully personal and universally appealing exercise in reflection."]]

        return lst

    #Find local lap pools 
    def find_facilities(self, athlete):

        try:
            #Get JSON results from Yelp and Index into the right dictionary
            response = requests.get(f'https://www.yelp.com/search/snippet?find_desc=gym%20pools&find_loc={athlete.zipcode}&request_origin=user')
            response_data = response.json()
            searchPageProps = response_data['searchPageProps']
            consumerHeaderProps = searchPageProps['mainContentComponentsListProps']

            lst = []
            #For the top five results from Yelp, save their review page urls and Business names
            for i in range(3,8):
                cur_dict = consumerHeaderProps[i]
                lst.append((f'Gym Name: {cur_dict.get("searchResultBusiness").get("name")}', \
                f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))


            return lst

        except:
            return []

class Cycling(Exercise):

    def __init__(self):

        super().__init__()

    def __repr__(self):
        return f"Cycling, {self.distance}"

    def set_distance(self, distance):
        self.distance = distance

    #Return Plan based on Race Distance
    def find_plan(self):
        if self.distance == "30+miles":
            return "You can find a training program courtesy of the BayCare Clininc at the link below. Make sure to start slow, ride safe, and have fun!",\
                 "https://www.baycare.net/media/3266/30-mile-plan-baycare-clinic-century-ride.pdf"
        elif self.distance == "60+miles":
            return "You can find a training program courtesy of Mpora.com at the link below.",\
                 "https://mpora.com/road-cycling/60-mile-bike-ride-training-plan/"
        elif self.distance == "century":
            return "You can find a training program courtesy of The Best Buddies Challenge at the link below.",\
                 "https://www.bestbuddieschallenge.org/hp/12-week-century-training-blog/"

    #Direct People to local bike shops
    def find_equipment(self, athlete):


        #Sometimes the web scraping here does not work. Error handle just in case
        try:
            #Get JSON results from Yelp and Index into the right dictionary
            response = requests.get(f'https://www.yelp.com/search/snippet?find_desc=bike%20shops&find_loc={athlete.zipcode}&request_origin=user')
            response_data = response.json()
            searchPageProps = response_data['searchPageProps']
            hovercardData = searchPageProps['searchMapProps']['hovercardData']

            lst = []

            #For the top five results from Yelp, save their review page urls and Business names
            #Unlike other yelp searches, this one stored as a dictionary, so need a counter to break after 5 results
            counter = 0
            for key in hovercardData.keys():
                if counter >=5:
                    break
                cur_dict = hovercardData[key]
                lst.append((f'Bike Shop: {cur_dict.get("name")}', \
                f'yelp.com{cur_dict.get("businessUrl")}'))
                counter +=1
            
            return lst

        except AttributeError:
            return []
        except KeyError:
            return []

    def find_books(self):

        lst = [["'It's All About the Bike: The Pursuit of Happiness on Two Wheels', by Robert Penn", "https://www.amazon.com/dp/B004QO965G/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1",\
             "Robert Penn has saddled up nearly every day of his adult life. In his late twenties, he pedaled 25,000 miles around the world. Today he rides to get to work, sometimes for \
                 work, to bathe in air and sunshine, to travel, to go shopping, to stay sane, and to skip bath time with his kids. He's no Sunday pedal pusher. So when the time came for a \
                     new bike, he decided to pull out all the stops. He would build his dream bike, the bike he would ride for the rest of his life; a customized machine that reflects the joy of cycling. \
                         It's All About the Bike follows Penn's journey, but this book is more than the story of his hunt for two-wheel perfection. En route, Penn brilliantly explores the culture, science, \
                             and history of the bicycle. From artisanal frame shops in the United Kingdom to California, where he finds the perfect wheels, via Portland, Milan, and points in between, his trek \
                                 follows the serpentine path of our love affair with cycling. It explains why we ride."],\
                ["'Back in the Frame: Cycling, Belonging and Finding Joy on a Bike', by Jools Walker", "https://www.amazon.com/dp/B07QWKMJDS/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1",\
                     "Jools Walker rediscovered cycling aged 28 after a decade-long absence from the saddle. When she started blogging about her cycle adventures under the alias Lady Vélo, \
                         a whole world was opened up to her. But it's hard to find space in an industry not traditionally open to women - especially women of colour. Shortly after getting back on two wheels, \
                             Jools was diagnosed with depression and then, in her early thirties, hit by a mini-stroke. Yet, through all of these punctures, one constant remained: Jools' love of cycling Funny, \
                                 moving and motivational, this book tells the story of how Jools overcame these challenges, stepped outside her comfort zone and learned to cycle her own path. Along the way she \
                                     shares a wealth of inspirational stories and tips from other female trailblazers, and shows how cycling can and should be a space for everyone. A celebration of cycling, Back \
                                         in the Frame will motivate you to get back on your bike and enjoy the ride, no matter what life throws at you."]]
                                         
        return lst
        
    #Return spinning locations
    def find_facilities(self, athlete):

        
        #Sometimes the web scraping here does not work. Error handle just in case
        try:
            #Get JSON results from Yelp and Index into the right dictionary
            response = requests.get(f'https://www.yelp.com/search/snippet?find_desc=spin%20studios&find_loc={athlete.zipcode}&request_origin=user')
            response_data = response.json()
            searchPageProps = response_data['searchPageProps']
            consumerHeaderProps = searchPageProps['mainContentComponentsListProps']
            lst = []

            #For the top five results from Yelp, save their review page urls and Business names
            for i in range(3,8):
                cur_dict = consumerHeaderProps[i]
                lst.append((f'Spin Studio: {cur_dict.get("searchResultBusiness").get("name")}', \
                f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))
        
            return lst
        except:
            return []

class Triathlon(Exercise): 

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Triathlon, {self.distance}"

    def set_distance(self, distance):
        self.distance = distance

    #Return Plan based on Race Distance
    def find_plan(self):
        
        if self.distance == "sprint":
            return "You can find a training program courtesy of triathlete.com at the link below. Make sure to start slow, take breaks when needed, and have fun!",\
                 "https://www.triathlete.com/training/getting-started/8-week-sprint-triathlon-training-plan-beginners/"
        elif self.distance == "olympic":
            return "You can find a training program courtesy of triathlete.com at the link below.",\
                 "https://www.triathlete.com/training/olympic-triathlon-16-week-training-plan/"
        elif self.distance == "half+ironman":
            return "You can find a training program courtesy of triathlete.com at the link below.",\
                 "https://www.triathlete.com/training/20-week-training-plan-first-70-3-triathlon/"
        elif self.distance == "ironman":
            return "You can find a training program courtesy of ironman.com at the link below.",\
                 "https://www.ironman.com/news_article/show/1040088"
        else:
            return "We're experiencing technical difficulties, please stand by.",\
                "/"

    #Equipment for all three exercises
    def find_equipment(self, athlete):

        try:
            #Get all the local running show stores
            run_url = "https://www.yelp.com/search/snippet?find_desc=running%20shoes&find_loc="+str(athlete.zipcode)+"&request_origin=user"

            #Get JSON results from Yelp for Running Shops and Index into the right dictionary
            run_response = requests.get(run_url)
            run_response_data = run_response.json()
            run_searchPageProps = run_response_data['searchPageProps']
            run_consumerHeaderProps = run_searchPageProps['mainContentComponentsListProps']

            run_lst = []

            #For the top five results from Yelp, save their review page urls and Business names
            for i in range(3,8):
                cur_dict = run_consumerHeaderProps[i]
                run_lst.append((f'Store Name: {cur_dict.get("searchResultBusiness").get("name")}', \
                f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))

            
            #Get all local bike shops
            #Get JSON results from Yelp for bike shops and Index into the right dictionary
            bike_response = requests.get(f'https://www.yelp.com/search/snippet?find_desc=bike%20shops&find_loc={athlete.zipcode}&request_origin=user')
            bike_response_data = bike_response.json()
            bike_searchPageProps = bike_response_data['searchPageProps']
            hovercardData = bike_searchPageProps['searchMapProps']['hovercardData']

            bike_lst = []

            #For the top five results from Yelp, save their review page urls and Business names
            #Unlike other yelp searches, this one stored as a dictionary, so need a counter to break after 5 results
            counter = 0
            for key in hovercardData.keys():
                if counter >=5:
                    break
                cur_dict = hovercardData[key]
                bike_lst.append((f'Bike Shop: {cur_dict.get("name")}', \
                f'yelp.com{cur_dict.get("businessUrl")}'))
                counter +=1

            swim_lst = [f"https://www.amazon.com/s?k={athlete.gen_clothes}+competitive+swimsuits+{athlete.clothes}&ref=nb_sb_noss", \
                "https://www.amazon.com/s?k=swim+goggles+competitive&crid=32YJIV94RJNIO&sprefix=swim+goggles+compe%2Caps%2C169&ref=nb_sb_ss_ts-doa-p_1_18", \
                    "https://www.amazon.com/s?k=Swim+Caps&ref=nb_sb_noss_2",\
                        "https://www.amazon.com/s?k=swim+accessories+for+lap+swimming&crid=LSFIQRMWDXLR&sprefix=Swim+ac%2Caps%2C165&ref=nb_sb_ss_ts-doa-p_3_7"]

            
            return run_lst, bike_lst, swim_lst
        
        except:
            swim_lst = [f"https://www.amazon.com/s?k={athlete.gen_clothes}+competitive+swimsuits+{athlete.clothes}&ref=nb_sb_noss", \
                "https://www.amazon.com/s?k=swim+goggles+competitive&crid=32YJIV94RJNIO&sprefix=swim+goggles+compe%2Caps%2C169&ref=nb_sb_ss_ts-doa-p_1_18", \
                    "https://www.amazon.com/s?k=Swim+Caps&ref=nb_sb_noss_2",\
                        "https://www.amazon.com/s?k=swim+accessories+for+lap+swimming&crid=LSFIQRMWDXLR&sprefix=Swim+ac%2Caps%2C165&ref=nb_sb_ss_ts-doa-p_3_7"]
            return [], [], swim_lst


    def find_books(self):
        
        lst = [["'The Triathlete's Training Bible: The World’s Most Comprehensive Training Guide, 4th Ed', by Joe Friel",\
             "https://www.amazon.com/The-Triathletes-Training-Bible-audiobook/dp/B07YM4V71M/ref=sr_1_3?crid=QRBV41X9N7D3&keywords=the+triathletes+training+bible&qid=1637681671&qsid=140-5700113-7714932&sprefix=the+traithl%2Caps%2C176&sr=8-3&sres=1937715442%2C1934030198%2C1931382425%2C1976357861%2C1937715639%2C1937715744%2C1937715825%2C1931382921%2C0446696765%2C0738234680%2C1101904607%2C1521447292%2C1782550844%2C1484946790%2C194800707X%2CB09M59KND8&srpt=ABIS_BOOK",\
             "Joe Friel is the most trusted coach in the world, and his proven triathlon training program has helped hundreds of thousands find success in the sport of triathlon.\
                 Joe has completely rewritten this new fourth edition of The Triathlete's Training Bible to incorporate new training principles and help athletes train smarter than ever.\
                     The Triathlete’s Training Bible equips triathletes of all abilities with every detail they must consider when planning a season, lining up a week of workouts, or preparing for race day."],\
                ["'A Life Without Limits: A World Champion's Journey', by Chrissie Wellington", "https://www.amazon.com/dp/B005EM8NQ2/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1",\
                     "In 2007, Chrissie Wellington shocked the triathlon world by winning the Ironman World Championships in Hawaii. As a newcomer to the sport and a complete unknown to the press, Chrissie's win shook up the sport.\
                          A LIFE WITHOUT LIMITS is the story of her rise to the top, a journey that has taken her around the world, from a childhood in England, to the mountains of Nepal, to the oceans of New Zealand, and the trails of Argentina, and first across the finish line.\
                         Wellington's first-hand, inspiring story includes all the incredible challenges she has faced--from anorexia to near--drowning to training with a controversial coach. But to Wellington, the drama of the sports also presents an opportunity to use sports to improve people's lives."]]
                                         
        return lst

    #Find Spin Studios and Gyms with Pools
    def find_facilities(self, athlete):
        
        #Sometimes webscraping fails. Error Handling Just in Case
        try:
            swim_response = requests.get(f'https://www.yelp.com/search/snippet?find_desc=gym%20pools&find_loc={athlete.zipcode}&request_origin=user')
            swim_response_data = swim_response.json()
            swim_searchPageProps = swim_response_data['searchPageProps']
            swim_consumerHeaderProps = swim_searchPageProps['mainContentComponentsListProps']

            swim_lst = []
            for i in range(3,8):
                cur_dict = swim_consumerHeaderProps[i]
                swim_lst.append((f'Gym Name: {cur_dict.get("searchResultBusiness").get("name")}', \
                f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))

        
            bike_response = requests.get(f'https://www.yelp.com/search/snippet?find_desc=spin%20studios&find_loc={athlete.zipcode}&request_origin=user')
            bike_response_data = bike_response.json()
            bike_searchPageProps = bike_response_data['searchPageProps']
            bike_consumerHeaderProps = bike_searchPageProps['mainContentComponentsListProps']

            bike_lst = []
            for i in range(3,8):
                cur_dict = bike_consumerHeaderProps[i]
                bike_lst.append((f'Spin Studio: {cur_dict.get("searchResultBusiness").get("name")}', \
                f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))

            return swim_lst, bike_lst
        
        except:
            return [],[]

    #Find Local Events
    def find_events(self, athlete):

            #Race Site uses state, not zipcode, so we use SearchEngine to find to which state the zipcoode belongs
            search = SearchEngine(simple_zipcode=True)
            zip_search = search.by_zipcode(athlete.zipcode)
            zip_dict = zip_search.to_dict()

            state = zip_dict['state']

            if self.distance == "sprint":
                return f'https://www.trifind.com/gs_sprint/SprintTriathlons.html?state={state}&page=1&year=2022&month=0', state
            elif self.distance == 'olympic':
                return f'https://www.trifind.com/gs_olympic/OlympicTriathlons.html?state={state}&page=1&year=2022&month=0', state
            elif self.distance == 'half+ironman':
                return f'https://www.trifind.com/iron-h.html?state={state}&page=1&year=2022&month=0', state
            elif self.distance == 'ironman':
                return f'https://www.trifind.com/gs_iron/FullIronDistanceTriathlons.html?state={state}&page=1&year=2022&month=0', state
            else: #Should never get here
                return f'/', "NA"
            
class Weight_Lifting(Exercise):

    def __init__(self):

        super().__init__()

    def __repr__(self):
        return f"Weight Lifting, {self.weight}"

    #Sets the type of lifting and equipment budget
    def set_additional(self, weight, budget):
        self.weight = weight
        self.budget = budget

    #return based on type of lifting
    def find_plan(self):
        if self.weight == "bodyweight":
            return ("Here is a Six-Week Plan for Beginners, courtesy of The Hybrid Athlete", "https://thehybridathlete.com/bodyweight-training-plan/"),\
                    ("Here is a long article with video examples of workouts, tips on stretching and form, and other introductory basics, courtesy of onnit.com","https://www.onnit.com/academy/basic-to-beast-complete-bodyweight-workout-program/"),\
                        ("Here is a collection of Bodyweight Exercises, though no explicit routine structure to them, courtesy of Men's Health","https://www.menshealth.com/uk/building-muscle/a756325/10-best-bodyweight-exercises-for-men/")
        elif self.weight == "highrep":
            return "Here is a 4-Days-A-Week low-weight, high-rep plan, courtesy of building-muscle101.com", "https://www.building-muscle101.com/20-rep-weight-training-workout-routine/"
        elif self.weight == "heavy":
            return "Here is a 3-to-4-Days-A-Week high-weight, low-rep plan, courtesy of aworkoutroutine.com", "https://www.aworkoutroutine.com/the-muscle-building-workout-routine/"

    #return based on type on budget
    def find_equipment(self):
        if self.budget == "100":
            return "Here are some at-home essentials.", ("Dip Bar",\
                 "https://www.amazon.com/Dripex-Adjustable-Connectors-Equipment-Calisthenics/dp/B08YYV47VJ/ref=asc_df_B08YYV47VJ/?tag=hyprod-20&linkCode=df0&hvadid=519485156281&hvpos=&hvnetw=g&hvrand=8903438363440240713&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-1366979420617&psc=1"),\
                     ("Pull-Up Bar", "https://www.amazon.com/Pure-Fitness-Multi-Purpose-Doorway-Pull-Up/dp/B00EB3HFHS/ref=asc_df_B00EB3HFHS/?tag=hyprod-20&linkCode=df0&hvadid=198074695887&hvpos=&hvnetw=g&hvrand=8318379034813128993&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-322054613682&psc=1")
        
        elif self.budget == "200":
            return "Here are some at-home essentials", ("Dip Bar",\
                 "https://www.amazon.com/Dripex-Adjustable-Connectors-Equipment-Calisthenics/dp/B08YYV47VJ/ref=asc_df_B08YYV47VJ/?tag=hyprod-20&linkCode=df0&hvadid=519485156281&hvpos=&hvnetw=g&hvrand=8903438363440240713&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-1366979420617&psc=1"),\
                     ("Pull-Up Bar", "https://www.amazon.com/Pure-Fitness-Multi-Purpose-Doorway-Pull-Up/dp/B00EB3HFHS/ref=asc_df_B00EB3HFHS/?tag=hyprod-20&linkCode=df0&hvadid=198074695887&hvpos=&hvnetw=g&hvrand=8318379034813128993&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-322054613682&psc=1"),\
                         ("Resistance Bands", "https://www.walmart.com/ip/Portable-Home-Gym-Pilates-Bar-System-Full-Body-Workout-Equipment-Training-Kit/292607978?wmlspartner=wlpa&selectedSellerId=16214&&adid=22222222227351084064&wl0=&wl1=g&wl2=c&wl3=440999815848&wl4=pla-913994989822&wl5=9067609&wl6=&wl7=&wl8=&wl9=pla&wl10=120798572&wl11=online&wl12=292607978&veh=sem&gclid=EAIaIQobChMI4NqYnYuv9AIVi77ICh3npQTcEAQYEiABEgJdOfD_BwE&gclsrc=aw.ds")
        
        elif self.budget == "500":
            return "Here are some options to mix-and-match",\
                ("Dip Bar","https://www.amazon.com/Dripex-Adjustable-Connectors-Equipment-Calisthenics/dp/B08YYV47VJ/ref=asc_df_B08YYV47VJ/?tag=hyprod-20&linkCode=df0&hvadid=519485156281&hvpos=&hvnetw=g&hvrand=8903438363440240713&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-1366979420617&psc=1"),\
                     ("Pull-Up Bar", "https://www.amazon.com/Pure-Fitness-Multi-Purpose-Doorway-Pull-Up/dp/B00EB3HFHS/ref=asc_df_B00EB3HFHS/?tag=hyprod-20&linkCode=df0&hvadid=198074695887&hvpos=&hvnetw=g&hvrand=8318379034813128993&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-322054613682&psc=1"),\
                         ("Resistance Bands", "https://www.walmart.com/ip/Portable-Home-Gym-Pilates-Bar-System-Full-Body-Workout-Equipment-Training-Kit/292607978?wmlspartner=wlpa&selectedSellerId=16214&&adid=22222222227351084064&wl0=&wl1=g&wl2=c&wl3=440999815848&wl4=pla-913994989822&wl5=9067609&wl6=&wl7=&wl8=&wl9=pla&wl10=120798572&wl11=online&wl12=292607978&veh=sem&gclid=EAIaIQobChMI4NqYnYuv9AIVi77ICh3npQTcEAQYEiABEgJdOfD_BwE&gclsrc=aw.ds"),\
                             ("Adjustable Free-Weights", "https://www.bowflex.com/selecttech/552/100131.html?adID=DOFG2BFEED1&pk_source=google&pk_medium=cpc&gclid=EAIaIQobChMI4NqYnYuv9AIVi77ICh3npQTcEAQYBSABEgKulvD_BwE")
        
        elif self.budget == "1000":
            return "Here are some options to mix-and-match",\
                ("Dip Bar","https://www.amazon.com/Dripex-Adjustable-Connectors-Equipment-Calisthenics/dp/B08YYV47VJ/ref=asc_df_B08YYV47VJ/?tag=hyprod-20&linkCode=df0&hvadid=519485156281&hvpos=&hvnetw=g&hvrand=8903438363440240713&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-1366979420617&psc=1"),\
                     ("Pull-Up Bar", "https://www.amazon.com/Pure-Fitness-Multi-Purpose-Doorway-Pull-Up/dp/B00EB3HFHS/ref=asc_df_B00EB3HFHS/?tag=hyprod-20&linkCode=df0&hvadid=198074695887&hvpos=&hvnetw=g&hvrand=8318379034813128993&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-322054613682&psc=1"),\
                         ("Resistance Bands", "https://www.walmart.com/ip/Portable-Home-Gym-Pilates-Bar-System-Full-Body-Workout-Equipment-Training-Kit/292607978?wmlspartner=wlpa&selectedSellerId=16214&&adid=22222222227351084064&wl0=&wl1=g&wl2=c&wl3=440999815848&wl4=pla-913994989822&wl5=9067609&wl6=&wl7=&wl8=&wl9=pla&wl10=120798572&wl11=online&wl12=292607978&veh=sem&gclid=EAIaIQobChMI4NqYnYuv9AIVi77ICh3npQTcEAQYEiABEgJdOfD_BwE&gclsrc=aw.ds"),\
                             ("Adjustable Free-Weights", "https://www.bowflex.com/selecttech/552/100131.html?adID=DOFG2BFEED1&pk_source=google&pk_medium=cpc&gclid=EAIaIQobChMI4NqYnYuv9AIVi77ICh3npQTcEAQYBSABEgKulvD_BwE"),\
                                 ("Spin Bike", "https://www.amazon.com/YOSUDA-Indoor-Cycling-Bike-Stationary/dp/B07D528W98/ref=sr_1_3?keywords=spin+bikes&qid=1638226210&qsid=140-5700113-7714932&refinements=p_36%3A17431213011&rnid=17431212011&s=exercise-and-fitness&sr=1-3&sres=B07D528W98%2CB07Q6X4H9N%2CB07NJL3X2X%2CB08MFBZ1RS%2CB08K8W5N5N%2CB00JDC0BC8%2CB08LCKX1CC%2CB00GQ9ZR7U%2CB08R1RSZP6%2CB002CVU2HG%2CB08FJ6M7DV%2CB08VRSXLSP%2CB07BSBBZPJ%2CB08NYR7VWT%2CB08832TDBK%2CB07X6GHLLT%2CB07PMD1WG8%2CB00XMHI7LC%2CB07XQL5ZWW%2CB09CSXBWM6&srpt=STATIONARY_BICYCLE"),\
                                    ("Bench", "https://www.amazon.com/Marcy-Multi-Position-Weightlifting-Strength-SB-10115/dp/B01NBRII6Y/ref=asc_df_B01NBRII6Y/?tag=hyprod-20&linkCode=df0&hvadid=216844664045&hvpos=&hvnetw=g&hvrand=14007167323133867743&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-376718925289&psc=1") 
        else: #Should never get here
            return "Error"

    def find_books(self):

        lst = [("'Starting Strength: Basic Barbell Training', by Mark Rippetoe", "https://www.amazon.com/Starting-Strength-Basic-Barbell-Training/dp/0982522738",\
            "Starting Strength has been called the best and most useful of fitness books. The second edition, Starting Strength: Basic Barbell Training, sold over \
                80,000 copies in a competitive global market for fitness education. Along with Practical Programming for Strength Training 2nd Edition, they form a \
                    simple, logical, and practical approach to strength training. Now, after six more years of testing and adjustment with thousands of athletes in \
                        seminars all over the country, the updated third edition expands and improves on the previous teaching methods and biomechanical analysis. \
                            No other book on barbell training ever written provides the detailed instruction on every aspect of the basic barbell exercises found in \
                                SS:BBT3. And while the methods for implementing barbell training detailed in the book are primarily aimed at young athletes, they have \
                                    been successfully applied to everyone: young and old, male and female, fit and flabby, sick and healthy, weak and already strong. \
                                        Many people all over the world have used the simple biological principle of stress/recovery/adaptation on which this method is \
                                            based to improve their performance, their appearance, and their long-term health. With over 150,000 copies in print in three \
                                                editions, Starting Strength is the most important method available to learn the most effective way to train with barbells \
                                                    -- the most important way to improve your strength, your health, and your life."),\
                                                        ("'Science and Development of Muscle Hypertrophy', by Brad J. Schoenfeld", "https://www.amazon.com/Science-Development-Muscle-Hypertrophy-Schoenfeld/dp/149251960X",\
                                                            "Muscle hypertrophy—defined as an increase in muscular size—is one of the primary outcomes of resistance training. Science and Development of Muscle Hypertrophy \
                                                                is a comprehensive compilation of science-based principles to help professionals develop muscle hypertrophy in athletes and clients. With more than 825 \
                                                                    references and applied guidelines throughout, no other resource offers a comparable quantity of content solely focused on muscle hypertrophy. \
                                                                        Readers will find up-to-date content so they fully understand the science of muscle hypertrophy and its application to designing training programs. \
                                                                            Written by Brad Schoenfeld, PhD, a leading authority on muscle hypertrophy, this text provides strength and conditioning professionals, \
                                                                                personal trainers, sport scientists, researchers, and exercise science instructors with a definitive resource for information regarding \
                                                                                    muscle hypertrophy—the mechanism of its development, how the body structurally and hormonally changes when exposed to stress, ways to \
                                                                                        most effectively design training programs, and current nutrition guidelines for eliciting hypertrophic changes.")]

        return lst

    #find local gyms
    def find_facilities(self, athlete):
        
        #Sometimes webscraping fails. Error Handling just in case
        try:
            response = requests.get(f'https://www.yelp.com/search/snippet?find_desc=gym&find_loc={athlete.zipcode}&request_origin=user')
            response_data = response.json()
            searchPageProps = response_data['searchPageProps']
            mainContentComponentsListProps = searchPageProps['mainContentComponentsListProps']

            lst = []
            for i in range(3,8):
                cur_dict = mainContentComponentsListProps[i]
                lst.append((f'Gym Name: {cur_dict.get("searchResultBusiness").get("name")}', \
                f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))

            return lst

        except:
            return []

class Yoga(Exercise):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Yoga, {self.practice}"

    #Sets type of practice and budget for retreats
    def set_additional(self, practice, budget):
        self.practice = practice
        self.budget = budget
    
    #return a few different routines based on the style of Yoga
    def find_plan(self):
        
        if self.practice == "restorative":
            return ("Caren Baginski", "https://www.youtube.com/watch?v=Wj5bbK2tbO4"),\
                    ("Jessica Richburg", "https://www.youtube.com/watch?v=c56tAJ9KjRg"),\
                        ("Yoga With Bird", "https://www.youtube.com/watch?v=VU6u-Fjtbd4"),\
                            ("VeryWellFit.com", "https://www.verywellfit.com/classic-restorative-yoga-poses-at-home-3882195"),\
                                ("PureWow.com","https://www.purewow.com/wellness/restorative-yoga-poses")
        elif self.practice == "hatha":
            return ("BrettLarkinYoga", "https://www.youtube.com/watch?v=GWg-siH2VEA"),\
                    ("Fightmaster Yoga","https://www.youtube.com/watch?v=XSQn4-lO0Vk"),\
                        ("Yoga With Christina - ChriskaYoga", "https://www.youtube.com/watch?v=pjRt080U3Go"),\
                            ("Tummee.com", "https://www.tummee.com/yoga-sequences/hatha-yoga-sequences"),\
                                ("ArhantaYoga.com", "https://www.arhantayoga.org/yoga-exercises-yoga-asana-guide/")

        elif self.practice == "vinyasa":
            return ("Yoga With Adriene","https://www.youtube.com/watch?v=9kOCY0KNByw"),\
                    ("SarahBethYoga","https://www.youtube.com/watch?v=W5dkeP3GxtU"),\
                        ("BrettLarkinYoga", "https://www.youtube.com/watch?v=bzSpwM9LiRs"),\
                            ("Tummee.com", "https://www.tummee.com/yoga-sequences/vinyasa-yoga-sequences"),\
                                ("Shape.com", "https://www.shape.com/fitness/workouts/14-yoga-poses-revamp-your-vinyasa-routine")
        else:
            return "Error"

    #Returns mats and clothing
    def find_equipment(self, athlete):
        
        mat_url = "https://www.amazon.com/s?k=yoga+mat&ref=nb_sb_noss_1"
        clothes_url = f"https://www.amazon.com/s?k={athlete.gen_clothes}+yoga+clothes+size+{athlete.clothes}&ref=nb_sb_noss"

        return mat_url, clothes_url
        
    #Some books on the physicality, others on meditation, origins of Yoga
    def find_books(self):
        lst = [("'Roots of Yoga (Penguin Classics)', collected and translated by James Sir Mallinson", "https://www.amazon.com/Roots-Penguin-Classics-James-Mallinson/dp/0241253047/ref=asc_df_0241253047/?tag=hyprod-20&linkCode=df0&hvadid=312014159271&hvpos=&hvnetw=g&hvrand=15709186972477835213&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-454673771728&psc=1",\
            "Despite the immense popularity of yoga today, there is surprisingly little knowledge of its roots among practitioners. This book brings together, for the first time, the core teachings of yoga in the words of their authors, rather than in the secondary versions of modern interpreters. Including key passages from the Upanishads, the Buddhist and Jaina traditions, the yoga sections of \
                the Indian Tantras, and many texts that are being critically translated for the first time, Roots of Yoga provides a comprehensive and immediate insight into the essential texts of the Indian traditions of yoga. This book is a first stop for anyone wishing to learn more than they are told at their yoga class, and an indispensable resource for serious yoga practitioners and teachers."),
                ("'Science of Yoga: Understand the Anatomy and Physiology to Perfect Your Practice', by Ann Swanson", "https://www.amazon.com/Science-Yoga-Understand-Physiology-Practice/dp/146547935X/ref=asc_df_146547935X/?tag=hyprod-20&linkCode=df0&hvadid=266429648371&hvpos=&hvnetw=g&hvrand=12192649304756311197&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-525268295205&psc=1",\
                    "Scientific principles and evidence have demystified so much of the practice. It is impossible to deny the benefits of yoga to every system in the body. Delve into the science behind your favorite yoga poses with this easy-to-understand, comprehensive guide.\
                        Perfect for yogis of all levels, this reference book is an in-depth look at your physiology to help you understand how yoga works, and how to practice it safely for the best results. Find out how the spine, breathing and body position are all fundamentally linked. See how specific muscles respond to the movements of the joints, and how alterations of a pose can enhance or reduce effectiveness. "),
                        ("'The Path of Yoga: An Essential Guide to Its Principles and Practices', by Georg Feuerstein",\
                            "https://www.amazon.com/Path-Yoga-Essential-Principles-Practices/dp/1590308832/ref=asc_df_1590308832/?tag=hyprod-20&linkCode=df0&hvadid=312049124368&hvpos=&hvnetw=g&hvrand=12192649304756311197&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-762189798912&psc=1&tag=&ref=&adgrpid=61851652213&hvpone=&hvptwo=&hvadid=312049124368&hvpos=&hvnetw=g&hvrand=12192649304756311197&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-762189798912",
                            "This overview of the essentials of Yoga is meant to both broaden and deepen the understanding of beginning students. It covers all the basic elements of this ancient discipline and philosophy of India—including Yoga poses, diet, breath control, meditation, mantras, Kundalini energy, and more. It also includes newly translated excerpts from the scriptures and pays special attention to branches of Yoga, such as Tantra, that are of great interest to Western students but are frequently misunderstood.")]

        return lst
    
    #Yoga studios
    def find_facilities(self, athlete):
        
        #Error handling in case webscraping fails
        try:
            response = requests.get(f'https://www.yelp.com/search/snippet?find_desc=yoga%20studios&find_loc={athlete.zipcode}&request_origin=user')
            response_data = response.json()
            searchPageProps = response_data['searchPageProps']
            consumerHeaderProps = searchPageProps['mainContentComponentsListProps']

            lst = []
            for i in range(3,8):
                cur_dict = consumerHeaderProps[i]
                lst.append((f'Yoga Studio: {cur_dict.get("searchResultBusiness").get("name")}', \
                f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))
            
            return lst

        except:
            return []
        
    #MReturn Yoga Retreats within budget
    def find_events(self):

        return f'https://bookretreats.com/s/yoga-retreats/affordable-yoga-retreats/united-states?ranges[dates.priceFrom][min]=89&ranges[dates.priceFrom][max]={self.budget}&pageNumber=1'
    

class Athlete():


    def __init__(self, name, zipcode, shoes, clothes, gen_clothes, exercise):
        self.name = name
        self.shoes = shoes
        self.clothes = clothes
        self.gen_clothes = gen_clothes
        self.zipcode = zipcode

        if exercise == 'running':
            self.exercise = Running()
        elif exercise == "swimming":
            self.exercise = Swimming()
        elif exercise == 'cycling':
            self.exercise = Cycling()
        elif exercise == 'triathlon':
            self.exercise = Triathlon()
        elif exercise == 'weightlifting':
            self.exercise = Weight_Lifting()
        elif exercise == 'yoga':
            self.exercise = Yoga()
        else: #should never get here 
            self.exercise = exercise

            

        

    def __repr__(self):
        
        s = f'Name: {self.name}, Shoe Size: {self.shoes}, Clothing Size: {self.clothes}, Zipcode: {self.zipcode}, Exercise: {self.exercise}'
        return s
