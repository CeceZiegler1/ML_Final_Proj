# Machine Learning CS0451 Project Proposal

Cece Ziegler, David Bryne, Julia Fairbank
April 7th, 2023

# Utilizing Biomechanical and Force Plate Data to Predict Bat Speed for Baseball Hitters

# Abstract

Our project will address the future of baseball training by understanding the underlying factors that contribute to athlethic success. We are pulling our data from the Open Biomechanics Project (OBP), which is an open source project from Driveline Baseball, the leading data driven player development facility in Seattle, WA. The data was captured using a combination of ground force plates, a marker motion capture system, bat speed sensors, and ball flight monitors. As a result, the data available is rather robust, with time series force plate data in all three dimensions, hip, torso, shoulder, and hand velocities, as well as bat speed and ball flight data. In essence, every piece of information that is responsible a baseball swing is accounted for. 

Our project hopes to determine the most important factors that affect players' statistics, primarily bat speed. We anticipcate beginning with an initial unsupervised data scrub to determine which variables have the strongest correlation to bat speed, then using those variables to build some predictive model. 

Ultimately, we will evaluate our success based on our ability to explain our dataset, our predicitive model, and our approach. Regardless of how strong our model ends up, we are priortizing creating a project that is detailed and easy to understand. Throughout this project, we anticipate making weekly goals that correspond to our greater goal of creating a strong, fair predicitive model. As we work through the next few weeks, setting and reaching weekly goals will allow us to be realistic about the work ahead to meet our final goal, and allow us to adjust as necessary. 

# Motivation and Question

In building a predictive model for bat speed, we could help inform coaching decision when it comes to developing hitters. If an athlete's true bat speed closely aligns with their predicted bat speed, this would mean that they are currently moving efficiently in the swing. In other words, they are transferring all of the energy they produce through the bat and into contact. On the other hand, if a hitter did not meet their predicted bat speed value, this would be indicitive of a mechanical inefficiency. As a result, a coach with access to this data and model would be able to bucket athletes into two main groups: strength focused and skill focused. Players with efficient movements would benefit from strength training to increase their baseline capabilities for bat speed, whereas players with high force production would benefit from a mechanical focus.

# Planned Deliverables

For our project, we plan to have a Python package that will include the code we will use to create our predictive model. We will include detailed documentation that will explain our methodology and decisions. Along with our Python package, we will include two Jupyter notebooks. The first Jupyter notebook will include our exploratory data analysis and supervised learning portion where we will determine which features of our dataset are most important in predicting the bat speed of an athlete. Our second Jupyter notebook will include our unsupervised predictive model in which we will fit our model on a training data set and then test our model to see how well it performs. We will use our Python package within our Jupyter notebooks to run our models and present our findings throughout the project in the Jupyter notebooks. These notebooks will include an in-depth analysis of our key variables along with graphs to support our findings. Additionally, our notebook will include our final predictive model, along with additional supportive graphs that detail our model’s performance. 

We will consider our deliverables successful if we are able to have a working model and an analysis of its strength. We mainly hope to achieve a strong explanation of our project and process as to detail how we were able to create our model and where further work is needed. 

As we work, we may find that our planned deliverables are either sufficient or insufficient for our process, and we are excited to adapt as necessary.

# Written Deliverables

Comprehensive blog post detailing our project, methods, and results. 

# Resources Required

From the OBP dataset, we will be focusing on baseball-hitting data, specifically force plate and joint velocity. 

The data can be collected from the following link: https://github.com/drivelineresearch/openbiomechanics


https://github.com/drivelineresearch/openbiomechanics

