""" 
This is the code used to represent the graphs, charts and tables for our survey regarding
the use of the trending AI tool known as ChatGPT. Here, I have imported Matpltlib to create
the visuals and numpy to help with data analysis and computing  
"""
import matplotlib.pyplot as plt
import numpy as np

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 1 - Age of Participants """

# Bar chart 
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of age ranges, number of responses 
# With colors representing each age range 
age_ranges = ["17-20", "21-30", "31-40","41-50"] 
num_responses = [83,19,1,1]
bar_colors = ["tab:red", "tab:pink" , "tab:blue", "tab:green"]

# Creating and plotting the bar chart with the lists we have initialized
ax.bar(age_ranges,num_responses, color= bar_colors)

# Setting the title as "Bar chart showing age ranges for Chatgpt survey"
ax.set_title('Bar chart showing age ranges for Chatgpt survey')

# Setting the y axis label as the "number of participants"
# Setting the x axis label as the "age range"
ax.set_ylabel('Number of Participants')
ax.set_xlabel("Age Range")

# Display bar chart  
plt.show()

# Pie chart
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing the list of percentages by age range, and list of age ranges
# As well as size of pie chart slices
percentages = ["79.8%", "18.3%", "1%","1%"]
age_ranges = ["17-20", "21-30", "31-40","41-50"]
sizes = [79.8,18.3,1,1]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each age range 
ax.pie(sizes, labels= percentages,colors = ["lightblue", "teal", "turquoise", "navy"],
       labeldistance =1.1) # Initialize distance between pie chart and the % labels

# Creating the legend for the age ranges and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(age_ranges, title = "Age Ranges", loc= "center left", bbox_to_anchor=(1.1, 0.5))

# Setting the title as "Pie chart showing age ranges for Chatgpt survey"
ax.set_title("Pie chart showing age ranges for Chatgpt survey")

# Display pie chart 
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 2 - Gender of Participants """

# Pie chart
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing the list of genders
# As well as size of pie chart slices
genders = "Male", "Female"
sizes = [44.2,55.8]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each gender
# 'autopct' formats how the % are displayed - here it is to 1 d.p.
ax.pie(sizes, labels=genders,colors = ["lightblue", "teal"], autopct = "%1.1f%%")

# Setting the title as "Gender demographic for Chatgpt survey - Pie Chart"
ax.set_title("Gender demographic for Chatgpt survey - Pie Chart")

# Display pie chart 
plt.show()

# Bar chart
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing the list of genders, responses
# With colors representing each gender
genders = ["Male", "Female"]
num_responses = [46,58]
bar_colors = ["tab:blue", "tab:cyan"]

# Creating and plotting the bar chart with the lists we have initialized
ax.bar(genders,num_responses, color= bar_colors)

# Setting the y axis label as the "number of participants"
# Setting the x axis label as the "gender"
ax.set_ylabel('Number of Participants')
ax.set_xlabel("Genders")

# Setting the title as "Gender demographic for Chatgpt survey - Bar Chart"
ax.set_title("Gender demographic for Chatgpt survey - Bar Chart")

# Display bar chart 
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 3 - academic roles """

# Pie chart 
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing the list of academic roles
# As well as size of pie chart slices
roles = "Undergraduate" , "Masters" , "PhD", "Professor"
sizes = [93.3,3.8,1.9,1]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each academic role
ax.pie(sizes, labels=roles,colors = ["pink", "purple", "magenta", "plum"])

# Setting the title as "Pie Chart showing Academic Roles for ChatGPT survey"
ax.set_title("Pie Chart showing Academic Roles for ChatGPT survey")

# Display pie chart 
plt.show()

# Bar chart
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of academic roles, number of responses 
# With colors representing each academic role
roles = ["Undergradute","Masters","PhD","Professor"]
num_responses = [97,4,2,1]
bar_colors = ["tab:blue", "tab:pink", "tab:cyan", "tab:purple"]

# Fixing the scale of y axis
plt.ylim(0,105)

# Creating and plotting the bar chart with the lists we have initialized
rects = ax.bar(roles,num_responses, color= bar_colors)

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)

# Setting the y axis label as the "number of participants"
# Setting the x axis label as the "academic role"
ax.set_ylabel('Number of participants')
ax.set_xlabel("Academic Roles")

# Setting the title as "Bar Chart showing academic roles"
ax.set_title('Bar Chart showing Academic Roles for ChatGPT survey')

# Display bar chart 
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 4 - region of study """

