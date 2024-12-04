class User:
    def __init__(self, user_id, username, password, email, created_at):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.created_at = created_at

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'created_at': self.created_at
        }


class Story:
    def __init__(self, story_id, user_id, created_at):
        self.story_id = story_id
        self.user_id = user_id
        self.created_at = created_at

    def to_dict(self):
        return {
            'story_id': self.story_id,
            'user_id': self.user_id,
            'created_at': self.created_at
        }


class Media:
    def __init__(self, media_id, story_id, media_type, media_url):
        self.media_id = media_id
        self.story_id = story_id
        self.media_type = media_type
        self.media_url = media_url

    def to_dict(self):
        return {
            'media_id': self.media_id,
            'story_id': self.story_id,
            'media_type': self.media_type,
            'media_url': self.media_url
        }


class Reaction:
    def __init__(self, reaction_id, reaction_type):
        self.reaction_id = reaction_id
        self.reaction_type = reaction_type

    def to_dict(self):
        return {
            'reaction_id': self.reaction_id,
            'reaction_type': self.reaction_type
        }


class Comment:
    def __init__(self, comment_id, user_id, story_id, comment_text, created_at):
        self.comment_id = comment_id
        self.user_id = user_id
        self.story_id = story_id
        self.comment_text = comment_text
        self.created_at = created_at

    def to_dict(self):
        return {
            'comment_id': self.comment_id,
            'user_id': self.user_id,
            'story_id': self.story_id,
            'comment_text': self.comment_text,
            'created_at': self.created_at
        }


class Follower:
    def __init__(self, follower_id, user_id, follower_user_id):
        self.follower_id = follower_id
        self.user_id = user_id
        self.follower_user_id = follower_user_id

    def to_dict(self):
        return {
            'follower_id': self.follower_id,
            'user_id': self.user_id,
            'follower_user_id': self.follower_user_id
        }


class Tag:
    def __init__(self, tag_id, tag_name):
        self.tag_id = tag_id
        self.tag_name = tag_name

    def to_dict(self):
        return {
            'tag_id': self.tag_id,
            'tag_name': self.tag_name
        }


class StoryTag:
    def __init__(self, story_id, tag_id):
        self.story_id = story_id
        self.tag_id = tag_id

    def to_dict(self):
        return {
            'story_id': self.story_id,
            'tag_id': self.tag_id
        }


class StoryReaction:
    def __init__(self, story_id, reaction_id, user_id):
        self.story_id = story_id
        self.reaction_id = reaction_id
        self.user_id = user_id

    def to_dict(self):
        return {
            'story_id': self.story_id,
            'reaction_id': self.reaction_id,
            'user_id': self.user_id
        }


class StoryComment:
    def __init__(self, story_id, comment_id):
        self.story_id = story_id
        self.comment_id = comment_id

    def to_dict(self):
        return {
            'story_id': self.story_id,
            'comment_id': self.comment_id
        }


class Like:
    def __init__(self, like_id, media_id, user_id, created_at):
        self.like_id = like_id
        self.media_id = media_id
        self.user_id = user_id
        self.created_at = created_at

    def to_dict(self):
        return {
            'like_id': self.like_id,
            'media_id': self.media_id,
            'user_id': self.user_id,
            'created_at': self.created_at
        }
