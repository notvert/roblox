**Project Overview:** Randomly generated Roblox outfits based on style selection 

**What are the major features of your web application?** Display different outfit styles leveraging Roblox APIs through style.new (Django project)

**What problem is it attempting to solve?** Players want to dress up in Y2K style, but there is no discovery mechanism besides search on Roblox marketplace. This also depends on the creator naming their items with the style. 

**What libraries or frameworks will you use?** I need to narrow down the list of APIs used, this is a starting point: https://devforum.roblox.com/t/collected-list-of-apis/557091

**Functionality:**

**What will they see on each page?** There's only one page for now, index page, and users select one of five styles. Once a style is selected, a list of digital items will be displayed. 

**What can they input and click and see?** Same as above

**How will their actions correspond to events on the back-end? **Pull data from API

**Data Model:**
If each pull of "Y2K" style happens and is stored, I can create a historical model of items.

**Things done:**
-Create Django project
-Identify major Roblox fashion styles (Y2K, Streetwear, Cottage-core, Fantasy)

**Next steps:**
-Create model
-Pull top 100 items per style and put into database
-Create API to pull database

**Notes:**
-Roblox does not require an API key but what happens if I make too many requests, how does it even know a specific person is using it and abusing it
-Create getstyle1.py to get list of items based champions and their respective data but realized that data dragon already does this
-Converted list of champions from a string into a json file
-Created a champions model
-Created a management command to load champions.json into the database
-Created a vue app to list all champions and their respective images
-Created views for four key stats and display the top 10 champions per stat
-Created an API to replace previous hard-coded data view; couldn't get top 10 list to work now
-For live game data pull, need to get encrypted ID via https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"input summoner name"
-Get live game data via https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"input ID"
-Create a new view to execute steps 9/10 and to have exception handling, save file to sample.json
-Create a management command to load match data (sample.json) into the database
-Load match data directly from views.py
-Added new endpoint to API for match data
-Display other player names with Scout button
Calculated if the user should invade or not based on if his/her team's total hp is greater than the enemy team's total hp