# Pie chart
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing the list of percentages by region of study, and list of regions
# As well as size of pie chart slices
labels = "4.8%", "84.6%" , "3.8%" , "5.8%" , "1%"
regions = "Asia", "North America" , "Africa" , "Europe" ,"Oceania"
sizes = [4.8,84.6,3.8,5.8,1]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each region
ax.pie(sizes, labels=labels,colors = ["lightgreen", "lightblue", "lavender", "pink", "orange"],
       labeldistance =1.2) # Initialize distance between pie chart and the % labels

# Creating the legend for the regions and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(regions, title = "Regions", loc= "center left", bbox_to_anchor=(1.2,0.5))

# Setting the title as "Pie Chart showing regions of study"
ax.set_title("Pie Chart showing Regions of Study")

# Display bar chart 
plt.show()

# Horizontal bar chart 
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of regions, number of responses 
regions = ("Asia", "North America" , "Africa" , "Europe" ,"Oceania")
num_responses = (5,88,4,6,1)

# Creating list of positions that are equally spaced for each region
y_pos = np.arange(len(regions))

# Creating and plotting the bar chart with the lists we have initialized
# Choosing one color for all of them
rects = ax.barh(y_pos, num_responses, color = "violet")

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)

# Setting the y axis ticks at position y_pos and the labels are the regions
ax.set_yticks(y_pos, labels=regions)
ax.invert_yaxis()  # labels read from top-to-bottom

# Setting the y axis label as the "number of participants"
# Setting the x axis label as the "region of study"
ax.set_xlabel('Number of Participants')
ax.set_ylabel('Region of Study')

# Setting the title as "Horizontal bar chart showing regions of study"
ax.set_title('Horizontal bar chart showing regions of study')

# Display horizontal bar chart 
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 5 - faculty of study """

# Pie chart
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing the list of percentages by facutly of study, and list of faculties
# As well as size of pie chart slices
labels = "33.7%" , "1%" , "6.7%", "2.9%" , "22.1%" , "4.8%" , "3.8%" , "21.2%" , "3.8%"
faculties = ["Science" ,"Law" , "Arts" , "Community Services" , "Eng. & Arch. Science", 
             "Design" , "Health Sciences", "Business", "Other"]
sizes = [33.7,1,6.7,2.9,22.1,4.8,3.8,21.2,3.8]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each region
ax.pie(sizes, labels=labels,colors = ["#FFA07A", "#FFDAB9", "#7FFFD4" ,"#FFC0CB", "#F0E68C",
    "#FFA500","#BA55D3", "#E6E6FA", "#B0E0E6", "#00FFFF"],
    labeldistance =1.2) # Initialize distance between pie chart and the % labels

# Creating the legend for the faculties and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(faculties, title = "Faculties", loc= "center left", bbox_to_anchor=(1.2,0.5))

# Setting the title as "Faculty of Study among participants"
ax.set_title("Faculty of Study among participants")

# Display Pie Chart
plt.show()

# Horizontal bar chart 
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of regions, number of responses 
faculties = ["Science" ,"Law" ,"Arts" , "Community Services" ,"Eng. & Arch. Science", 
             "Design" , "Health Sciences","Business", "Other"]
num_responses = [35,1,7,3,23,5,4,22,4]

# Creating list of positions that are equally spaced for each faculties
y_pos = np.arange(len(faculties))

# Creating and plotting the bar chart with the lists we have initialized
# Choosing one color for all of them
rects = ax.barh(y_pos, num_responses, color = "cornflowerblue")

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)

#Setting the y axis ticks at position y_pos and the labels are the faculties
ax.set_yticks(y_pos, labels=faculties)
ax.invert_yaxis()  # labels read from top-to-bottom

# Setting the y axis label as the "number of participants"
# Setting the x axis label as the "faculty of study"
ax.set_xlabel('Number of Participants')
ax.set_ylabel('Faculty of Study')

# Setting the title as "Faculty of Study among participants"
ax.set_title("Faculty of Study Among Participants")

# Display Horizontal Bar Chart
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 6 - ethnicity - selet all that apply """
 
