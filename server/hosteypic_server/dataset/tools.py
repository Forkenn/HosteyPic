import os
import io
import csv
import random
import string

from textwrap import shorten

from fastapi import UploadFile
from fastapi_users.password import PasswordHelper
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from hosteypic_server.users.models import User
from hosteypic_server.posts.models import Post
from hosteypic_server.likes.models import Like

class DatasetManager:
    @classmethod
    async def load_csv(cls, input_csv: UploadFile, session: AsyncSession):
        reader = csv.DictReader(io.TextIOWrapper(input_csv.file, encoding="utf-8"), delimiter=';')
        data = [row for row in reader]

        users, users_output = await cls.__load_users(data, session)
        await cls.__load_posts(data, users, session)

        return users_output

    @staticmethod
    async def __load_users(data: list, session: AsyncSession):
        users: dict = {}
        users_output: list = [['id', 'username', 'email', 'password']]
        password_helper = PasswordHelper()
        for row in data:
            if len(users) == 200:
                break

            username = row["username"]
            if username in users:
                continue

            password = ''.join(
                random.SystemRandom().choice(
                    string.ascii_lowercase + string.ascii_uppercase + string.digits
                ) for _ in range(10)
            )
            hashed_password = password_helper.hash(password=password)
            email = 'test-' + ''.join(
                random.SystemRandom().choice(
                    string.ascii_lowercase + string.ascii_uppercase + string.digits
                ) for _ in range(6)
            ) + '@hosteypic.test'

            insert_link = '... Source: ' + row['user_link']
            user_about = row['user_about']
            if len(user_about) > 140 - len(insert_link):
                about_me = shorten(
                    user_about,
                    width=140 - len(insert_link),
                    break_long_words=False,
                    break_on_hyphens=False,
                    placeholder=""
                ) + insert_link

            else:
                about_me = user_about + insert_link

            avatar = row["user_avatar"]

            if not os.path.isfile('uploads/avatars/original/' + avatar):
                avatar = 'default.jpg'

            user = User(
                avatar=avatar,
                username=username,
                about_me=about_me,
                hashed_password=hashed_password,
                email=email
            )
            session.add(user)
            await session.flush()
            users[username] = user.id
            users_output.append([user.id, username, email, password])

        await session.commit()
        return (users, users_output)

    @staticmethod
    async def __load_posts(data: list, users: dict, session: AsyncSession):
        for row in data:
            post = Post(
                attachment=row["image"],
                title=row["image_title"],
                body=row["image_body"],
                user_id=random.choice(list(users.values())),
            )
            session.add(post)
        await session.commit()

    @classmethod
    async def add_likes(cls, session: AsyncSession):
        users = (await session.execute(select(User))).scalars().all()
        posts = (await session.execute(select(Post))).scalars().all()

        for user in users:
            liked_posts = set()
            while len(liked_posts) < 300:
                post = random.choice(posts)
                if post.id in liked_posts:
                    continue

                like = Like(user_id=user.id, post_id=post.id)
                session.add(like)
                liked_posts.add(post.id)

        print('Likes created')
        await session.commit()

    @classmethod
    async def add_followers(cls, session: AsyncSession):
        users = (await session.execute(select(User))).scalars().all()
        users_count = len(users)

        for user in users:
            followers_count = random.randint(100, users_count)

            for followee in users[:followers_count]:
                await user.follow(followee)

            print(f'Created follows for user with id: {user.id}')

        await session.commit()
