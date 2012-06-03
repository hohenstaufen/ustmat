Urban street tree mobile application for Toronto
================================================

Have you ever wondered what type of tree you were passing along Toronto 
streets, or how much of a difference these neighbourhood trees make for 
energy conservation and air quality?   This data is all available and 
can be made user friendly and accessible to visitors and residents of 
Toronto.  Today Toronto Open Data has released records of size, 
location and species (type of tree) for over 530,000 street trees to 
enable this Random Hacks of Kindness project to create a website or 
mobile application.  Tree species descriptions and economic valuation 
of tree benefits are readily available from linking to existing sites.  
A precedent project is there to inspire the project and to build upon, 
this is the mobile application for street trees in New York City, 
Trees Near You.


Example:
--------

When you enter the address or click my position, a screen could pop up 
with the following fields: 1. An image of the leaf; 2. The common name 
for the tree; 3. The botanical name for the tree; 4. A brief 
description of the tree; 5. The address in the database associated with 
the tree; 6. The description using a locator system or text where the 
tree is on the right of way; 7. the estimated annual value of the 
ecological benefits for the tree in a dollar value, and perhaps 
represented as a pie chart by related benefits such as carbon 
sequestration, energy conservation, pollutant up take, etc.


User Stories:
-------------

A user might use this simply to learn more about the trees in their 
neighbourhood but could also use it to protect the trees, ie. A call to 
3-1-1 Toronto (city services number) might be: "hello, my neighbour at 
XX Jones Avenue has a large white oak that is being disturbed by 
repaving and widening the driveway.  Can the city please inspect and 
protect the tree".


Constraints:
------------

The data is now available via Toronto Open 
[www.toronto.ca/open](www.toronto.ca/open). The limitiations of the 
data are available in the information notes. 


Extra Credit:
-------------

Perhaps a tree in front of a home needs work, (the tree located within 
the City right of way), and the resident wants to request an 
inspection. Now the resident can call 3-1-1 Toronto and provide much 
more information that will help City staff locate the right tree, and 
even help prioritize service based on the type of tree, (some tree 
species  are more prone to holding deadwood then others) ie, "hello, I 
have a very large silver maple tree in front of my home and one branch 
is hanging over the street that appears dead."


Similar Projects and Resources:
-------------------------------

New York City has a similar tree application for mobile users called 
Trees Near You. As well as the name of the tree the app uses the size 
of the tree with the species to provide a calculation of the value of 
the ecological benefits of the tree annually.  This part of the New 
York application is based on data from the site 
[www.treebenefits.com/calculator/](www.treebenefits.com/calculator/).

This tree benefits site could be used for a Toronto application as 
well, the values associated with the northeast U.S. are generally 
applicable in southern Ontario based on the level of detail of the 
application.


Parks, Forestry and Recreation worked with the U.S. Forest Service to 
estimate ecological benefits for the entire urban forest of Toronto 
recently, [www.toronto.ca/trees/pdfs/Every_Tree_Counts.pdf](www.toronto.ca/trees/pdfs/Every_Tree_Counts.pdf)
.  Providing this information on a tree by tree basis can be very 
helpful for residents.


Technologies involved
---------------------

* [Geoserver](http://geoserver.org/) with 
[OpenStreetMap](http://www.openstreetmap.org/) layers of Toronto region
* [Django](https://www.djangoproject.com/) providing API for comments, 
geocoding and tree informations
* [PostgreSQL](http://www.postgresql.org/) with 
[PostGIS](http://postgis.refractions.net/) for 
[Street Tree Data](http://www1.toronto.ca/wps/portal/open_data/open_data_item_details?vgnextoid=5af95104c26f3310VgnVCM1000003dd60f89RCRD&vgnextchannel=6e886aa8cc819210VgnVCM10000067d60f89RCRD)

