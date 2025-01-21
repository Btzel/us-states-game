# U.S. States Game

An interactive geography learning game that challenges players to name all 50 U.S. states, built with Python using Turtle graphics and Pandas.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Latest-red)
![Turtle](https://img.shields.io/badge/Turtle-Graphics-green)
![CSV](https://img.shields.io/badge/CSV-Data-yellow)

## 🎯 Overview

This project creates an educational game where players:
1. View a blank U.S. map
2. Enter state names
3. See correct guesses appear on the map
4. Track their progress
5. Generate a list of missed states

## 🎮 Game Features

### Interactive Elements
- Blank U.S. map visualization
- Text input for state names
- Real-time score tracking
- State name placement on correct guesses

### Data Management
- CSV-based state data storage
- Coordinate system for state placement
- Progress tracking
- Missing states report generation

## 🔧 Technical Components

### Game Management System
```python
def compare_answer(self, answer, score):
    is_found = False
    counter = 0
    for state_name in self.data_dict['state'].values():
        if answer.lower() == state_name.lower():
            is_found = True
            self.state_name = state_name.title()
            self.state_position = (self.data_dict['x'][counter],
                                 self.data_dict['y'][counter])
            self.found_states.append(self.state_name)
            score += 1
            break
        counter += 1
    return is_found, self.state_name, self.state_position, score
```

### Key Features
1. **State Verification**
   - Case-insensitive matching
   - Duplicate entry prevention
   - Coordinate mapping

2. **Progress Tracking**
   - Real-time score updates
   - States found counter
   - Missing states tracking

3. **Data Processing**
   - CSV data handling
   - State coordinates mapping
   - Missing states report

## 💻 Implementation Details

### Class Structure
- `GameManager`: Core game logic and state management
- `Screen`: Display and input handling
- Data handling with Pandas DataFrames

### Data Management
- States data stored in CSV format
- X,Y coordinates for each state
- Dynamic updates of remaining states

## 🚀 Usage

1. Install required packages:
```bash
pip install pandas
```

2. Run the game:
```bash
python main.py
```

3. Enter state names when prompted
4. Type 'exit' to end the game
5. Check 'missing_states.csv' for unguessed states

## 🎯 Game Rules

1. Enter the name of any U.S. state
2. Correctly guessed states appear on the map
3. Track your progress with the score counter
4. Try to name all 50 states
5. Use 'exit' to end the game at any time

## 🛠️ Project Structure

```
us_states_game/
├── main.py           # Game initialization and loop
├── game_manager.py   # Game logic and state management
├── screen.py         # Display management
├── 50_states.csv     # State data and coordinates
└── blank_states_img.gif  # Game map image
```

## 📊 Features

### Input Processing
- Case-insensitive state matching
- Duplicate entry prevention
- Exit command handling

### Output Generation
- Missing states report
- Score tracking
- Visual state placement

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

Burak TÜZEL