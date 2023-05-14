# Machine Learning CS0451 Project Proposal

Cece Ziegler, David Bryne, Julia Fairbank, Sam Ehrsam
April 7th, 2023

# Utilizing Biomechanical and Force Plate Data to Predict Bat Speed for Baseball Hitters

# Abstract
Our project will address the future of baseball training by understanding the underlying factors that contribute to athletic success. We are pulling our data from the Open Biomechanics Project (OBP), which is an open-source project from Driveline Baseball, the leading data-driven player development facility in Seattle, WA. The data was captured using a combination of ground force plates, a marker motion capture system, bat speed sensors, and ball flight monitors. As a result, the data available is rather robust, with time series force plate data in all three dimensions, hip, torso, shoulder, and hand velocities, as well as bat speed and ball flight data. In essence, every piece of information that is responsible for a baseball swing is accounted for. 
Our project hopes to determine the most important factors that affect players' statistics, primarily bat speed. We anticipate beginning with an initial unsupervised data scrub to determine which variables have the strongest correlation to bat speed, then using those variables to build some predictive model. 
Ultimately, we will evaluate our success based on our ability to explain our dataset, our predictive model, and our approach. Regardless of how strong our model ends up, we are prioritizing creating a project that is detailed and easy to understand. Throughout this project, we anticipate making weekly goals that correspond to our greater goal of creating a strong, fair predictive model. As we work through the next few weeks, setting and reaching weekly goals will allow us to be realistic about the work ahead to meet our final goal, and allow us to adjust as necessary. 

# Motivation and Question

In building a predictive model for bat speed, we could help inform coaching decisions when it comes to developing hitters. If an athlete's true bat speed closely aligns with their predicted bat speed, this would mean that they are currently moving efficiently in the swing. In other words, they are transferring all of the energy they produce through the bat and into contact. On the other hand, if a hitter did not meet their predicted bat speed value, this would be indicative of mechanical inefficiency. As a result, a coach with access to this data and model would be able to bucket athletes into two main groups: strength-focused and skill-focused. Players with efficient movements would benefit from strength training to increase their baseline capabilities for bat speed, whereas players with high force production would benefit from a mechanical focus.

# Planned Deliverables

For our project, we plan to have a Python package that will include the code we will use to create our predictive model. We will include detailed documentation that will explain our methodology and decisions. Along with our Python package, we will include two Jupyter notebooks. The first Jupyter notebook will include our exploratory data analysis and supervised learning portion where we will determine which features of our dataset are most important in predicting the bat speed of an athlete. Our second Jupyter notebook will include our unsupervised predictive model in which we will fit our model on a training data set and then test our model to see how well it performs. We will use our Python package within our Jupyter notebooks to run our models and present our findings throughout the project in the Jupyter notebooks. These notebooks will include an in-depth analysis of our key variables along with graphs to support our findings. Additionally, our notebook will include our final predictive model, along with additional supportive graphs that detail our model’s performance. 

We will consider our deliverables successful if we are able to have a working model and an analysis of its strength. We mainly hope to achieve a strong explanation of our project and process as to detail how we were able to create our model and where further work is needed. 

As we work, we may find that our planned deliverables are either sufficient or insufficient for our process, and we are excited to adapt as necessary.

# Written Deliverables

Comprehensive blog post detailing our project, methods, and results. 

# Resources Required

From the OBP dataset, we will be focusing on baseball-hitting data, specifically force plate and joint velocity to predict bat speed. 

The data can be collected from the following link: https://github.com/drivelineresearch/openbiomechanics

# Individual Learning Goals

Julia: My goals were focused on creating a strong work dynamic, ensuring that we are meeting consistently and keeping up with deadlines. Additionally, from a personal standpoint, I have a goal of taking the lead on a certain section or algorithm. While I’m not sure what that specifically will look like, I’m excited to figure out which section complements my interests and what I hope to work on. 

Cece: My first goal for our final project was to complete a project that involved predictive analysis in sports. I am excited to learn about what factors most impact the bat speed of an athlete and how machine learning is impactful in determining the factors. Additionally, my goals included submitting my portion of the project on time, and working with my group members to draft and revise different sections. I am excited to work with my group members on this project and learn more about how machine learning is used with predictive models in sports. 

David: My initial goals had a heavy emphasis on communication and writing. Given that the dataset we have chosen is focused on baseball, I expect that I will take on a large role in synthesizing our findings into digestible prose. I also noted in my goals that I wanted to play an active role in implementation despite my lack of experience. I hope that through a significant project such as this, I will be able to improve my ability to take an idea from conception to production utilizing concepts we have learned in class. 

# Risk Statement

One potential risk that we could foresee is that bat speed is not easily explained by isolated biomechanical factors. Baseball swings are highly coordinated actions that rely on well sequenced movements for contact to occur. By simply looking at points of data rather than the full picture, we may not accurately predict bat speed values. Another potential risk is that the data may have rather high variability and bat speed is far too nuanced to be modeled. Baseball swings are unique to the individual, and we may find that different players can be successful with different strengths. 


# Ethics Statement

Male individuals with access to resources have the potential to benefit from this project. The resources necessary to capture this data are extensive and expensive, meaning that there will be certain individuals that benefit more than others from this project. Because the dataset that we are using is a male dataset, female athletes have the potential to be excluded from this project as the data is fit to male standards.  

Our project will individually benefit male athletes and their coaching staff to tailor their training to their individual talents and weaknesses, allowing them to be the best athlete they can be. While the impact will be contained within the sports world, we are excited to work on this project. We do not anticipate a global effect from this project but are excited by the potential for other sports teams, male and female, to adopt a similar method. 



