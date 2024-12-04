-- Створення бази даних
DROP DATABASE IF EXISTS lab4;
CREATE DATABASE IF NOT EXISTS lab4;
USE lab4;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Stories (
    story_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE TABLE Media (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    story_id INT,
    media_type ENUM('photo', 'video') NOT NULL,
    media_url VARCHAR(255) NOT NULL,
    FOREIGN KEY (story_id) REFERENCES Stories(story_id) ON DELETE CASCADE
);

CREATE TABLE Reactions (
    reaction_id INT AUTO_INCREMENT PRIMARY KEY,
    reaction_type ENUM('like', 'love', 'laugh', 'sad', 'angry') NOT NULL
);

CREATE TABLE Comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    story_id INT,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (story_id) REFERENCES Stories(story_id) ON DELETE CASCADE
);

CREATE TABLE Followers (
    follower_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    follower_user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (follower_user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE TABLE Tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    tag_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE StoryTags (
    story_id INT,
    tag_id INT,
    PRIMARY KEY (story_id, tag_id),
    FOREIGN KEY (story_id) REFERENCES Stories(story_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES Tags(tag_id) ON DELETE CASCADE
);

CREATE TABLE StoryReactions (
    story_id INT,
    reaction_id INT,
    user_id INT,
    PRIMARY KEY (story_id, reaction_id, user_id),
    FOREIGN KEY (story_id) REFERENCES Stories(story_id) ON DELETE CASCADE,
    FOREIGN KEY (reaction_id) REFERENCES Reactions(reaction_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE TABLE StoryComments (
    story_id INT,
    comment_id INT,
    PRIMARY KEY (story_id, comment_id),
    FOREIGN KEY (story_id) REFERENCES Stories(story_id) ON DELETE CASCADE,
    FOREIGN KEY (comment_id) REFERENCES Comments(comment_id) ON DELETE CASCADE
);

CREATE TABLE Likes (
    like_id INT AUTO_INCREMENT PRIMARY KEY,
    media_id INT,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (media_id) REFERENCES Media(media_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Додавання користувачів
INSERT INTO Users (username, password, email) VALUES
('alice', 'password1', 'alice@example.com'),
('bob', 'password2', 'bob@example.com'),
('charlie', 'password3', 'charlie@example.com'),
('david', 'password4', 'david@example.com'),
('eve', 'password5', 'eve@example.com');

-- Додавання історій
INSERT INTO Stories (user_id) VALUES
(1), (2), (3), (4), (5);

-- Додавання медіа
INSERT INTO Media (story_id, media_type, media_url) VALUES
(1, 'photo', 'http://example.com/photo1.jpg'),
(2, 'video', 'http://example.com/video1.mp4'),
(3, 'photo', 'http://example.com/photo2.jpg'),
(4, 'video', 'http://example.com/video2.mp4'),
(5, 'photo', 'http://example.com/photo3.jpg');

-- Додавання реакцій
INSERT INTO Reactions (reaction_type) VALUES
('like'), ('love'), ('laugh'), ('sad'), ('angry');

-- Додавання коментарів
INSERT INTO Comments (user_id, story_id, comment_text) VALUES
(1, 2, 'Це чудово!'),
(2, 3, 'Цікавий пост!'),
(3, 4, 'Супер!'),
(4, 5, 'Дуже смішно!'),
(5, 1, 'Мені подобається!');

-- Додавання підписників
INSERT INTO Followers (user_id, follower_user_id) VALUES
(1, 2), (2, 3), (3, 4), (4, 5), (5, 1);

-- Додавання тегів
INSERT INTO Tags (tag_name) VALUES
('funny'), ('travel'), ('food'), ('nature'), ('music');

-- Додавання тегів до історій
INSERT INTO StoryTags (story_id, tag_id) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5);

-- Додавання реакцій до історій
INSERT INTO StoryReactions (story_id, reaction_id, user_id) VALUES
(1, 1, 2), (2, 2, 3), (3, 3, 4), (4, 4, 5), (5, 5, 1);

-- Додавання коментарів до історій
INSERT INTO StoryComments (story_id, comment_id) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5);

-- Додавання лайків до медіа
INSERT INTO Likes (media_id, user_id) VALUES
(1, 2), (2, 3), (3, 4), (4, 5), (5, 1);
