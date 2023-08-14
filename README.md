# [Tic Tac Toe AI: A Modern Tic Tac Toe Game using Customtkinter](https://github.com/PythonDecorator)

<br />

![version](https://img.shields.io/badge/version-1.0.0-blue.svg)

--- 

## Table of Contents

* [Overview](#overview)
* [Demo](#demo)
* [Documentation](#documentation)
* [Features](#features)
* [Converting to Executable](#converting-to-executable)
* [Controls](#Controls)
* [Licensing](#license)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [For Open Source](#For-open-source)
* [Social Media](#Social-media)

<br />

## Overview

The "Tic Tac Toe " project aims to bring the classic game of Tic Tac Toe to life as a desktop application using the
CustomTkinter library in Python.

In this project I have created a user-friendly and visually appealing interface for playing Tic Tac Toe against another
player or against the computer with AI.

I have only implemented the AI logic to block the user from winning on the third move to make the game easier, In the
next version of this game, I will add the difficulty choice and implementations.

<br />

## Demo

![demo-blog.gif](apps/static/assets/demo/demo-blog.gif)

- **Download the One file .exe file from the dist or download folder**
- **You don't need to install anything, just download, click and start playing.**

<br />

## Features

> Features

1. ✅ `Interactive Game Board`: Interactive game board with a 3x3 grid using buttons that respond to player clicks for
   placing X and O markers.

2. ✅ `Winning Conditions`: Implement the logic to check for winning combinations (horizontal, vertical, and diagonal)
   and declare a winner when a player completes a line of their markers.

3. ✅ `Tie Detection`: Detect a tie or draw scenario when the game board is completely filled, and no player has won.

4. ✅ `Restart and Reset`: Provide options to restart the game after a match is completed or to reset the game board
   without changing the player's turn.

5. ✅ `Visual Feedback`: Enhance user experience by visually highlighting the winning line and displaying clear messages
   for different game outcomes.

6. ✅ `Score Tracking`: Keep track of each player's wins, losses, and ties throughout multiple game sessions.

7. ✅ `Responsive Design`: Ensure that the game interface is responsive and visually appealing on different screen sizes
   and resolutions.

<br />

## Documentation

This game was built based on the Pygame documentation

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

## Reporting Issues

GitHub Issues is the official bug tracker for the Tic Tac Toe.

## Technical Support or Questions

If you have questions contact me [okpeamos.ao@gmail.com]() instead of opening an issue.

## For Open Source

"Tic Tac Toe Game App with CustomTkinter" is an interactive game that showcases your skills in GUI programming and game
development. This project allows you to explore the mechanics of a classic game, apply decision-making logic for AI
opponents, and design an appealing user interface. Whether you're aiming to build a portfolio project or simply enjoy
creating an entertaining game, this project offers a rewarding experience that combines coding prowess with a touch of
nostalgia.

## Social Media

- Twitter: <https://twitter.com/AmosBrymo67154>
- Instagram: <https://www.instagram.com/pythondecorator>

<br />

---

