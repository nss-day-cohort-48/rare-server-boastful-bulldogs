DROP TABLE Posts;

CREATE TABLE "Users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "first_name" varchar,
    "last_name" varchar,
    "email" varchar,
    "bio" varchar,
    "username" varchar,
    "password" varchar,
    "profile_image_url" varchar,
    "created_on" date,
    "active" bit
);
CREATE TABLE "DemotionQueue" (
    "action" varchar,
    "admin_id" INTEGER,
    "approver_one_id" INTEGER,
    FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
    PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE "Subscriptions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "follower_id" INTEGER,
    "author_id" INTEGER,
    "created_on" date,
    FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Posts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER,
    "category_id" INTEGER,
    "title" varchar,
    "publication_date" date,
    "image_url" varchar,
    "content" varchar,
    "approved" bit,
    FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
    FOREIGN KEY(`category_id`) REFERENCES `Categories`(`id`)
);
CREATE TABLE "Comments" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "post_id" INTEGER,
    "author_id" INTEGER,
    "content" varchar,
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
    FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Reactions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar,
    "image_url" varchar
);
CREATE TABLE "PostReactions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER,
    "reaction_id" INTEGER,
    "post_id" INTEGER,
    FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE "Tags" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar
);
CREATE TABLE "PostTags" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "post_id" INTEGER,
    "tag_id" INTEGER,
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar
);
INSERT INTO Categories ('label')
VALUES ('News');
INSERT INTO Tags ('label')
VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url')
VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Users
VALUES (
        null,
        "Steve",
        "Brownie",
        "steve@nss.com",
        "Head Sorcerer @ NSS",
        "steve",
        "steve",
        "https://i.pravatar.cc/150?u=steve",
        1627318439512,
        1
    );
SELECT *
FROM Users;

INSERT INTO Users
VALUES (
        null,
        "Josh",
        "Brownie",
        "josh@nss.com",
        "Assistant",
        "josh",
        "josh",
        "https://i.pravatar.cc/150?u=steve",
        1627318439091,
        0
    );

INSERT INTO Posts
VALUES (
    null,
    1,
    1,
    "Fires raging in the PNW",
    1627408353185,
    "https://static01.nyt.com/images/2017/09/10/us/10XP-oregon1_xp/06oregon1_xp-jumbo.jpg?quality=90&auto=webp",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    1
);
INSERT INTO Posts
VALUES (
    null,
    1,
    1,
    "Olympians are winning Gold!",
    1627412440128,
    "https://epmgaa.media.clients.ellingtoncms.com/img/photos/2020/04/09/simonebiles_t580.jpg?8f1b5874916776826eb17d7e67de7278c987ca33",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    1
);

SELECT * FROM Posts
