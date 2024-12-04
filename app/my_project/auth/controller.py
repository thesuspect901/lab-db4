from .dao import *

from flask import jsonify, request

class UserController:
    @staticmethod
    def get_all_users_with_stories():
        users = UserDAO.get_all_users_with_stories()
        return jsonify(users), 200

    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        return jsonify(users), 200
    
    @staticmethod
    def get_user(user_id):
        user = UserDAO.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({'message': 'User not found'}), 404

    @staticmethod
    def add_user(data):
        if not data or not all(key in data for key in ('username', 'email', 'password', 'signup_date')):
            return jsonify({'message': 'Invalid data'}), 400
        success = UserDAO.add_user(data['username'], data['email'], data['password'], data['signup_date'])
        if success:
            return jsonify({'message': 'User added successfully!'}), 201
        return jsonify({'message': 'Failed to add user'}), 500
    
    @staticmethod
    def update_user(user_id, data):
        if not data or not all(key in data for key in ('username', 'email', 'password', 'signup_date')):
            return jsonify({'message': 'Invalid data'}), 400
        success = UserDAO.update_user(user_id, data['username'], data['email'], data['password'], data['signup_date'])
        if success:
            return jsonify({'message': 'User updated successfully!'}), 200
        return jsonify({'message': 'User not found or failed to update'}), 404
    
    @staticmethod
    def delete_user(user_id):
        try:
            UserDAO.delete_user(user_id)
            return jsonify({'message': 'User deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting user: {e}'}), 500


class StoryController:
    @staticmethod
    def get_all_stories_with_media():
        stories = StoryDAO.get_all_stories_with_media()
        return jsonify(stories), 200
    
    @staticmethod
    def get_all_stories():
        stories = StoryDAO.get_all_stories()
        return jsonify(stories), 200
    
    @staticmethod
    def get_story(story_id):
        story = StoryDAO.get_story_by_id(story_id)
        if story:
            return jsonify(story), 200
        return jsonify({'message': 'Story not found'}), 404
    
    @staticmethod
    def add_story(data):
        if not data or not all(key in data for key in ('user_id', 'created_at')):
            return jsonify({'message': 'Invalid data'}), 400
        success = StoryDAO.add_story(data['user_id'], data['created_at'])
        if success:
            return jsonify({'message': 'Story added successfully!'}), 201
        return jsonify({'message': 'Failed to add story'}), 500
    
    @staticmethod
    def update_story(story_id, data):
        if not data or not all(key in data for key in ('user_id', 'created_at')):
            return jsonify({'message': 'Invalid data'}), 400
        success = StoryDAO.update_story(story_id, data['user_id'], data['created_at'])
        if success:
            return jsonify({'message': 'Story updated successfully!'}), 200
        return jsonify({'message': 'Story not found or failed to update'}), 404
    
    @staticmethod
    def delete_story(story_id):
        try:
            StoryDAO.delete_story(story_id)
            return jsonify({'message': 'Story deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting story: {e}'}), 500

class MediaController:
    @staticmethod
    def get_all_media():
        media = MediaDAO.get_all_media()
        return jsonify(media), 200
    
    @staticmethod
    def get_media(media_id):
        media = MediaDAO.get_media_by_id(media_id)
        if media:
            return jsonify(media), 200
        return jsonify({'message': 'Media not found'}), 404
    
    @staticmethod
    def add_media(data):
        if not data or not all(key in data for key in ('story_id', 'media_type', 'media_url')):
            return jsonify({'message': 'Invalid data'}), 400
        success = MediaDAO.add_media(data['story_id'], data['media_type'], data['media_url'])
        if success:
            return jsonify({'message': 'Media added successfully!'}), 201
        return jsonify({'message': 'Failed to add media'}), 500
    
    @staticmethod
    def update_media(media_id, data):
        if not data or not all(key in data for key in ('story_id', 'media_type', 'media_url')):
            return jsonify({'message': 'Invalid data'}), 400
        success = MediaDAO.update_media(media_id, data['story_id'], data['media_type'], data['media_url'])
        if success:
            return jsonify({'message': 'Media updated successfully!'}), 200
        return jsonify({'message': 'Media not found or failed to update'}), 404
    
    @staticmethod
    def delete_media(media_id):
        try:
            MediaDAO.delete_media(media_id)
            return jsonify({'message': 'Media deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting media: {e}'}), 500
        
