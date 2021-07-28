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
    """Return posts by User Id"""
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
        WHERE u.id = ?
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