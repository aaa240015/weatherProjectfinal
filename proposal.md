# Weather Environment Simulator

## Repository
GitHub Repo: https://github.com/aaa240015/weatherProjectfinal

## Description
This project is aimed at simulating weather enviroment depending on the mood of the user. It is deigned to help someone express their mood and how they feel in form of an art that is specicifally tailored to their preference. The project  will utilize the various aspects of digital arts to show how art and computing can come together to elevate a person's mood , reduce stress or even express their feeling through meditating and observing the art formulated from it.


## Features
  ### Various Weather states
  - It includes three weather states that include hot weather, stormy weather and calm weather. These states are controlled by the user through two ways
     * **Keyboard inputs:**The user presses the keys like S for stormy ,H for Hot and C for calm. These keys make the program transition into the specified weather states respectivley 
     * **Graphical user Interface input:** The Program also allows the user to change the state of the weather through clicking the provided User Interface Menu that .
     These two ways of changing the state of the weather makes it easier for one to get the full experience of the art.
     The three states have distinctive features to show their differences:
     * **Stormy weather:** Incorporates heavy cloud formations, animated raindrops, and flashes of lightning to mimic a realistic storm. The dynamic nature of this state emphasizes intensity and energy.
     * **Hot weater:** Features a sun that moves across the sky to reflect different times of day (morning, noon, evening). 
     * **Calm weather:**: There will be slowly moving clouds and the sun without any disruptions to mimic a calm enviroment
  ### Animals for each Weather state
  - To give the user a sense of relaxation, Each weather state can have set of different animals 
    The Stormy enviroment can have frogs since they're the only universal animals that have a swampy habitat and are always associated with wet enviroments. The Hot enviroment can have bunnies and the calm enviroment can have both bunnies and flying birds of vairous colors. I will use classes for each animal
  ### Customization features
	- **Sun Speed Adjustemnt:** This piece of art shall allow the user to increase the speed of the sun or increase the speed of it depending on the user preferences . I plan to use two button a plus and a minus button.
  - **Sky Color Customization:** The sky color shall also be dictated by the type of enviroment but also customizable by the user. I plan on using a color slider for the same effect.

## Challenges
- **Memory management** might be a challenge. Rendering all these items in the program might have a huge demand on the memory resources of one's machine and this is going to slow down the display of the items stated.Optimizing rendering and managing memory usage efficiently will be crucial for smooth performance
- **Accuratley simulating the three weather states** might be a challenge. Implementing randomness of each feature will require a lot of mathematical knowledge and knowing how to coordinate how various aspects of each element to synchronize during display seems to bring up a challenge and might need a lot of practise of trial and error.
- **Balancing  art with technology** to express emotions is challenging.It may be difficult to anticipate and accommodate every user’s preferred method of relaxation or emotional connection. 
## Outcomes
Ideal Outcome:
- Smooth and accurate rendering of the elements
- fully functional GUI and keyboard operations
- responsive customizable aspects
- immersive user experience to allow expression of emotions throught the program

Minimal Viable Outcome:
- A running program that shows three weather states with smooth transitions while switching occurs
- Simple visual differentiation for the three states

## Milestones

- Week 1 :Project planning 
  1. Set up the development enviroment with the necessary libraries
  2. Come up with  the design structure
- Week 2 :Prototyping
  1. Implement the three states prototypes 
  2. Try basic keyboard input and check their behaviour when changing the states
- Week 3 :Add features and animations
  1. Add moving animation to the program like moving objects (sun, clouds)
  2. Add clouds, sun and rainfall objects to the Display
  3. Introduce animal classes to the program
  4. Link the animals to various states
- Week 4: Customizable controls
  1. Add GUI controls and features such as text labels and buttons  
  2. add customisable features such as the sun speed controler and the color slider
- Week 5 (Final): Polishing and testing
  1. Optimize memory perfomances
  2. Run the program to check on errors and fix them
  3. Finish up and prepare to push the final draft to github