# Horizontal bar chart 
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of ethnicites, number of responses
ethnicities = ["White / Caucasian / European", 
             "Black / African / Caribbean",
             "Indigenous / First Nation",
             "Hispanic / Latino",
             "East Asian",
             "Arab / Middle Eastern / North African",
             "South Asian / Southeast Asian",
             "East African",
             "Central Asian"]
num_responses = [16,7,2,3,6,45,37,1,1]

y_pos = np.arange(len(ethnicities)) # The list of label locations - ethnicities

# Creating and plotting the bar chart with the lists we have initialized
# Choosing one color for all of them
rects = ax.barh(y_pos, num_responses, color = "lightseagreen")

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)

#Setting the y axis ticks at position y_pos and the labels are the ethnicities
ax.set_yticks(y_pos, labels=ethnicities)
ax.invert_yaxis()  # Labels are read from top to bottom

# Setting the x axis label as the "number of responses"
# Setting the y axis label as the "ethnicities"
ax.set_xlabel('Number of Responses')
ax.set_ylabel('Ethnicities')

# Setting title as 'Ethnicites among participants for ChatGPT survey'
ax.set_title('Ethnicites among participants for ChatGPT survey')

# Display Horizontal Bar Chart
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 7 - people who have tried chatGPT """
#//////////////////////////////////////////////////////////////////////////////
# Based on gender
# Grouped bar chart

# Initializing a figure and axis to plot, with a constrained layout
fig, ax = plt.subplots(layout='constrained')

# Creating a tuple of genders 
# And dictionary of number of responses - Key:response, Value:tuple of counts
genders = ("Male", "Female")
num_responses = { "Yes": (29,27), "No": (17,31)}

# Fixing the scale of the y axis
plt.ylim(0,35)

x = np.arange(len(genders))  # The list of label locations - genders
width = 0.25  # Initialize the width of the bars
multiplier = 0 # Initialize multiplier to 0

# Looping through responses to plot grouped bars
for attribute, measurement in num_responses.items():
    
    # Calculating the offset for each group 
    # Offset makes sure that bars are evenly spaced
    offset = width * multiplier
    
    # Creating and plotting the grouped bar chart with each label
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    
    # Creates labels of values of each bar
    ax.bar_label(rects, padding=3)
    multiplier += 1 # Increment mutliplier to shift position of next bar

# Setting title as 'Survey responses of chatGPT use among genders'
ax.set_title('Survey responses of ChatGPT use among Genders')

# Setting the x axis ticks at position x+wdith and labels are genders
ax.set_xticks(x + width, genders)
 
# Creating the legend for the responses and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(loc='upper left', bbox_to_anchor=(0.4,1))

# Setting the y axis label as the "number of responses"
# Setting the x axis label as the "genders"
ax.set_ylabel('Number of Responses')
ax.set_xlabel("Genders")

# Display Grouped Bar Chart
plt.show()

# Pie chart for those who have used ChatGPT
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of genders, number of responses
genders = ["Male", "Female"]
sizes = [51.8,48.2]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each gender 
# 'autopct' formats how the % are displayed - here it is to 1 d.p.
ax.pie(sizes, labels=genders,colors = ["lime", "green"], autopct='%1.1f%%')
ax.set_title("Gender demographic for those who have tried ChatGPT")

# Display Pie Chart
plt.show()

# Pie chart for those who havent used chatGPT
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of genders, number of responses
labels = "Male", "Female"
sizes = [35.4,64.6]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each gender
# 'autopct' formats how the % are displayed - here it is to 1 d.p.
ax.pie(sizes, labels=genders,colors = ["red", "salmon"], autopct='%1.1f%%')
ax.set_title("Gender demographic for those who havent tried ChatGPT")

# Display Pie Chart
plt.show()

#//////////////////////////////////////////////////////////////////////////////
# Based on ages
# Table

# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Create a 2D list to store the info on chatGPT usage based on ages 
data = [['Ages', 'Have tried ChatGPT', 'Haven\'t Tried ChatGPT'],['17-20', '43', '40'],
        ['21-30', '12', '7'],['31-40', '0', '1'],['41-50', '1', '0']]

# Hiding the axes and ticks as it is not required here
ax.axis('off')

# Setting the title as "Survey response on ChatGPT usage based on ages"
ax.set_title("Survey Responses on ChatGPT usage based on Ages")

# Creating a table and adding it to the axes
table = ax.table(cellText=data, loc='center')
 
# Setting the preferred font size for table
table.auto_set_font_size(False)
table.set_fontsize(14) 

# Fixing the cell heights by looping through rows
cell_height = 0.1 # Initialize the cell height
for row in table._cells:
    table._cells[row]._height = cell_height

# Fxing the width of the columns
table.auto_set_column_width([0, 1, 2, 3, 4])

# Aligning the text in the center by looping through each cell
for cell in table._cells.values():
    cell.set_text_props(ha='center', va='center')

# Display table
plt.show()

#//////////////////////////////////////////////////////////////////////////////
# Based on region of study
# Grouped bar chart

# Initializing a figure and axis to plot, with a constrained layout
fig, ax = plt.subplots(layout='constrained')

# Creating a tuple of regions 
# And dictionary of number of responses - Key:response, Value:tuple of counts
regions = ("Asia", "North America" , "Africa" , "Europe" ,"Oceania")
response = { "Yes": (2,50,1,2,1), "No": (3,38,3,4,0)}

# Fixing the scale of y axis
plt.ylim(0,55)

x = np.arange(len(regions))  # The list of label locations - regions
width = 0.25  # Initialize the width of the bars
multiplier = 0 # Initialize multiplier to 0

# Looping through responses to plot grouped bars
for attribute, measurement in response.items():
    
    # Calculating the offset for each group 
    # Offset makes sure that bars are evenly spaced
    offset = width * multiplier
    
    # Creating and plotting the grouped bar chart with each label
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    
    # Creates labels of values of each bar
    ax.bar_label(rects, padding=3)
    multiplier += 1 # Increment mutliplier to shift position of next bar

# Setting title as 'Survey responses of chatGPT use among region of study'
ax.set_title('Survey responses of ChatGPT use among Regions of Study')

# Setting the x axis ticks at position x+wdith and labels are regions
ax.set_xticks(x + width, regions)

# Creating the legend for the responses and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(loc='upper left', bbox_to_anchor=(0.8,1))

# Setting the y axis label as the "number of responses"
# Setting the x axis label as the "regions"
ax.set_ylabel('Number of Responses')
ax.set_xlabel("Regions")

# Display grouped bar chart
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 8 - how often they use chatGPT """
#//////////////////////////////////////////////////////////////////////////////
# Overall
# Pie chart 

# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing the list of percentages by frequency, and list of frequencies
# As well as size of pie chart slices
labels = "1.9%","10.6%","16.3%","24%","47.1%"
frequency = ["Daily" ,"Often" , "Occasionally" , "Rarely" ,"Never"]
sizes = [1.9,10.6,16.3,24,47.1]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each frequency
ax.pie(sizes, labels=labels,colors = ["teal", "pink", "orange", "yellowgreen", "plum"],
       labeldistance =1.1) # Initialize distance between pie chart and the % labels

# Creating the legend for the responses and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(frequency, title = "Frequencies", loc= "center left", bbox_to_anchor=(1.1,0.5))

# Setting title as 'Survey responses of how often participants use ChatGPT'
ax.set_title("Survey responses of how often participants use ChatGPT")

# Display pie chart
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 9 - what do they use chatGPT for - select all that apply """
#//////////////////////////////////////////////////////////////////////////////
# Overall
# Horizontal bar chart 

# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of ethnicites, number of responses
uses = ["Job related traits", "Solve school subject problems",
        "Explain / Simplify concepts", "Advice", "Programming",
        "Quick research", "Generating ideas" , "Translator", "Just to chat",
        "Don't really use it"]
num_responses = [12,35,37,5,20,33,22,4,5,52]

y_pos = np.arange(len(uses)) # The list of label locations - uses

# Creating and plotting the bar chart with the lists we have initialized
# Choosing one color for all of them
rects = ax.barh(y_pos, num_responses, color = "lightgreen")

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)

#Setting the y axis ticks at position y_pos and the labels are the uses
ax.set_yticks(y_pos, labels=uses)
ax.invert_yaxis()  # Labels are read from top to bottom

# Setting the y axis label as the "Applications"
# Setting the x axis label as the "number of responses"
ax.set_ylabel('Applications')
ax.set_xlabel('Number of Responses')

# Setting title as 'Participant Responses on the applications of ChatGPT'
ax.set_title('Participant Responses on the applications of ChatGPT')

# Display horizontal bar chart
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 10 + 11 - pros and cons of ChatGPT - select all that apply """
#//////////////////////////////////////////////////////////////////////////////
# Overall
# Horizontal bar charts
# Pros

# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of benefits, number of responses
pros = ["Personalized feedback", "Quick and easy to use" , 
        "Increases efficiency" , "None of the above"]
num_responses = [48,69,60,20]

y_pos = np.arange(len(pros)) # The list of label locations - pros

# Creating and plotting the bar chart with the lists we have initialized
# Choosing one color for all of them
rects = ax.barh(y_pos, num_responses, color = "teal")

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)

#Setting the y axis ticks at position y_pos and the labels are the pros
ax.set_yticks(y_pos, labels=pros)
ax.invert_yaxis()  # Labels are read from top to bottom

# Setting the y axis label as the "Benefits"
# Setting the x axis label as the "number of responses"
ax.set_ylabel('Benefits')
ax.set_xlabel('Number of Responses')

# Setting title as 'Benefits of chatGPT towards education'
ax.set_title('Benefits of ChatGPT towards education')

# Display horizontal bar chart
plt.show()

# Cons
# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of downsides, number of responses
cons = ["Form of plagiarism", "Unreliable source of information", 
        "Heavy dependence on technology" , "Privacy concerns", "None of the above"]
num_responses = [71,44,56,25,17]

y_pos = np.arange(len(cons)) # The list of label locations - cons

# Creating and plotting the bar chart with the lists we have initialized
# Choosing one color for all of them
rects = ax.barh(y_pos, num_responses, color = "pink")

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)

# Setting the y axis ticks at position y_pos and the labels are the cons
ax.set_yticks(y_pos, labels=cons)
ax.invert_yaxis() # Labels are read from top to bottom

# Setting the y axis label as the "Downsides"
# Setting the x axis label as the "number of responses"
ax.set_ylabel('Downsides')
ax.set_xlabel('Number of Responses')

# Setting title as 'Downsides of chatGPT towards education'
ax.set_title('Downsides of ChatGPT towards education')

