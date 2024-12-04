from .models import *

from flask import current_app

class UserDAO:
    @staticmethod
    def get_all_users_with_stories():
        try:
            cursor = current_app.mysql.connection.cursor()
            query = """
                SELECT Users.username, Stories.story_id
                FROM Users
                LEFT JOIN Stories ON Users.user_id = Stories.user_id
                ORDER BY Users.username;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            data = [{"username": row[0], "story_id": row[1]} for row in results]
        except Exception as e:
            print(f"Error fetching users with stories: {e}")
            data = []
        finally:
            cursor.close()
        return data

    @staticmethod
    def get_all_users():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Users")
            users = [User(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching users: {e}")
            users = []
        finally:
            cursor.close()
        return users

    @staticmethod
    def get_user_by_id(user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE user_id = %s", (user_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching user by id: {e}")
            row = None
        finally:
            cursor.close()
        return User(*row).to_dict() if row else None

    @staticmethod
    def add_user(username, password, email):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)",
                           (username, password, email))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_user(user_id, username, password, email):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE Users SET username = %s, password = %s, email = %s WHERE user_id = %s",
                           (username, password, email, user_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def delete_user(user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()


class StoryDAO:
    @staticmethod
    def get_all_stories_with_tags():
        try:
            cursor = current_app.mysql.connection.cursor()
            query = """
                SELECT Stories.story_id, Tags.tag_name
                FROM Stories
                JOIN StoryTags ON Stories.story_id = StoryTags.story_id
                JOIN Tags ON StoryTags.tag_id = Tags.tag_id
                ORDER BY Stories.story_id;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            data = [{"story_id": row[0], "tag_name": row[1]} for row in results]
        except Exception as e:
            print(f"Error fetching stories with tags: {e}")
            data = []
        finally:
            cursor.close()
        return data

    @staticmethod
    def get_all_stories():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Stories")
            stories = [Story(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching stories: {e}")
            stories = []
        finally:
            cursor.close()
        return stories

    @staticmethod
    def get_story_by_id(story_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Stories WHERE story_id = %s", (story_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching story by id: {e}")
            row = None
        finally:
            cursor.close()
        return Story(*row).to_dict() if row else None

    @staticmethod
    def add_story(user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO Stories (user_id) VALUES (%s)", (user_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding story: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_story(story_id, user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE Stories SET user_id = %s WHERE story_id = %s", (user_id, story_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating story: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor

    @staticmethod
    def delete_story(story_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM Stories WHERE story_id = %s", (story_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting story: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

class MediaDAO:
    @staticmethod
    def get_all_media():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Media")
            media = [Media(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching media: {e}")
            media = []
        finally:
            cursor.close()
        return media

    @staticmethod
    def get_media_by_id(media_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Media WHERE media_id = %s", (media_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching media by id: {e}")
            row = None
        finally:
            cursor.close()
        return Media(*row).to_dict() if row else None

    @staticmethod
    def add_media(story_id, media_type, media_url):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO Media (story_id, media_type, media_url) VALUES (%s, %s, %s)",
                           (story_id, media_type, media_url))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding media: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_media(media_id, story_id, media_type, media_url):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE Media SET story_id = %s, media_type = %s, media_url = %s WHERE media_id = %s",
                           (story_id, media_type, media_url, media_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating media: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def delete_media(media_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM Media WHERE media_id = %s", (media_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting media: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()