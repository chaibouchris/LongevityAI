# Health Tracker API

## 📌 Overview
The **Health Tracker API** is a backend system that calculates a **health score** based on multiple health metrics such as blood test results, physical activity, sleep duration, BMI, smoking habits, and overall stability. This API dynamically updates user health scores and compares them against a system-wide average.

## 🚀 Features
- 🏥 **Health Score Calculation** based on various health parameters.
- 📊 **Real-Time System Average Comparison** to assess overall health trends.
- 📡 **REST API Endpoints** for user health data management.
- 🛠 **Built with FastAPI & SQLAlchemy** for high performance and scalability.
- 🔐 **Secure Database Integration** using MySQL.

## 🏗️ Project Structure
```
health_tracker/
│── app/
│   ├── db/                 # Database models and configurations
│   ├── routes/             # API route definitions
│   ├── score_calculators/  # Score calculation logic
│   ├── services/           # Business logic and calculations
│   ├── utils/              # Helper functions and utilities
│   ├── main.py             # API entry point
│── .env                    # Environment variables (DB connection, etc.)
│── requirements.txt        # Python dependencies
│── README.md               # Documentation
```

## 🏁 Installation & Setup
### Prerequisites
- Python 3.10+
- MySQL Server
- Virtual Environment (optional but recommended)

### 📦 Install Dependencies
```sh
pip install -r requirements.txt
```

### 🛠 Setup Environment Variables
Create a **`.env`** file in the project root and configure the following:
```
SQLALCHEMY_DATABASE_URL=mysql+pymysql://username:password@localhost/health_tracker
```

### 🚀 Run the Server
```sh
uvicorn app.main:app --reload
```
The API will be available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

## 🔥 API Endpoints
### User Management
- **POST** `/users` → Create a new user.
- **GET** `/users` → Retrieve all users.
- **GET** `/users/{user_id}` → Get details of a specific user.
- **PUT** `/users/{user_id}` → Update user details.
- **DELETE** `/users/{user_id}` → Delete a user.

### Health Score Calculation
- **GET** `/get_health_score/{user_id}` → Calculate and retrieve the health score for a user.
- **GET** `/get_latest_health_average` → Retrieve the latest system-wide health score average.
- **POST** `/calculate_system_health_average` → Update the system-wide average health score.
- **GET** `/health_scores` → Retrieve all health scores.
- **GET** `/health_scores/{user_id}` → Retrieve a specific user's health score.

### Health Data Management
- **POST** `/blood_tests` → Add a blood test record.
- **GET** `/blood_tests` → Retrieve all blood test records.
- **GET** `/blood_tests/{test_id}` → Retrieve a specific blood test record.
- **DELETE** `/blood_tests/{test_id}` → Delete a blood test record.
- **POST** `/physical_activity` → Add a physical activity record.
- **GET** `/physical_activity` → Retrieve all physical activity records.
- **GET** `/physical_activity/{activity_id}` → Retrieve a specific physical activity record.
- **DELETE** `/physical_activity/{activity_id}` → Delete a physical activity record.
- **POST** `/sleep_activity` → Add a sleep activity record.
- **GET** `/sleep_activity` → Retrieve all sleep activity records.
- **GET** `/sleep_activity/{sleep_id}` → Retrieve a specific sleep activity record.
- **DELETE** `/sleep_activity/{sleep_id}` → Delete a sleep activity record.

### Additional Calculations
- **GET** `/bmi_score` → Calculate BMI-based score.
- **GET** `/comparison_score` → Compare the user's health score with the system average.
- **GET** `/smoking_penalty` → Retrieve smoking penalty calculation.
- **GET** `/stability_bonus` → Retrieve stability bonus calculation.
- **GET** `/system_health_average` → Retrieve system-wide health average.
- **GET** `/system_health_average/history` → Retrieve historical health averages.

## 📊 Health Score Calculation Breakdown
The **health score** is calculated using multiple health indicators:
| Category                | Max Score |
|-------------------------|----------|
| 🩸 Blood Test Results  | 50       |
| 🚶 Physical Activity   | 15       |
| 😴 Sleep Duration     | 10       |
| ⚖️ BMI Score         | 20       |
| 🚬 Smoking Penalty    | (-10) to 0 |
| 📈 Stability Bonus    | 5        |
| 📊 System Comparison | 10       |
| **Total Possible Score** | **100** |

📖 **For a detailed breakdown of the scoring system, check** [Health Score Explanation](./health_score_explanation.md)

## 🛠 Technologies Used
- **FastAPI** 🚀 (Backend framework)
- **SQLAlchemy** 🗄 (ORM for database management)
- **MySQL** 🛢 (Database)
- **Pydantic** 📏 (Data validation)
- **Uvicorn** ⚡ (ASGI Server)

## 🤝 Contributing
We welcome contributions! Feel free to **fork** the repository and submit a **pull request** with improvements.

## 📜 License
This project is licensed under the **MIT License**.

---
🚀 **Developed with ❤️ by Chai Shalom Bouchris**

