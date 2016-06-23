# Virtual_Assistant

Virtual Assistant is a python based side-project to explore the capabilities of the Natural Language Toolkit when combined with basic AI. The goal is to achieve simple, human-like question and answer interaction between the user and the computer. Virtual Assistant will make use of various APIs to draw information from, all of which will be called from one central controller using natural language speech-to-text input and naturalized language text-to-speech output. 

Simple user/computer interaction: 
```
User: echo $(date +%x_%r)
Computer: 06/22/2016_11:06:23 PM
```
Goal interaction:
```
User (spoken): "What time is it in Paris?"
Computer (spoken): "It is currently 6:08 AM in Paris, France."
```
---
#####Project Phases:
1. Functionality (June 8 - Present)
  * Create a variety of API and system controllers to accept a single string input and return a single string output.
2. Centralize Control
  * Create a central controller to call the controllers from phase 1, allowing a more flexible experience.
  * Create a simple model to store user information to reduce API calls, and prepare for more naturalized IO.
3. Output
  * Implement a text-to-speech library for all output.
  * Create a system to naturalize the return strings to sound more human-like.
4. Input
  * Implement a speech-to-text library for all input.
  * Use the NLTK to breakdown the input.
  * Create a system to understand the input to run commands.
5. AI
  * Remember recent queries and results
  * Remember common speech patterns
  * Improve and naturalize text and speech processing
