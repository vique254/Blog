"""Second migration

Revision ID: b850589a56af
Revises: bcfc2ecc3fa5
Create Date: 2019-12-04 17:46:58.407691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b850589a56af'
down_revision = 'bcfc2ecc3fa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blog_id', sa.Integer(), nullable=False))
    op.add_column('comments', sa.Column('comment', sa.String(length=255), nullable=True))
    op.drop_constraint('comments_blog_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blogs', ['blog_id'], ['id'])
    op.drop_column('comments', 'username')
    op.drop_column('comments', 'blog')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blog', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('comments', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_blog_fkey', 'comments', 'blogs', ['blog'], ['id'])
    op.drop_column('comments', 'comment')
    op.drop_column('comments', 'blog_id')
    # ### end Alembic commands ###