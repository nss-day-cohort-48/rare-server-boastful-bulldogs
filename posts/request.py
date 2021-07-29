from models import Post, User, Category
import sqlite3
import json

# SQL GET function for posts
def get_all_posts():
    """Return all posts"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.first_name user_first_name,
            u.last_name user_last_name,
            c.label category_label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'],
                    row['title'], row['publication_date'], row['image_url'],
                    row['content'], row['approved'])

            user = User(row['user_id'], row['user_first_name'], row['user_last_name'])
            category = Category(row['category_id'], row['category_label'])

            post.user = user.__dict__
            post.category = category.__dict__

            posts.append(post.__dict__)

    return json.dumps(posts)


# SQL GET post by ID
def get_single_post(id):
    """Return a single post by Id"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.first_name user_first_name,
            u.last_name user_last_name,
            c.label category_label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post = Post(data['id'], data['user_id'], data['category_id'],
                data['title'], data['publication_date'], data['image_url'],
                data['content'], data['approved'])

        user = User(data['user_id'], data['user_first_name'], data['user_last_name'])
        category = Category(data['category_id'], data['category_label'])

        post.user = user.__dict__
        post.category = category.__dict__

        return json.dumps(post.__dict__)


# SQL GET post by User Id
def get_posts_by_user_id(id):
    """Return a list of posts by User Id"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id user_id,
            u.first_name user_first_name,
            u.last_name user_last_name,
            c.label category_label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.user_id = ?
        """, ( id, ))

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(row['id'], row['user_id'], row['category_id'],
                    row['title'], row['publication_date'], row['image_url'],
                    row['content'], row['approved'])

            user = User(row['user_id'], row['user_first_name'], row['user_last_name'])
            category = Category(row['category_id'], row['category_label'])

            post.user = user.__dict__
            post.category = category.__dict__

            posts.append(post.__dict__)

    return json.dumps(posts)

#SQL CREATE POST
def create_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id, title, publication_date, image_url, content, approved )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['category_id'],
              new_post['title'], new_post['publication_date'],
              new_post['image_url'], new_post['content'], new_post['approved'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the post dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_post['id'] = id


    return json.dumps(new_post)