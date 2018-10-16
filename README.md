# Term Project Proposal: Makeup Color Matching
Team Members: Jonathan Beltran, Jingyu (Jack) He, Pranjal Joshi, Angela Tsung, Aaron Wendell\
MIS 3640

## The Big Idea

The main idea of our project is to create a tool to help beauty lovers discover a scientifically precise shade of color for their makeup products. We will focus on the aspect of color matching from a photo. We will explore web scraping, database queries, as well as object-relational mapping. Our minimum viable product will be a working webpage in which users can upload a photo of their skin and receive color recommendations in their foundation shade. Our stretch goal will be to create a database with makeup products and link in product recommendations in the corresponding shade for the user.

## Learning Goals

### Shared Goals:
Collectively, we hope to learn to apply design thinking and agile methodology to this project and learn to use Python toolkits and frameworks to build a working product.We want to learn to grow and apply our knowledge of Python combined with learning to apply and use databases and queries.

### Individual Goals:
* Jonathan: Have experience on how to build a solution/product by using Python and other programming platforms.
* Jack: Use Python as a tool to provide creative solution to meet task requirements as a entry level developer.
* Pranjal: Get a first hand experience on how the final product looks and what kind of elements are used to build it. 
* Angela: Experience project management with a emphasis on the technical aspect, learn and apply object-relational mapping
* Aaron: Create a python program that connects to other platforms such as SQL, html, etc.

## Implementation Plan

For this project, we plan on using SQL Alchemy for object-relational mapping, the Flask web framework for its extensions in object-relational mapping, and the OpenCV library for color detection aspects. First, we will need to figure out what information and inputs we will need from the user in order to determine a result and output. In order to match colors, we will need a colors database and use the Euclidean distance between a number of random points  to determine a balanced color point from the image. For our stretch goal, we will need to web scrape makeup product information and color correspondence in order to map our color output to specific product recommendations.

For this initial high-level brainstorm of our project components, the user data we will collect will be an image upload of the user’s skin color. Ths user interactions we will need to build include a place for the user to upload a photo and an interface for the user to navigate their corresponding shade and makeup products. Some of the objects and logics we will have include the randomized choice of a color point, corresponding color hex codes, as well as a lookup function for the right color. The product will include a beginning scene, an uploading scene, as well as a browsing scene for the final recommendations.

## Project Schedule

* Week 1: Research on database and library needed (color number, skin color, photo recognition system, etc)
* Week 2: Prototype a mock-up / pseudo-code that help vision how the whole system works
* Week 3: Start building on the query mechanism on the products & color database
* Week 4: Start develop/adopt the photo/face recognition system that identifies the color of a specific zone in a picture
* Week 5: Begin on the GUI/user interface prototyping phase of development
* Week 6: Thanksgiving Holiday
* Week 7: Prepare for project design review, deliver a beta version that has part of the functionalities of the final project. Integration and testing on the integrated WIP
*Week 8: Debugging and final testing

## Collaboration Plan

In terms of delegating the work, we will be using the agile development method so that we can improve our product through iterations. We will divide the project into main sections that make up the whole project (Query system, color database, and other features we may think of throughout the course of the project) and split the team accordingly. Depending on the difficulty of the task, there will be pairs or small teams of three. To make sure we keep up with internal and hard deadlines, we will use our project schedule to make a Gantt chart, that way, we will hold ourselves accountable individually and as a team. If a particular team member is skilled in a certain area of the project, they will take the lead and delegate as they see fit, but not to the point where there is an imbalance of work.

## Risks

Since we have 5 team members, we can have the risk of having ‘free riders’ or simply miscommunications can easily slow down the progress of the work. If works are spread out between all the team members, we can also bear the risk of having bottlenecks if some team members slack on some of the tasks.
On the technical side of the project, we would expect that the most difficult aspect of the project will be the ‘translation process’ of turning one’s skin color to a color code. This process can involve video/photo recognition that might go out of bound on what we have on hands so far, as well as querying a data frame can be difficult at the moment. In all, the difficulty of some part of the project can cause delays to the delivery time and technical help such as consulting online or with professor is needed.

## Additional Course Content

To complete the project, we need to understand how to handle data frames/database by learning basic actions like queries or calculations that can estimate the proximity of the test result vs. what we have in the database. Furthermore, because user interface is necessary for this project (in the case of having user to input the photo/capturing his/her face), learning about basic GUI like asking for inputs and displaying outputs would be essential. Finally, learning how to adopt an API for reading the skin color code would be helpful, in the case there is one.