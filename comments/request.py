from models import Comment, Post, User
import sqlite3
import json

# SQL CREATE COMMENT
def create_comment(new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content, created_on )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_comment['post_id'], new_comment['author_id'],
                new_comment['content'], new_comment['created_on']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid
        # Add the `id` property to the post dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id

    return json.dumps(new_comment)


# SQL GET COMMENTS BY POST ID
def get_comments_by_post_id(id):
    """Return a list of comments by post Id"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on,
            p.title post_title,
            p.category_id post_category,
            u.first_name user_first_name,
            u.last_name user_last_name
        FROM Comments c
        JOIN Posts p
            ON p.id = c.post_id
        JOIN Users u
            ON u.id = c.author_id
        WHERE c.post_id = ?
        """, ( id, ))

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = Comment(row['id'], row['post_id'], row['author_id'],
                    row['content'], row['created_on'])

            post = Post(row['post_id'], row['post_title'], row['post_category'])
            user = User(row['author_id'], row['user_first_name'], row['user_last_name'])

            comment.post = post.__dict__
            comment.user = user.__dict__

            comments.append(comment.__dict__)
    
    return json.dumps(comments)