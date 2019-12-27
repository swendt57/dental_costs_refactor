## Dental Cost Comparison between San Diego, California and Tijuana, Mexico

This is a refactor of my Milestone 2 project (see description below). I have converted the webiste into a Python / Flask app and have added a MongoDB database
along with functionality to manage the dentists in real time. I have also added a User Comments section that displays comments submitted 
by actual users as well as functionality that allows users to register and log in and out as needed.

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
* Add a Tips and Tricks section for crossing back and forth across the international border 
* Improve the scatter chart on the Cost Comparisons page

### Technologies Used - WORKING!!

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
  * My preferred IDE
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