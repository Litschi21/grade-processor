import matplotlib.pyplot as plt
import os
import pandas as pd
from PIL import Image
import re
from reportlab.pdfgen import canvas
from reportlab.rl_config import defaultPageSize
import string
import sys

def set_align_for_column(table, col, align="left"):
    cells = [key for key in table._cells if key[1] == col]
    for cell in cells:
        table._cells[cell]._loc = align
        table._cells[cell]._text.set_horizontalalignment('left')

alphabet = tuple([letter for letter in string.ascii_letters])
digits = tuple([str(digit) for digit in range(10)])
students = {}

pdf_file = os.curdir + '/grade_report.pdf'
filename = os.curdir + '/grades.txt'
err_file = os.curdir + '/error.txt'

try:
    with open(pdf_file, 'x'):
        pass
except FileExistsError:
    pass

# Initialize PDF values
documentTitle = 'Grade Report'
title = 'Grade Report'

# Creating a pdf object
pdf = canvas.Canvas(pdf_file)
width  = defaultPageSize[0]
height = defaultPageSize[1]
pdf.setTitle(documentTitle)

# Write title on pdf
pdf.setFont('Courier-Bold', 36)
pdf.drawString(width // 2 - 125, height-50, title)

# Read the txt file and make a dictionary with each student's name and their corresponding grade
try:
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(alphabet):
            student_name = line.strip()
            students[student_name] = []
        elif line.startswith(digits):
            grades = list(map(int, re.findall(r'\d+', line)))
            if students:
                student = list(students.keys())[-1]
                students[student] = grades
        else:
            continue
except FileNotFoundError:
    with open(err_file, 'a+') as f:
        f.write(f'Error: file does not exist.')
except Exception as e:
    with open(err_file, 'a+') as f:
        f.write(f'Error: {e}')

if not students:
    print('No students found in file.')
    sys.exit(1)

# Gets the average grade of each student
for name, grades in students.items():
    if grades:
        avg = round(sum(grades) / len(grades), 1)
        students[name] = avg

# Histogram of Grades - histogram showing grade distribution
avg_grades = [round(grade) for grade in students.values()]

fig1, ax1 = plt.subplots()
grade_hist = ax1.hist(avg_grades, bins=[1, 2, 3, 4, 5, 6], align='left', rwidth=0.9, color='#1e305c')
plt.xticks([1, 2, 3, 4, 5])

plt.xlabel('Average Grade')
plt.ylabel('Number of Students')
plt.title('Average Grade Distribution')

# Tables - two tables showing top 3 and bottom 3 students
# Top Table
fig2, ax2 = plt.subplots()

fig2.patch.set_visible(False)
ax2.axis('off')
ax2.axis('tight')

# Define Data
top_data = []
full_data = []

sorted_students = dict(sorted(students.items(), key=lambda x: x[1]))
sorted_items = list(sorted_students.items())
for keys, values in sorted_items[:3]:
    top_data.append([keys, values])

sorted_students = dict(sorted(students.items(), key=lambda x: x[0].split()[-1]))
sorted_items = list(sorted_students.items())
for keys, values in sorted_items:
    full_data.append([keys, values])

# Visualize Table
df_top = pd.DataFrame(top_data, columns=['Name', 'Grade'])
tb_top = ax2.table(cellText=df_top.values, colLabels=df_top.columns, loc='center')

set_align_for_column(tb_top, col=0)
set_align_for_column(tb_top, col=1)

# Full table
fig3, ax3 = plt.subplots()

fig3.patch.set_visible(False)
ax3.axis('off')
ax3.axis('tight')

df_full = pd.DataFrame(full_data, columns=['Name', 'Grade'])
tb_full = ax3.table(cellText=df_full.values, rowLabels=list(range(1, len(students.keys())+1)), colLabels=df_full.columns, loc='center')

set_align_for_column(tb_full, col=0)
set_align_for_column(tb_full, col=1)

# Student Performance Trend - sorted scatter plot showing all students' averages
fig4, ax4 = plt.subplots()

sorted_grades = sorted(students.values(), reverse=True)
student_scatter = ax4.scatter(sorted_grades, list(range(1, len(students)+1)), color='#1e305c')

plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.title('All Student Grades')

# Make all the charts images, so it can be drawn onto pdf
grade_hist = os.curdir + '/grade_histogram.png'
student_scatter = os.curdir + '/student_scatterplot.png'
tb_top = os.curdir + '/top_table.png'
tb_full = os.curdir + '/full_table.png'

# Save all chart images
fig1.savefig(grade_hist)
fig2.savefig(tb_top)
fig3.savefig(tb_full)
fig4.savefig(student_scatter)

# Resize tables
img1 = Image.open(tb_top)
img2 = Image.open(tb_full)

bbox1 = img1.getbbox()
bbox2 = img2.getbbox()

if bbox1:
    cropped1 = img1.crop(bbox1)
    cropped1.save('top_table.png')

if bbox2:
    cropped2 = img2.crop(bbox2)
    cropped2.save('full_table.png')

# Draw charts onto PDF
pdf.drawImage(grade_hist, 140, height-440, width=480, height=360)
pdf.drawImage(student_scatter, 0, height-800, width=480, height=360)

# Create new page
pdf.showPage()

sorted_student_names = list(sorted_students.keys())
pdf.setFont('Courier-Bold', 16)
pdf.drawString(width // 2 - 90, height-50, 'Top 3 Students')
pdf.drawImage(tb_top, 100, height-110, width=350, height=50)

pdf.drawImage(tb_full, 100, height-160-350, width=350, height=350)

# Save PDF
pdf.save()

# Delete images
os.remove(grade_hist)
os.remove(student_scatter)
os.remove(tb_top)
os.remove(tb_full)

if os.path.exists(err_file):
    os.remove(err_file)
