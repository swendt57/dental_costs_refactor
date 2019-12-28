## Dental Cost Comparison between San Diego, California and Tijuana, Mexico

This is a refactor of my Milestone 2 project (see description below). I have converted the webiste into a Python / Flask app and have added a MongoDB database
along with functionality to manage the dentists in real time. I have also added a User Comments section that displays comments submitted 
by actual users as well as functionality that allows users to register and log in and out as needed.

The original website can be viewed at https://swendt57.github.io/dental_costs_project/  
The new Flask/Python version can be viewed at https://dental-costs.herokuapp.com/

The original code base is available at https://github.com/swendt57/dental_costs_project
The new Flask/Python version is at https://github.com/swendt57/dental_costs_refactor

#### Previous Description

San Diego and Tijuana are on either side of the USA/Mexico international border. Due to this proximity, I know of many people, especially 
those without insurance, who go to Tijuana for their dental work. (Years ago, I was one of those people.) I thought it would be 
interesting to compare the costs of basic services.

After researching on the Internet, I decided to start with Yelp's Top Ten Most Affordable Dentists in San Diego and in Tijuana.

I am using real data whenever possible, however, many dentists, especially those on the US affordable list, are reticent 
to share any figures on the phone. Due to this, I have had to insert fake data but I will mark it as such.

Since this is a school project, and the main purpose is to show that I can create engaging interactive websites, and after 
checking with my mentor, I am proceeding as described above.

### UX
User Stories for this edition:
* **User wants to read of others experiences**
* **Users want the ability to upload comments about their experiences**
* **Admins want the ability to add and edit dentists as needed without having to manually create a JSON text file** 

Previously enacted stories:
* User wants to find less expensive dentists
* User wants to compare pricing between San Diego and Tijuana
* User wants to see where the various dentists are located
* User wants driving directions to a dentist

Future User Stories
* Users want information on logistics of crossing the international border (future)

I created some mock-ups in Balsamiq Mockup 3 and these can be downloaded from my GitHub site at 
https://github.com/swendt57/dental_costs_refactor/tree/master/support/mockups

### Features

**The site includes the following new features:**

* A User Comment section where users can upload their experiences
* An extensive Admin section that:
  * Allows dentists can be added, edited, activated, and deactivated through the web interface
  * Allows the main dentist JSON file to be exported at will from the web interface
  * Users can use to register for the site, login and log out, and to upload comments
* An improved **Location Maps** page that shows the dental office name in a tool tip when a user pauses on the icon

**Features from the original site:**

* An **Introduction** page that explains the purpose and thinking behind the website
* A **Top 10 Affordable Dentists** page that shows Yelp's Top 10 Affordable Dentists for both San Diego and Tijuana
  * Each dental office is hyperlinked to Google Maps and can provide driving directions 
* A **Cost Comparisons** page that has three chart sections
  * A bar chart that shows the average cost of five common procedures and overlays Tijuana data over San Diego
  * A distribution chart that shows the cost-per-procedure for each office and each procedure
  * Two pie charts that displays the amount of real data vs fake data for each city which I think is illuminating
* A **Location Maps** page that has a Google map each for San Diego and Tijuana; each showing the dental offices in relation to each other.

**Possible future work:**

* Add functionality to allow users to filter comments on dentist, city, and user
* Add joins to the MongoDB queries to avoid having to do repeated queries for on complete record
* Add an "auto-delete" function for removing older copies of the dentist JSON files
* Allow order of the dentists to be changed through the interface with up and down arrows
* Add pagination the the User Comments page
* Add modals for logging in and registering
* Improve error handling
* Improve validation
* Add a Tips and Tricks section for crossing back and forth across the international border 
* Improve the scatter chart on the Cost Comparisons page

### Technologies Used - WORKING!!
**New to this refactor**

* Python
  * https://www.python.org/
  * The main language I used for the data processing portion of the website
* Flask
  * http://flask.palletsprojects.com/en/1.1.x/
  * The Python framework that the app is built on
* Marshmallow and Flask-Marshmallow
  * https://marshmallow.readthedocs.io/en/stable/
  * https://flask-marshmallow.readthedocs.io/en/latest/
  * Used for validating data input and providing helpful messages to the user
* PyMongo
  * https://api.mongodb.com/python/current/
  * Used for interfacing with MongoDB database
