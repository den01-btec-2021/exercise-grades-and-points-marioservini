[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6331382&assignment_repo_type=AssignmentRepo)
# Exercise 1.26 - Grades and Points

The table below describes how the grade for a particular course is determined. Write a program that gives a course grade according to the provided table.

| points | grade       |
| ------ | ----------- |
| < 0    | impossible! |
| 0-49   | failed      |
| 50-59  | 1           |
| 60-69  | 2           |
| 70-79  | 3           |
| 80-89  | 4           |
| 90-100 | 5           |
| > 100  | incredible! |

Sample outputs:

```plaintext
Give points [0-100]:
*37*
Grade: failed
```

```plaintext
Give points [0-100]:
*76*
Grade: 3
```

```plaintext
Give points [0-100]:
*95*
Grade: 5
```

```plaintext
Give points [0-100]:
*-3*
Grade: impossible!
```
