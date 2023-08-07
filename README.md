# Face Recognition Attendance Software

## Introduction

This repository contains a Face Recognition Attendance Software that allows users to perform various tasks related to face recognition and attendance management. The software is developed using Python and utilizes various libraries such as OpenCV, Tkinter, PIL, and MySQL Connector.

## Setup and Installation

### Requirements

To run this software, you need to have the following installed:

1. Python 3.6 or higher
2. MySQL Server
3. MySQL Workbench (optional, for database management)

### Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries by running the following command: pip install -r requirements.txt
3. 3. Download and install MySQL Server and MySQL Workbench (optional) on your machine.

### Database Configuration

1. Open MySQL Workbench and create a new schema named 'face_recognizer'.
2. Create two tables within the 'face_recognizer' schema:
- Table 'register_details' with columns: 'First Name', 'Last Name', 'Mobile', 'Email', 'Security Qs', 'Security Ans', 'Password'.
- Table 'student' with columns: 'Dep', 'Course', 'Year', 'Semester', 'Student_id', 'Name', 'Div', 'RollNum', 'Gender', 'DOB', 'Email', 'Phone', 'Address', 'Teacher', 'PhotoSample'.
3. Set the username as 'root' and password as '@INDIA12tnb' for the database connection in the relevant Python files.

### Data Folder

Create a folder named 'data' in the root directory of the project. This folder will be used to store images for training.

## File Descriptions

1. **login.py**: This file contains the login window and authentication logic.
   
   ![Screenshot (169)](https://github.com/rehan1608/Face-Recognition-System/assets/72146315/e7f68c59-319f-4ed9-b10a-ae9064516ff6)


2. **main.py**: This file contains the main menu window with options for different functionalities.

  ![Screenshot (170)](https://github.com/rehan1608/Face-Recognition-System/assets/72146315/7fb5a980-9952-4860-9389-0db36a719f3e)


3. **student_details.py**: This file displays the details of students in a tabular format.

   ![Screenshot (171)](https://github.com/rehan1608/Face-Recognition-System/assets/72146315/ab354330-28b0-4168-abc9-212d182234b4)


4. **train.py**: This file is used to train the face recognition model using the images from the 'data' folder.

   ![Screenshot (172)](https://github.com/rehan1608/Face-Recognition-System/assets/72146315/b56b9fba-f698-451c-b30c-7279e28f30f8)


5. **face_detection.py**: This file contains the main face detection and recognition logic.

   ![Screenshot (174)](https://github.com/rehan1608/Face-Recognition-System/assets/72146315/0cc9b087-cac5-4cab-ab4a-a1516ba73a08)


6. **developer.py**: This file displays the developer details.

    ![Screenshot (175)](https://github.com/rehan1608/Face-Recognition-System/assets/72146315/91b4bb40-fb32-4ad6-8cef-a0a346e773cf)


7. **help.py**: This file provides help and instructions for using the software.

    ![Screenshot (176)](https://github.com/rehan1608/Face-Recognition-System/assets/72146315/582b36b8-65e2-406f-b98b-c63ac20b1fde)


8. **attendance.py**: This file manages the attendance data and updates the database.

    ![Screenshot (177)](https://github.com/rehan1608/Face-Recognition-System/assets/72146315/484178e4-63ec-4f7d-b54e-78c57504febd)



## Usage

1. Run the 'login.py' file to start the application.
2. Enter valid login credentials or register as a new user.
3. Use the main menu to navigate through different functionalities.

## Collaboration and Suggestions

I welcome collaboration and suggestions to further improve and enhance this Face Recognition Attendance Software project. If you are interested in contributing or have any valuable suggestions, I would be delighted to connect with you.

### How to Collaborate?

If you are passionate about face recognition technology, attendance management, or any related field, and you would like to contribute to the project, here's how you can collaborate:

1. **Code Contribution**: You can contribute by enhancing existing features, adding new functionalities, improving the user interface, or fixing any bugs. To collaborate on coding tasks, you can fork this repository, make your changes, and submit a pull request. We will review your changes and merge them into the main project if they align with our goals.

2. **Testing and Feedback**: Testing the software and providing feedback is another valuable way to contribute. You can report any issues or suggest improvements by creating an issue in the repository. Your feedback will help us make the software more robust and user-friendly.

3. **Documentation**: Clear and concise documentation is crucial for the project's success. You can help by improving the README.md file or writing documentation for new features. A well-documented project is more accessible to users and potential contributors.

4. **Spread the Word**: If you find this project interesting and useful, consider sharing it with others who might be interested. A larger user base and community involvement can drive the project's growth.

### Connect with Us

To collaborate or discuss any ideas related to the project, you can reach out to us through the following channels:

- **Email**: raorehan79@gmail.com
- **GitHub**: [https://github.com/rehan1608/Face-Recognition-System](https://github.com/rehan1608/Face-Recognition-System)
- **Website**: https://portfoliorehan.netlify.app/

I am open to all ideas and contributions, and I believe that collaborative efforts can lead to remarkable advancements. Let's work together to make this Face Recognition Attendance Software even better!