* MongoDB
  * https://www.mongodb.com/
  * Document-based, distributed database used the app 
* Heroku
  * https://www.heroku.com/home
  * Cloud host of the website
* PyCharm
  * https://www.jetbrains.com/pycharm/
  * Python integrated development environment
  * My preferred Python IDE

**Original list**
* JavaScript
  * https://www.javascript.com/
  * The main scripting language that I used for navigation, charting, accessing Google API, etc
* jQuery
  * https://jquery.com/
  * JavaScript library that simplifies DOM manipulation
* Jasmine
  * https://jasmine.github.io/
  * JavaScript testing framework used for unit tests on data parsing methods
* D3, DC, Cross Filter 
  * https://d3js.org/
  * https://dc-js.github.io/dc.js/
  * https://square.github.io/crossfilter/
  * D3 is a charting framework, DC and Crossfilter used for mutli-dimensional data views
  * I mostly used D3 but one chart was built with DC and Crossfilter
* Bootstrap 4
  * https://getbootstrap.com/docs/4.0/getting-started/introduction/
  * Responsive, mobile-first, framework````
* Google Fonts
  * https://fonts.google.com/
  * Free, open-source, on-demand, fonts
* Google Maps API
  * https://cloud.google.com/maps-platform/maps/
  * Mapping API that I used for driving directions and showing office locations
* Font Awesome
  * https://fontawesome.com
  * Icons and such
* IntelliJ IDEA
  * https://www.jetbrains.com/idea/
  * Java integrated development environment
  * My preferred overall IDE
* GitHub
  * https://github.com/swendt57
  * Code repository
* CVS to JSON Converter
  * https://www.convertcsv.com/csv-to-json.htm
  * Used for converting Excel based data to JSON
* Stack Overflow
  * https://stackoverflow.com/
  * Community of developers that has potential solutions to almost any problem
* Microsoft Excel
  * https://products.office.com/en-us/excel-c
  * I used this for initial collecting and manipulating of the data and then converting it to CSV
  
### Testing

**Automated testing**
I used Python assertions to test Python methods functions that manipulated data including:
* data_format.py -- restructure_dental_json, and expand_data  
Python tests can be run with the command > python python_tests.py on https://github.com/swendt57/dental_costs_refactor/blob/master/tests/python_tests.py

I used Jasmine to test all JavaScript functions that manipulated data including:
* maps.js -- assembleCoordinates
* cost-comparison.js -- assembleOverlayDataSet, sortDataByCity, and determineMockDataTotals   
Jasmine automated tests can be run by running this file: https://github.com/swendt57/dental_costs_refactor/tree/master/tests/jasmine/index.html

**Manual Testing**

Admin Functions
1. Verify that the Admin nav button only appears when an admin is logged in (the username swendt57 has admin privileges)
2. View each page and verify that each is responsive to changing screen sizes
    * Dentist Lists
    * User Lists
    * Add Dentist
    * Add User
    * Add Comment
3. Fill out each form, leaving some required values empty to verify that the validation is working.   
**Note:** To reach Edit pages, click the appropriate hyperlink on the list pages.

User Comments
1. Go to the User Comments page.
2. Verify that the Add Comment button only appears when a user is logged in.
3. Add a comment and verify that it appears at the top of the list.

Top 10
1. Go to Top 10 Affordable page.
2. Verify both boxes show and have 10 dentists each.
3. Verify that the addresses appear for larger screens and only the name appears for smaller screens. The page must be 
reloaded for the addresses to appear and disappear for different screen sizes.
4. Verify each link takes the user to a Google Maps directions page with that office selected.
5. Verify that the boxes are side by side on larger screens.

Cost Comparisons
1. Go to Cost Comparisons page.
2. Verify that three chart sections display (four charts in total).
3. Verify that the charts shrink somewhat for smaller screens. The page must be reloaded for the charts to change size.
4. Verify that on small screens in portrait mode a message recommending landscape mode appears. The page must be reloaded 
for this message to appear and disappear.
5. On the top chart:
    * verify that all five procedures are displayed.
    * verify that rolling over the legend highlight the bars for that city.
    * verify that rolling over either the bar or the overlay bar highlight the other bars for that city.
    * verify that the chart 
6. On the center chart:
    * verify that all five procedures are displayed.
    * verify that all five procedures are displayed.
    * verify that the tooltips show the procedure and cost.
