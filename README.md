# [Tic Tac Toe AI: A Modern Tic Tac Toe Game](https://github.com/PythonDecorator)

<br />

![version](https://img.shields.io/badge/version-1.0.0-blue.svg)

--- 
![tic tac toe thumbnail.png](demo%2Ftic%20tac%20toe%20thumbnail.png)
## Table of Contents

* [Overview](#overview)
* [Demo](#demo)
* [Documentation](#documentation)
* [Features](#features)
* [Flow Chart](#flow-chart)
* [Converting to Executable](#converting-to-executable)
* [Controls](#Controls)
* [Licensing](#license)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [For Open Source](#For-open-source)
* [Social Media](#Social-media)

<br />

## Overview

This "Tic Tac Toe " project brings the classic game of Tic Tac Toe to life as a desktop application using the
in Python.

In this project I have created a user-friendly and visually appealing interface for playing Tic Tac Toe against 
the computer with AI.


<br />

## Demo
![Tic Tac Toe Demo.gif](demo%2FTic%20Tac%20Toe%20Demo.gif)

- **Download the One file .exe file from the dist folder**
- **You don't need to install anything, just download, click and start playing.**

<br />

## Features

> Some main features

1. ✅ `Interactive Game Board`: Interactive game board with a 3x3 grid using buttons that respond to player clicks for
   placing X and O markers.

2. ✅ `Winning Conditions`: Implemented logic to check for winning combinations (horizontal, vertical, and diagonal)
   and declare a winner when a player completes a line of their markers.

3. ✅ `Tie Detection`: Detects a tie or draw scenario when the game board is completely filled, and no player has won.

4. ✅ `Restart and Reset`: Provided options to restart the game after a match is completed or to reset the game board.

5. ✅ `Visual Feedback`: Enhanced user experience by displaying clear messages for different game outcomes.

6. ✅ `Score Tracking`: Keep track of each player's wins, losses, and ties throughout multiple game sessions.

7. ✅ `Responsive Design`: Ensures that the game interface is responsive and visually appealing on different screen sizes
   and resolutions.

<br />

## Flow Chart
![Tic Tac Toe Flow.png](files%2Fflow%20chart%2FTic%20Tac%20Toe%20Flow.png)

<br />


## Documentation

This game was built based on the customtkinter and Pygame documentation

<br /> 

## Converting to Executable

PyInstaller is a popular tool that allows you to convert Python scripts into standalone executable files for various
platforms, effectively creating desktop applications.

- You can use PyInstaller options to customize the behavior and appearance of the generated executable. Refer to the
  PyInstaller documentation for more information on available options.
- Keep in mind that PyInstaller generates a self-contained executable, but the size of the executable might be larger
  due
  to the inclusion of the Python interpreter and any dependencies, it's best to use venv to make sure only packages used
  in the
  project are included.
- Be sure to test the generated executable on the
  target platform to ensure everything works as expected.

<br />

> Install modules via `VENV`

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Create the .exe file

```bash
$ pyinstaller main.spec 
```

<br />

## Controls

- Computer X starts the game after the first round turn shifts to the Player
- Click on each grid to place symbol
- The result of the game is displayed at the end of the game
- A track of player scores is maintained
- Click restart to play again

<br />

## License

This project is licensed under the MIT license. See also the attached LICENSE file.

<br />

## Reporting Issues

GitHub Issues is the official bug tracker for the Tic Tac Toe.

<br />

## Technical Support or Questions

If you have questions contact me okpeamos.ao@gmail.cominstead of opening an issue.

<br />

## For Open Source

"Tic Tac Toe Game App with CustomTkinter" is an interactive game that showcases your skills in GUI programming and game
development. This project allows you to explore the mechanics of a classic game, apply decision-making logic for AI
opponents, and design an appealing user interface. Whether you're aiming to build a portfolio project or simply enjoy
creating an entertaining game, this project offers a rewarding experience that combines coding prowess with a touch of
nostalgia.

<br />

## Social Media

- Twitter: <https://twitter.com/AmosBrymo67154>
- Instagram: <https://www.instagram.com/pythondecorator>

<br />

---

