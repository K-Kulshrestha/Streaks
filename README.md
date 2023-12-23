# Streaks
<h2>Overview</h2>
Welcome to Streaks, a responsive and interactive web application designed to enhance user productivity through streak tracking. This document provides an overview of the key features, technologies, and security measures implemented in this project.

<h1>Features</h1>
<h2>Streak Tracking</h2>
One of the standout features of Streak is the streak tracking functionality. This feature is designed to motivate users by encouraging daily task completion. Users can easily track their progress and build streaks for increased engagement.

<h2>Responsive Web Application</h2>
Streak is built as a responsive web application, ensuring a seamless user experience across various devices. The integration of Flask, HTML, CSS, and JavaScript contributes to the application's responsiveness, making it accessible to a wide range of users.

<h2>Secure User Authentication</h2>
Security is a top priority in Stream. User authentication is implemented with bcrypt encryption to safeguard user credentials. This ensures that user data is protected from unauthorized access, providing a secure environment for users to manage their tasks and streaks.

<h2>MongoDB Data Storage</h2>
Efficient data storage is crucial for a dynamic web application, and Streak leverages MongoDB for this purpose. This NoSQL database allows for the efficient retrieval and management of user information and posts. The choice of MongoDB enhances the scalability and performance of the application.

<h2>Technologies Used</h2>
Flask: The web application framework that powers Streak.
HTML, CSS, and JavaScript: The trio of front-end technologies responsible for the user interface and interactivity.
bcrypt Encryption: Employed for secure user authentication, ensuring the confidentiality of user credentials.
MongoDB: The NoSQL database used for efficient storage and retrieval of user information and posts.
Getting Started
To run Streak locally, follow these steps:

Clone the repository: git clone https://github.com/K-Kulshrestha/Streaks
<br>
Install dependencies: pip install -r requirements.txt
<br>
Set up MongoDB and configure the connection details.
<br>
Run the application: python app.py
<br>
Access the application in your web browser: http://localhost:5000
