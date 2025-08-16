# Grade Processor

A Python tool that transforms simple text files containing student names and grades into PDF reports with charts and tables. Made for teachers and professors who want to create professional-looking representations of their students' grades.

## Features
- **Visual Reports**: Generates charts and tables from grade data
- **PDF Output**: Creates clean and visual PDF documents
- **Simple Input Format**: Works with basic text files and simple formatting
- **Flexible Grading**: Supports varying numbers of grades per student by calculating averages
- **Easy to use**: Just place your text file in the same folder as the program and run it

## Input Format
Create a text file with student data formatted as follows:
```
Student Name 1
1 2 3 4 5

Student Name 2
3 4 2 5 4 3

Student Name 3
5 4 3
```

### Format Rules:
- Student Name on one line
- Grades on the next, seperated by spaces
- Grades should be on a scale of 1-5 (1 being the best and 5 being the worst)
- Students can have different numbers of assignments/tests

## Installation

### Option 1: Download the Executable (Recommended)
1. Download the Executable directly
2. Your program will be ready for use

### Option 3: Run the source code
1. Download/Copy the Python code
2. Make sure you have Python installed on your system
3. Install the requirements:
`pip install -r requirements.txt`

## Usage
1. Create your grade data txt file (see example file or formatting above)
2. Place the text file in the same folder as the exe file
3. Run the program
4. The program will generate a PDF report with charts and tables in a couple of seconds

## What will it do?
The program will:
- Calculate each student's average grade
- Generate visual charts showing grade distribution and individual grades
- Produce tables that show the top 3 students as well as a full list sorted by last name
- Output everything into a PDF report

## System Requirements
- Windows operating system (for executable version)
- Python 3.x with required packages (for source code version)
- Text file with grade data in the specified format

## Target Audience
This tool is designed for:
- Teachers/Professors looking to create good-looking reports instead of Excel spreadsheets or text files
- Educators who want more visual grade analysis
- Anyone who needs polished and visual grade data

## Contributing and/or Support
If you encounter any issues or have questions about this tool, please create an issue on the Github page.
Feel free to submit issues and enhancement requests!
