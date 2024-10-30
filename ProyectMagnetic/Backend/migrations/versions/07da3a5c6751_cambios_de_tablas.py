"""Cambios de tablas

Revision ID: 07da3a5c6751
Revises: 
Create Date: 2024-10-13 21:10:00.563399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07da3a5c6751'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persona_rol',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('persona_id', sa.Integer(), nullable=True),
        sa.Column('rol_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['persona_id'], ['personas.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['rol_id'], ['roles.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('historial_accesos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('persona_id', sa.Integer(), nullable=True))  # Cambiado a nullable=True
        batch_op.drop_constraint('historial_accesos_usuario_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'personas', ['persona_id'], ['id'])
        batch_op.drop_column('usuario_id')

    with op.batch_alter_table('permisos_acceso', schema=None) as batch_op:
        batch_op.add_column(sa.Column('persona_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('es_universal', sa.Boolean(), nullable=True))
        batch_op.drop_constraint('permisos_acceso_usuario_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'personas', ['persona_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('permisos_acceso', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('permisos_acceso_usuario_id_fkey', 'usuarios', ['usuario_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('es_universal')
        batch_op.drop_column('persona_id')

    with op.batch_alter_table('historial_accesos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('historial_accesos_usuario_id_fkey', 'usuarios', ['usuario_id'], ['id'])
        batch_op.drop_column('persona_id')

    op.drop_table('persona_rol')
    # ### end Alembic commands ###