# Display horizontal bar chart
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 12 - challnges ChatGPT poses """
#//////////////////////////////////////////////////////////////////////////////
# Overall
# Horizontal bar chart

# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of challenges, number of responses
challenges = ["Web Traffic", "Fake news and propaganda" , "Data Privacy" ,
        "Ethical concerns" , "Student\'s knowledge", "Real-World harm",
        "Critical thinking", "None of the above"]
num_responses = [22,34,30,44,60,15,57,15]

y_pos = np.arange(len(challenges)) # The list of label locations - challenges

# Creating and plotting the bar chart with the lists we have initialized
# Choosing one color for all of them
rects = ax.barh(y_pos, num_responses, color = "gold")

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)

# Setting the y axis ticks at position y_pos and the labels are the challenges
ax.set_yticks(y_pos, labels=challenges)
ax.invert_yaxis() # Labels are read from top to bottom

# Setting the y axis label as the "Challenges"
# Setting the x axis label as the "number of responses"
ax.set_ylabel('Challenges')
ax.set_xlabel('Number of Responses')

# Setting title as 'Challenges that Chatgpt poses - Participant Responses'
ax.set_title('Challenges that Chatgpt poses - Participant Responses')

# Display horizontal bar chart
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 13 - how beneficial is chatgpt to students """
#//////////////////////////////////////////////////////////////////////////////
# Overall
# Bar Chart

# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing a list of degrees, number of responses 
# With colors representing each degree
degrees = ["Not at all", "Slightly", "Moderately", "Very" , "Extremely"]
num_responses = [10,10,46,29,9]
bar_colors = ["tab:purple", "tab:orange" ,"tab:green", "tab:blue" , "tab:pink"]

# Fixing scale of y axis
plt.ylim(0,50)

# Creating and plotting the bar chart with the lists we have initialized
rects = ax.bar(degrees,num_responses, color= bar_colors)

# Creates labels of values of each bar
ax.bar_label(rects, padding=3)
 
# Setting the y axis label as the "number of responses"
# Setting the x axis label as the "Degrees"
ax.set_ylabel('Number of Responses')
ax.set_xlabel("Degrees")

# Setting title as 'Bar Chart showing responses on how beneficial chatgpt is'
ax.set_title('Bar Chart showing responses on how beneficial ChatGPT is')

# Display bar chart
plt.show()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""" Question 14 - should ChatGPT be allowed in universities """
#//////////////////////////////////////////////////////////////////////////////
# Overall
# Pie chart

# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Initializing the list of percentages by frequency, and list of frequencies
# As well as size of pie chart slices
labels = "71.2%", "28.8%"
frequency = ["Yes" ,"No"]
sizes = [71.2, 28.8]

# Creating an plotting the pie chart with the sizes, labels
# With colors represeting each frequency
ax.pie(sizes, labels=labels,colors = ["teal", "pink"],
       labeldistance =1.1) # Initialize distance between pie chart and the % labels

# Creating the legend for the responses and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(frequency, title = "", loc= "center left", bbox_to_anchor=(1.0,0.8))

# Setting title as "Should ChatGPT be allowed in Universities?"
ax.set_title("Should ChatGPT be allowed in Universities?")

# Display pie chart
plt.show()

#//////////////////////////////////////////////////////////////////////////////
# Based on roles
# Grouped bar chart

# Initializing a figure and axis to plot, with a constrained layout
fig, ax = plt.subplots(layout='constrained')

# Creating a tuple of academic roles 
# And dictionary of number of responses - Key:response, Value:tuple of counts
roles = ("Undergraduate", "Masters" , "PhD" , "Professor")
response = { "Yes": (70,2,2,0), "No": (27,2,0,1)}

# Fixing scale of y axis
plt.ylim(0,75)

x = np.arange(len(roles))  # The list of label locations - roles
width = 0.25  # Initialize the width of the bars
multiplier = 0 # Initialize multiplier to 0

# Looping through responses to plot grouped bars
for attribute, measurement in response.items():
    
    # Calculating the offset for each group 
    # Offset makes sure that bars are evenly spaced
    offset = width * multiplier
    
    # Creating and plotting the grouped bar chart with each label
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    
    # Creates labels of values of each bar
    ax.bar_label(rects, padding=3)
    multiplier += 1  # Increment mutliplier to shift position of next bar

# Setting title as "Among Academic Roles: Should ChatGPT be allowed in Universities?"
ax.set_title('Among Academic Roles: Should ChatGPT be allowed in Universities?')

# Setting the x axis ticks at position x+wdith and labels are roles
ax.set_xticks(x + width, roles)

