Run application : fastapi dev app.py


Traditional Database (SQL/MongoDB):
Users: id, username, email, password, age, weight, height, goals
Workouts: id, user_id, plan_name, date, exercises, duration
Nutrition: id, user_id, date, meals, calories, macros
Progress: id, user_id, workout_id, sets, reps, weights, notes
Vector Database:
Exercise Knowledge: exercise descriptions, instructions, benefits
Nutrition Knowledge: food information, dietary guidelines, meal plans
Fitness Knowledge: training principles, recovery, injury prevention
API Endpoints
Authentication
POST /auth/register - User registration
POST /auth/login - User login
GET /auth/user/{user_id} - Get user profile
Core CRUD
GET/POST/PUT/DELETE /workouts - Workout management
GET/POST/PUT/DELETE /exercises - Exercise database
GET/POST/PUT/DELETE /nutrition - Nutrition logging
GET/POST/PUT/DELETE /progress - Progress tracking
AI Chat
POST /chat/ask - Send question, get RAG-powered response
GET /chat/history/{user_id} - Get chat history
