# Flask_Webhook_API_for_Subscription_Management
This repository contains a Flask application that serves as a webhook listener for managing user subscription data in a MongoDB database. The application allows for the insertion, retrieval, and updating of user records, particularly focusing on updating the subscription end date via webhook POST requests. This is ideal for subscription-based services that require real-time updates to user data.

# Key Features:

MongoDB Integration: Seamlessly connects to a MongoDB cluster for data storage and management.

Webhook Listener: Handles POST requests to update subscription end dates for specific users.

Data Validation: Ensures incoming webhook data is properly validated before processing.

Sample User Data: Includes a script to insert and update sample user data for testing purposes.

Perfect for SaaS providers or anyone needing to automate subscription management tasks with a robust, backend solution.

# Installation
1. Clone the Repository

git clone https://github.com/arnob72/Flask_Webhook_API_for_Subscription_Management.git

cd Flask_Webhook_API_for_Subscription_Management


3. Install Dependencies

Ensure you have Python and pip installed. Then, install the necessary Python packages:

pip install Flask pymongo

3. Configure MongoDB

Update the MongoDB connection string in the script with your own credentials:

client = MongoClient('mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority&appName=<appname>')

4. Run the Application

Start the Flask server:

python app.py
The server will run locally at http://127.0.0.1:5000.

# Usage
1. Insert Sample Data

Run the provided script to insert a sample user into the MongoDB database:

2. Test the Webhook

Use a tool like Postman to send a POST request to the webhook endpoint:

POST http://127.0.0.1:5000/webhook

Content-Type: application/json
{
    "user_id": "u1603001",
    "subscription_end_date": "2024-01-15"
}

3. Verify the Update

Check your MongoDB database to confirm that the subscription end date for the specified user has been updated.
