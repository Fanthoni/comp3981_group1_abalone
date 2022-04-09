# Abalone - Group 1
### Setting Up and Running the Program
Using Windows Terminal or PyCharm IDE is recommended.

First, make sure to have python installed on the machine (version 3.10 is the latest python version when this README file is written).
Then simply go to the root project directory and type:

```text
python gui.py
```

Abalone Tkinter GUI game board will appear.

#### Playing the Game
To start playing a game, you must first select the 'settings' button located in the middle of the GUI, and configure 
the game settings.
(NOTE: Pressing the 'Start Game' button without selecting the 'settings' button will not result in starting the game)
    ==> Pressing 'settings' opens up another GUI window with simple radio buttons and text box inputs in order 
    to configure your next game settings.
    ==> Once finished setting your game options, select the green 'Apply Game Configuration' to apply changes!

Now, to start your match, simply hit the 'Start Game' button, and the timer will begin running for the 'black' 
marble player.

If it is the player's turn, marble movements are made the following way:
    1) click on the desired marbles to move
        (NOTE: If you have selected the wrong marbles to move, hit the 'reset' button located bottom-left of the game board GUI interface)
    2) then select the one of the 'direction' buttons located bottom left of the game board GUI (i.e. NORTHWEST, EAST, ... ) to actuate your marble(s) movement


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

### Authors
1. Jason Banh
2. Anson Chan
3. Samuel Cheon
4. Ferrel Anthoni
