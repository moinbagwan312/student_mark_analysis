 ◾ Student Marks Analysis using NumPy

 

 A beginner-friendly Python project that analyzes student marks with NumPy. It calculates totals, averages, subject-wise statistics, pass/fail status, and rankings, then prints a final performance report.

 

 ◾ Features

 

 - Total and average marks for each student

 - Subject-wise average, highest, and lowest marks

 - Strongest and weakest subject

 - Topper and lowest performer

 - Pass/Fail report (a student fails if any subject is below 40)

 - Student ranking by total marks

 - Consolidated class performance report

 

 ◾ Tech Stack

 

 - Python 3.x

 - NumPy

 

 ◾ Project Structure

 

 ```

 student-marks-analysis/

 ├── student_analysis.py    Main analysis script

 ├── requirements.txt       Dependencies

 └── README.md              Project documentation

 ```

 

 ◾ Installation

 

 1. Clone the repository:


 2. (Optional) Create a virtual environment:

 &x20;  ```bash

 &x20;  python -m venv venv

 &x20;  source venv/bin/activate       Windows: venv Scripts activate

 &x20;  ```

 

 3. Install dependencies:

 &x20;  ```bash

 &x20;  pip install -r requirements.txt

 &x20;  ```

 

 ◾ Usage

 

 ```bash

 python student_analysis.py

 ```

 

 ◾ Dataset

 

 | Student | Python | SQL | Mathematics | Statistics |

 |---------|--------|-----|-------------|------------|

 | Rahul   | 85     | 78  | 90          | 88         |

 | Priya   | 92     | 89  | 95          | 91         |

 | Amit    | 45     | 55  | 60          | 50         |

 | Sneha   | 76     | 82  | 79          | 85         |

 | Karan   | 30     | 40  | 35          | 45         |

 

 ◾ Sample Output (Summary)

 

 ◾Class Summary

 - Total Students: 5

 - Class Average: 69.5

 - Passed: 4

 - Failed: 1

 

 ◾◾Ranking◾◾

 

 | Rank | Student | Total | Average | Status |

 |------|---------|-------|---------|--------|

 | 1    | Priya   | 367   | 91.75   | PASS   |

 | 2    | Rahul   | 341   | 85.25   | PASS   |

 | 3    | Sneha   | 322   | 80.5    | PASS   |

 | 4    | Amit    | 210   | 52.5    | PASS   |

 | 5    | Karan   | 150   | 37.5    | FAIL   |

 

 ◾◾Subject Performance◾◾

 

 | Subject     | Average | Highest | Lowest |

 |-------------|---------|---------|--------|

 | Python      | 65.6    | 92      | 30     |

 | SQL         | 68.8    | 89      | 40     |

 | Mathematics | 71.8    | 95      | 35     |

 | Statistics  | 71.8    | 91      | 45     |

 

 ◾- Strongest Subject: Mathematics

 ◾- Weakest Subject: Python

 ◾- Topper: Priya

 ◾- Lowest Performer: Karan

 

 ◾ NumPy Concepts Used

 

 | Function | Purpose |

 |----------|---------|

 | `np.array()` | Create arrays for students, subjects, and marks |

 | `np.sum(axis=1)` | Total marks per student |

 | `np.mean(axis=0/1)` | Average per subject / per student |

 | `np.max()` / `np.min()` | Highest and lowest marks |

 | `np.argmax()` / `np.argmin()` | Index of topper, weakest subject, etc. |

 | `np.any()` | Check for any failed subject |

 | `np.argsort()` | Rank students by total marks |

 | Boolean indexing | Filter passed/failed students |

 

 ◾ Possible Improvements

 

 - Load marks from a CSV file using pandas

 - Add grade calculation (A, B, C, ...)

 - Visualize results with Matplotlib

 - Accept marks as user input

 

