# Abalone - Group 1

### Instruction on How to Run State Space Generator
To run the state space generator, simply follow the following:
1. Navigate into the root of the project
2. Insert the .input files into the project root directory
3. In the command line or terminal, navigate to the root project again
4. Run the following command\
**Note**: Python3.10 is the required python sdk version to run the executable

```text
python abalone.py
```

5. Input the file name
6. The corresponding *Test<#>.move* and *Test<#>.board* file will be generated under the *testOutput* folder

### Setting Up and Running the Program
This abalone program can be executed wherever emojis can be printed properly. Using Windows Terminal or PyCharm IDE is recommended.

Note: The Windows default console host (conhost.exe) does not support printing Unicode characters. However, the new Windows Terminal does.

First, make sure to have python installed on the machine (version 3.10 is the latest python version when this README file is written).
Then simply go to the root project directory and type 

```text
python abalone_UI.py
```

Abalone Game Menu will show
```text
---Main Menu---
1. Start Game
2. Set Starting Positions
3. Set Game Mode
4. Set Player Colors
5. Set Turn Time
6. Set Turn Limit
7. Exit
Input: 
```

Starting the game will show the current board like so
```text
          I 🟥 🟥 🟥 🟥 🟥 
        H 🟥 🟥 🟥 🟥 🟥 🟥 
      G 🟩 🟩 🟥 🟥 🟥 🟩 🟩 
     F 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 
   E 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 
     D 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 9
      C 🟩 🟩 🟦 🟦 🟦 🟩 🟩 8
        B 🟦 🟦 🟦 🟦 🟦 🟦 7
          A 🟦 🟦 🟦 🟦 🟦 6
              1  2  3  4  5

---Player 1---
Time remaining: X
Moves remaining: X
1. Make Move
2. View Previous Moves
3. Pause Game
4. Stop Game
Input: 
```


### Authors
1. Jason Banh
2. Anson Chan
3. Samuel Cheon
4. Ferrel Anthoni