# Creating the legend for the responses and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(loc='upper left', bbox_to_anchor=(0.8,1))

# Setting the y axis label as the "number of responses"
# Setting the x axis label as the "Academic roles"
ax.set_ylabel('Number of Responses')
ax.set_xlabel("Academic Roles")

# Display grouped bar chart
plt.show()

#//////////////////////////////////////////////////////////////////////////////
# Based on faculties
# Grouped bar chart

# Initializing a figure and axis to plot, with a constrained layout
fig, ax = plt.subplots(layout='constrained')

# Creating a tuple of faculties
# And dictionary of number of responses - Key:response, Value:tuple of counts
faculties = ("Science", "Law" , "Arts" , "Community \n Services" , "Eng. & Arch. \n Science ", 
             "Design", "Health \n Science", "Business", "Other")
response = { "Yes": (27,1,4,1,18,3,3,16,1), "No": (8,0,3,2,5,2,1,6,3)}

# Fixing scale of y axis
plt.ylim(0,30)

x = np.arange(len(faculties))  # The list of label locations - faculties
width = 0.25  # Initialize the width of the bars
multiplier = 0 # Initialize multiplier to 0

# Looping through responses to plot grouped bars
for attribute, measurement in response.items():
    
    # Calculating the offset for each group 
    # Offset makes sure that bars are evenly spaced
    offset = width * multiplier
    
    # Creating and plotting the grouped bar chart with each label
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    
    # Creates labels of values of each bar
    ax.bar_label(rects, padding=3)
    multiplier += 1 # Increment mutliplier to shift position of next bar

# Setting title as "Among Faculties: Should ChatGPT be allowed in Universities?"
ax.set_title('Among Faculties: Should ChatGPT be allowed in Universities?')

# Setting the x axis ticks at position x+wdith and labels are faculties
ax.set_xticks(x + width, faculties)

# Rotating the x-axis tick labels to avoid faculty names overlapping
ax.set_xticklabels(faculties, rotation=45, ha='right')

# Creating the legend for the responses and formatting the layout 
# Sepcifying the location and placement of legend with 'loc' and 'bbox_to_anchor'
ax.legend(loc='upper left', bbox_to_anchor=(0.8,1))

# Setting the y axis label as the "number of responses"
# Setting the x axis label as the "Faculties"
ax.set_ylabel('Number of Responses')
ax.set_xlabel("Faculties")

# Display grouped bar chart
plt.show()

#//////////////////////////////////////////////////////////////////////////////
# Based on ethnicities
# Table

# Initializing a figure and axis to plot
fig, ax = plt.subplots()

# Creating a 2D list to store the info on chatGPT usage based on ages 
data = [['Ethnicities', 'In favor of ChatGPT', 'Against ChatGPT'],
        ['White / Caucasian / European', '11', '5'],
        ['Black / African / Caribbean', '5', '2'],
        ['Indigenous / First Nation', '2', '0'],
        ['Hispanic / Latino', '2', '1'],
        ['East Asian', '5', '1'],
        ['Arab / Middle Eastern / North African', '32', '13'],
        ['South Asian / Southeast Asian', '26', '11'],
        ['East African', '1', '0'],
        ['Central Asian', '1', '0']]


# Hiding the axes and ticks as it is not required here
ax.axis('off')

# Setting title as "Among Ethnicities: Should ChatGPT be allowed in Universities?"
ax.set_title("Among Ethnicities: Should ChatGPT be allowed in Universities?")

# Creating a table and adding it to the axes
table = ax.table(cellText=data, loc='center')

# Setting the preferred font size for table
table.auto_set_font_size(False)
table.set_fontsize(14)

# Fixing the cell heights by looping through rows
cell_height = 0.1 # Initialize the cell height
for row in table._cells:
    table._cells[row]._height = cell_height

# Fxing the width of the columns
table.auto_set_column_width([0, 1, 2, 3, 4])

# Aligning the text in the center by looping through each cell
for cell in table._cells.values():
    cell.set_text_props(ha='center', va='center')

# Display Table
plt.show()
