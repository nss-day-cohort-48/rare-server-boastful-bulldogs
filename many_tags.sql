Create Table TagsPosts (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `tag_id` INTEGER NOT NULL,
    `post_id` INTEGER NOT NULL,
    FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`),
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

DROP TABLE Posts;

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
INSERT INTO `Tags` VALUES (null, "COPILOT");



INSERT INTO `TagsPosts` VALUES (null, 2, 1);
INSERT INTO `TagsPosts` VALUES (null, 2, 1);
INSERT INTO `TagsPosts` VALUES (null, 1, 2);
INSERT INTO `TagsPosts` VALUES (null, 1, 2);
INSERT INTO `TagsPosts` VALUES (null, 1, 2);
INSERT INTO `TagsPosts` VALUES (null, 2, 1);
INSERT INTO `TagsPosts` VALUES (null, 2, 1);

Select
    t.id,
    t.label
From Tags t
Join TagsPosts tp on t.id = tp.tag_id
Join Posts p on p.id = tp.post_id
where p.id = 1;

SELECT * FROM Tags