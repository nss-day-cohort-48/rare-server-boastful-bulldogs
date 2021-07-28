from models import Post, User, Category
import sqlite3
import json

def get_posts_by_category_id(id): 
    """return posts by category id"""
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
        WHERE p.category_id = ?
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