7. On the pie charts:
    * verify that there is one chart for each city.
    * verify that the labels are not cut off.
    * verify that when you roll over a wedge that it increases in size.

Location Maps
1. Go to Location Maps page.
2. Verify that there are two maps, one each for San Diego and Tiuana.
3. Verify that each map shows 10 locations with a legend below.
4. Verify that the maps are side by side on larger screens.

Footer
1. Verify that only two icons appear at a time.  
    * Register and Log in if no user is logged in.  
    * Log out and Comment if a user is logged in.
2. Verify that the icons shrink for smalled screen sizes

**Manual testing** was performed on: 
* Chrome version 79.0.3945.88 browser including:
  * Galaxy S5 simulator
  * iPhone 6/7/8 simulator
  * iPad simulator
  * iPad Pro simulator
* Firefox 71.0 browser including:
  * Galaxy S9/S9+ simulator
  * iPhone X/XS simulator
  * Kindle Fire HDX simulator
* Galaxy S10e phone with:
  * Chrome mobile version 79.0.3945.93
  * Firefox for Android version 68.3.0
  
Known Issues  
* There is a small amount of back and forth play on the comparisons page. I have tried all suggested remedies but none solve 
the issue completely.

### Deployment

The website is currently deployed on Heroku at https://dental-costs.herokuapp.com/  
These instructions are for the inital deployment of the app.
1. From the terminal, log into Heroku > heroku login
2. Verify that both Profile and requirements.txt files are both up-to-date. The requirements file can be updated by running this 
on the terminal > pip3 freeze --local > requirements.txt
3. From the terminal, run > heroku apps: create 'dental-costs'
4. On the Heroku Dashboard for the app, set the configuration Variables:
    1. Click Settings to open the settings page.
    2. Click the Reveal Config Vars button to show the configs.
    3. Add the following keys. The values are kept separate from the app except the last two:
        * db_user
        * db_pw
        * google_api_key
        * secret_key
        * IP -- 0.0.0.0
        * PORT -- 5000
5. Verify that the local Git repo is up-to-date and from the terminal type > git push heroku master
6. If needed, start a web process by typing > heroku ps: scale web=1
7. If needed, restart the dynos. 
    1. On the Heroku Dashboard, click the More button in the upper-right corner.
    2. From the drop-down, select Restart all dynos
8. If you have lead a good, clean life, the app is deployed... If not, troubleshoot! :-)  

NOTE: If not already done, the website base URL must be added to the Website Restrictions section of the Google Cloud Platform 
APIs and Services area. This helps to reduce non-authorized use of the API key.


#### Acknowledgements

(https://placehold.it/150/f03c15/000000?text=YANKEE) 'TTT'

* Thanks to the following people for their **clear and concise** answers on stackoverflow.com:
  * su27 - https://stackoverflow.com/questions/18967441
  * Berk Özbalcı - https://stackoverflow.com/questions/50867685
  * Agush - https://stackoverflow.com/questions/14304494
  * Boston Kenne - https://stackoverflow.com/questions/52491353
  * dkamins - https://stackoverflow.com/questions/9170288
* https://flask.palletsprojects.com/ for favicon information
* https://css-tricks.com
* https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/
* https://datatofish.com/rename-file-python/
* Thanks to the following people on stackexchange.com:
  * Micahel Thomas - https://craftcms.stackexchange.com/questions/8593

#### Original Acknowledgements

* This project was inspired by my friend, Gail Dana, of San Diego, California
* Opaque div background concept from www.scotch.io
* Used the CSV to JSON converter from www.convertcsv.com/csv-to-json.htm
* Thanks to www.stackoverflow.com for keeping me sane. In particular:
  * Johannes - https://stackoverflow.com/users/5641669/johannes
  * Mark - https://stackoverflow.com/users/16363/mark - who's examples I leveraged to create the overlay bar chart
* Hannah Recht from https://bl.ocks.org/hrecht for chart legend examples
* Kiran from https://bl.ocks.org/kiranml1 for a sample D3 pie chart
* https://webdesign.tutsplus.com/tutorials/svg-viewport-and-viewbox-for-beginners--cms-30844 for ViewPort and ViewBox explanations
* Used https://www.latlong.net to look up latitude and longitudes for mapping functions