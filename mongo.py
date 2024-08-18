import pymongo
from typing import List, Dict, Any
import streamlit as st

import streamlit

url = "mongodb+srv://eli:DxhkMWiiylHIq3eB@atlascluster.m6tavxq.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(url)

# Create a database
db: object = client["translate"]

# Create a collection
collection: object = db["new_test"]


def insert_user_name(user_name: str, amount) -> None:
    # Create a dictionary with the user data
    user_data = {
        'user_name': user_name,
        'amount': amount,
        'stock': {}
    }
    # Insert the dictionary into the collection
    collection.insert_one(user_data)


def find_user_name(user_name: str) -> List[Dict[str, Any]]:
    """
    Queries the database for a user by their username.

    Args:
        user_name (str): The username of the user to find.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the user's data from the database.
    """
    # Query the collection to find documents matching the username
    data = collection.find({'user_name': user_name})

    # Convert the cursor to a list of dictionaries
    return list(data)


def get_all_users() -> List[Dict[str, Any]]:
    """
    Queries the database for all users and removes the '_id' field from each document.

    Args:
        collection (Collection): The MongoDB collection to query.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing all users' data from the database, with '_id' removed.
    """
    # Query the collection to find all documents
    cursor = collection.find()

    # Convert the cursor to a list of dictionaries
    data = list(cursor)

    # Remove the '_id' field from each document
    cleaned_data = [{k: v for k, v in doc.items() if k != '_id'} for doc in data]

    return cleaned_data


def update_user_name(user_name: str, new_amount) -> None:
    """
    Updates the amount for a given user by their username.

    Args:
        user_name (str): The username of the user to update.
        new_amount: The new amount to set for the user.
    """
    try:
        # Specify the query and the new values to update
        query = {'user_name': user_name}
        new_values = {'$set': {'amount': new_amount}}

        # Perform the update
        result = collection.update_one(query, new_values)

        if result.matched_count == 0:
            print("No user found with the specified username.")
        else:
            print("User updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


def update_user_stock(user_name: str, stock_symbol: str, amount: int) -> None:
    try:
        # Specify the query and the new values to update
        query = {'user_name': user_name}
        update_values = {'$set': {f'stock.{stock_symbol}': amount}}

        result = collection.update_one(query, update_values)
        if result.matched_count == 0:
            print("No user found with the specified username.")
        else:
            print("Stock updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


def delete_user(user_name: str) -> None:
    try:
        # Specify the query to match the user
        query = {'user_name': user_name}
        result = collection.delete_one(query)

        if result.deleted_count == 0:
            st.error(f"No user found with the username: {user_name}.")
        else:
            st.success(f"User '{user_name}' deleted successfully.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
