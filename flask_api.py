

from pymongo import MongoClient

client = MongoClient('mongodb+srv://username:password@defaultcluster.tje53xt.mongodb.net/?retryWrites=true&w=majority&appName=DefaultCluster')

db = client['SubscriptionApp']
collection = db['users']

new_user = {
       "id": "u1603001",
       "machine_id": "WIN-SLQ38IMAQJL; DESKTOP-NJH43FF; vmi1505649; vmi1560941; DESKTOP-QEOSP9D",
       "machine_limit": 0,
       "run_limit": 0,
       "total_run": 11346,
       "paid": 1,
       "proxy": 1,
       "group_posting": 1,
       "multiple_machine": 1,
       "multiple_account": 1,
       "duplicate_img": 0,
       "delete_similar_listings": 0,
       "custom": 1,
       "subscription_end_date": "2023-12-15",
       "profile": "https://www.upwork.com/ab/messages/rooms/room_ca89c504d5caa8d9e3b2c3ca16d63b37",
       "client_name": "Anthony",
       "services": "item",
       "payment_type": "once",
       "custom_modifications": "posting in random locations"
   }

collection.insert_one(new_user)

user = collection.find_one({"id": "u1603001"})
print(user)

collection.update_one({"id": "u1603001"}, {"$set": {"paid": 0}})

"""webhook"""

from flask import Flask, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)

# MongoDB connection (use your actual credentials)
client = MongoClient('mongodb+srv://username:password@defaultcluster.tje53xt.mongodb.net/?retryWrites=true&w=majority&appName=DefaultCluster')

db = client['SubscriptionApp']
collection = db['users']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    user_id = data.get('user_id')
    new_subscription_end_date = data.get('subscription_end_date')

    if not user_id or not new_subscription_end_date:
        return jsonify({"error": "Missing user_id or subscription_end_date"}), 400

    result = collection.update_one({"id": user_id}, {"$set": {"subscription_end_date": new_subscription_end_date}})
    
    if result.matched_count == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "Webhook received and processed"}), 200

if __name__ == '__main__':
    app.run()
