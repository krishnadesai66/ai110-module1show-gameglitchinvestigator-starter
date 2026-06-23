# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

I mainly noticed that the hint would tell me to go higher or go lower, despite needing to go the opposite direction. I was also unable to start a
new game when I hit the new game button. The game would not check if my guess was out of range for the difficulty level I chose. The range and attempts in the side panel and main panel do not match either which is confusing for the player. The game also claims I have 1 attempt left when I do not.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior   | Actual Behavior | Console Output / Error |
|-------|---------------------|-----------------|------------------------|
   80        Go lower           Go higher          N/A
|--------|--------------------|-----------------|------------------------|
 New game  New game would start    nothing         N/A
|--------|-------------------|-----------------|------------------------|
   55       "Out of range"      Go higher          N/A
|-------|-------------------|-----------------|------------------------|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Extension in VS Code. A suggestion it made was to set the count of attempts to 0 instead of 1 so that I have an accurate count of attempts. I had tested it this correction by playing the game again and finally being able to finish it with the attempts on the screen. The AI did not suggest anything misleading. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I tested if the bug was fixed by testing it with the original input I tested before the fix and then using different input. I tested the corrected hints but using multiple inputs and seeing if I was able to inch closer to the correct answer (which I was able to do). I also had tested off nominal test cases to ensure that the hints were letting me know I was guessing the wrong number. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

Session state saves storage across different script reruns. Streamlit reruns forces the UI to reflect changes in session state without requiring a manual user interaction. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to use AI more intentionally! Instead of a constant feedback loop with AI, being more intentional with my responses can really save time and learning. 

- What is one thing you would do differently next time you work with AI on a coding task?
I would be more thorough with previewing my task at hand. Perhaps utilizing AI to break down what I have to work with before diving in with changes.


- In one or two sentences, describe how this project changed the way you think about AI generated code.
It's not always perfect and requires a human pair of eyes to correct it! 
