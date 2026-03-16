# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1.) The "New Game" button doesn't start a new game
2.) When I enter a number that is higher than the target, it tells me to go higher. 
3.) When I enter a number that is lower than the target, it tells me to go lower. It seems like the hints are inverted. 
4.) The easier is not easier. It is supposed to be between 1-20 but the # is 97 
5.) The blue header with the instructions does not update the interval. 
6.) The hard (1-50) is easier than the medium (1-100)
7.) When the level changes from hard to easy, the secret number doesn't change

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot and Claude. One correct suggestion was that Copilot told me that when the user changes the difficulty, the secret number doesn't reset and the number of attempts does not reset so I had to fix that. Specifically, it gave me code to implement these changes. I implemented these changes and then verified by running the web app and testing it. One suggestion that was incorrect by Copilot is that I asked it to fix the higher or lower message and it still didn't realize the reversed logic of the original was incorrect. Since I knew the logic myself, I knew that Copilot was wrong. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was fixed by testing it in streamlit and using pytest. One test I ran using pytest was checking if the higher or lower message outputs were consistent and correct. Another test I ran manually was inputting numbers and seeing what the output message was. Originally, they were reversed which helped me to identify the error. Copilot helped me to design pytests by generating me one. 

---
## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Reruns: Every time you interact with a Streamlit app like click a button, type in a box, or move a slider, Streamlit reruns your entire Python script from top to bottom. It's not like a normal app where only one function runs when you click a button. The whole file re-executes every single time.

Session state: Because the script reruns from scratch every time, any regular variables you created get wiped. Session state is Streamlit's way of letting you save values that survive across reruns. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to is finding errors myself and then asking Copilot to help me fix them rather than only using AI to find errors as well. As a result, one thing I plan to do differently is to depend less on AI to find errors and debug. While AI is faster and easier, I also need to practice identifying errors in the code itself. 

This project changed the way I think about AI generated code because it made me realize that its not that great at fixing code just yet unless you copy and paste everything in. It requires a lot more prompt engineering and giving it context. 
