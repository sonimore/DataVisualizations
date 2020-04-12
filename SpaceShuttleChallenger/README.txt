Data Visualization Assignment 3

The data set used to create this visualization was the provided data set, challenger.csv. This data set contains
the following attributes: flight_index (order that flights were launched),
num_o_ring_distress (the number of O-rings that experienced distress during launch),
launch_temp (temperature at launch in degrees Farenheit),
leak_check_pressure (pressue of the gas meant to be contained by O-rings),
and tufte_metric (Tufte's measure of damage to O-rings during launch).

This website can be viewed by running python3 -m http.server in this directory, navigating to the URL stated on the terminal, and clicking on the links to each of the visualizations.

The splom.html file displays a relationship between all of the attributes with each other (except for the tufte_metric).
I left one of the attributes out, namely, the flight_index, to keep the visualization under the 16 scatterplot constraint.
However, this can easily be reverted by making a few small changes to the html file (e.g. by getting rid of the filter when defining the attributes).
This visualization allows the user to interact with the data by allowing them to hover over an individual data point
on the plot, which displays a tooltip with information about each of the attributes for the specific data point selected.
Furthermore, hovering over one data point highlights the corresponding data points in the other graphs. Increasing their
size and giving them a contrasting color were mechanisms I decided to use to make these points pop out.
Clicking on a circle toggles them to a pink color so that users can easily view information about multiple data points simultaneously.

The parallelCoordinates.html file displays relationships between the 5 variables by plotting a mapping between them.
The visualization allows the user to interact with the visualization by hovering over a line, which in turn highlights
the entire path and increases the line width for easy visibility. This also contains a tooltip that displays information
the attributes for that specific path. It also allows users to click on a particular path, triggering it to select the path
and change the color to pink. This allows users to focus their attention on specific tasks. A to-do item is to make
the teal paths part of the background by making it gray when a user has selected a path or is hovering over a path.

Disclaimer and Sources:
I used various sources to be able to complete this assignment. In order to ensure that I learned as much as possible,
I copied and pasted other examples, and played around with the examples by deleting pieces of the code
and subsequently fixing the code, and also by adding my own features to it. I also looked up the documentation for each line of code
that I didn't understand to make sure that I understood it completely.
My ideas are nonetheless inspired by various sources, including:
https://plot.ly/javascript/custom-buttons/
https://syntagmatic.github.io/parallel-coordinates/examples/basic.html
https://www.dashingd3js.com/d3js-scales
https://beta.observablehq.com/@jerdak/parallel-coordinates-d3-v4
http://bl.ocks.org/d3noob/a22c42db65eb00d4e369
https://www.kylebradbury.org/visualizations/scattermatrix/
http://www.d3noob.org/2013/01/selecting-filtering-subset-of-objects.html