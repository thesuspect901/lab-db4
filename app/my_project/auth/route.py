from flask import Blueprint, request
from .controller import UserController, StoryController, MediaController

# Створюємо Blueprints для кожного контролера
user_bp = Blueprint('user_bp', __name__, url_prefix='/api/users')
story_bp = Blueprint('story_bp', __name__, url_prefix='/api/stories')
media_bp = Blueprint('media_bp', __name__, url_prefix='/api/media')

# ============================
#        USER ROUTES
# ============================

@user_bp.route('/', methods=['GET'])
def get_all_users():
    """
    Get all users
    ---
    tags:
      - Users
    responses:
      200:
        description: List of all users
    """
    return UserController.get_all_users()


@user_bp.route('/with-stories', methods=['GET'])
def get_all_users_with_stories():
    """
    Get all users with their stories
    ---
    tags:
      - Users
    responses:
      200:
        description: Users with nested stories
    """
    return UserController.get_all_users_with_stories()


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: User object
      404:
        description: User not found
    """
    return UserController.get_user(user_id)


@user_bp.route('/', methods=['POST'])
def add_user():
    """
    Create user
    ---
    tags:
      - Users
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
              email:
                type: string
              password:
                type: string
    responses:
      201:
        description: User created
    """
    data = request.get_json()
    return UserController.add_user(data)


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update user
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
              email:
                type: string
              password:
                type: string
    responses:
      200:
        description: User updated
    """
    data = request.get_json()
    return UserController.update_user(user_id, data)


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete user
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: User deleted
    """
    return UserController.delete_user(user_id)


# ============================
#       STORY ROUTES
# ============================

@story_bp.route('/', methods=['GET'])
def get_all_stories():
    """
    Get all stories
    ---
    tags:
      - Stories
    responses:
      200:
        description: List of stories
    """
    return StoryController.get_all_stories()


@story_bp.route('/with-media', methods=['GET'])
def get_all_stories_with_media():
    """
    Get stories with attached media
    ---
    tags:
      - Stories
    responses:
      200:
        description: Stories + media
    """
    return StoryController.get_all_stories_with_media()


@story_bp.route('/<int:story_id>', methods=['GET'])
def get_story(story_id):
    """
    Get story by ID
    ---
    tags:
      - Stories
    parameters:
      - name: story_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Story object
    """
    return StoryController.get_story(story_id)


@story_bp.route('/', methods=['POST'])
def add_story():
    """
    Create story
    ---
    tags:
      - Stories
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              user_id:
                type: integer
    responses:
      201:
        description: Story created
    """
    data = request.get_json()
    return StoryController.add_story(data)


@story_bp.route('/<int:story_id>', methods=['PUT'])
def update_story(story_id):
    """
    Update story
    ---
    tags:
      - Stories
    parameters:
      - name: story_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      content:
        application/json:
          schema:
            type: object
            properties:
              user_id:
                type: integer
    responses:
      200:
        description: Story updated
    """
    data = request.get_json()
    return StoryController.update_story(story_id, data)


@story_bp.route('/<int:story_id>', methods=['DELETE'])
def delete_story(story_id):
    """
    Delete story
    ---
    tags:
      - Stories
    parameters:
      - name: story_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Story deleted
    """
    return StoryController.delete_story(story_id)


# ============================
#        MEDIA ROUTES
# ============================

@media_bp.route('/', methods=['GET'])
def get_all_media():
    """
    Get all media
    ---
    tags:
      - Media
    responses:
      200:
        description: Media list
    """
    return MediaController.get_all_media()


@media_bp.route('/<int:media_id>', methods=['GET'])
def get_media(media_id):
    """
    Get media by ID
    ---
    tags:
      - Media
    parameters:
      - name: media_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Media item
    """
    return MediaController.get_media(media_id)


@media_bp.route('/', methods=['POST'])
def add_media():
    """
    Add media
    ---
    tags:
      - Media
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              story_id:
                type: integer
              url:
                type: string
    responses:
      201:
        description: Media created
    """
    data = request.get_json()
    return MediaController.add_media(data)


@media_bp.route('/<int:media_id>', methods=['PUT'])
def update_media(media_id):
    """
    Update media
    ---
    tags:
      - Media
    parameters:
      - name: media_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      content:
        application/json:
          schema:
            type: object
            properties:
              url:
                type: string
    responses:
      200:
        description: Media updated
    """
    data = request.get_json()
    return MediaController.update_media(media_id, data)


@media_bp.route('/<int:media_id>', methods=['DELETE'])
def delete_media(media_id):
    """
    Delete media
    ---
    tags:
      - Media
    parameters:
      - name: media_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Media deleted
    """
    return MediaController.delete_media(media_id)
