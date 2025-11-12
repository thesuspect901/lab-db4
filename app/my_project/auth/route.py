from flask import Blueprint, request
from .controller import UserController, StoryController, MediaController

# Створюємо Blueprints для кожного контролера
user_bp = Blueprint('user_bp', __name__, url_prefix='/api/users')
story_bp = Blueprint('story_bp', __name__, url_prefix='/api/stories')
media_bp = Blueprint('media_bp', __name__, url_prefix='/api/media')

# ---------- User Routes ----------
@user_bp.route('/', methods=['GET'])    
def get_all_users():
    return UserController.get_all_users()

@user_bp.route('/with-stories', methods=['GET'])
def get_all_users_with_stories():
    return UserController.get_all_users_with_stories()

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    return UserController.add_user(data)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return UserController.update_user(user_id, data)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)


# ---------- Story Routes ----------
@story_bp.route('/', methods=['GET'])
def get_all_stories():
    return StoryController.get_all_stories()

@story_bp.route('/with-media', methods=['GET'])
def get_all_stories_with_media():
    return StoryController.get_all_stories_with_media()

@story_bp.route('/<int:story_id>', methods=['GET'])
def get_story(story_id):
    return StoryController.get_story(story_id)

@story_bp.route('/', methods=['POST'])
def add_story():
    data = request.get_json()
    return StoryController.add_story(data)

@story_bp.route('/<int:story_id>', methods=['PUT'])
def update_story(story_id):
    data = request.get_json()
    return StoryController.update_story(story_id, data)

@story_bp.route('/<int:story_id>', methods=['DELETE'])
def delete_story(story_id):
    return StoryController.delete_story(story_id)


# ---------- Media Routes ----------
@media_bp.route('/', methods=['GET'])
def get_all_media():
    return MediaController.get_all_media()

@media_bp.route('/<int:media_id>', methods=['GET'])
def get_media(media_id):
    return MediaController.get_media(media_id)

@media_bp.route('/', methods=['POST'])
def add_media():
    data = request.get_json()
    return MediaController.add_media(data)

@media_bp.route('/<int:media_id>', methods=['PUT'])
def update_media(media_id):
    data = request.get_json()
    return MediaController.update_media(media_id, data)

@media_bp.route('/<int:media_id>', methods=['DELETE'])
def delete_media(media_id):
    return MediaController.delete_media(media_id)
