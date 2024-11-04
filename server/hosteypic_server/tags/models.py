import sqlalchemy as alch
import sqlalchemy.orm as orm

from hosteypic_server.database import Base

tags_posts = alch.Table(
    'tags_posts', Base.metadata,
    alch.Column('post_id', alch.Integer, alch.ForeignKey('posts.id', ondelete='CASCADE')),
    alch.Column('tag_id', alch.Integer, alch.ForeignKey('tags.id', ondelete='CASCADE'))
)

class Tag(Base):
    __tablename__ = 'tags'
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(alch.String(50))
