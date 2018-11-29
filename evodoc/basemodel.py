from flask_sqlalchemy import Model, BaseQuery
import sqlalchemy as sa
import datetime
from sqlalchemy.ext.declarative import declared_attr
from evodoc.exception.dbException import DbException

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


class IdModel(Model):
    @declared_attr
    def id(self):
        for base in self.__mro__[1:-1]:
            if getattr(base, '__table__', None) is not None:
                type = sa.ForeignKey(base.id)
                break
        else:
            type = sa.Integer

        return sa.Column(type, primary_key=True)

    @classmethod
    def getById(cls, id):
        entity = cls.query.filter_by(id=id).first()
        return entity

# class declaring softdelete params (model mixin)


class SoftDelete(object):
    delete = sa.Column(sa.DateTime, nullable=True)


class CreateUpdate(object):
    create = sa.Column(sa.DateTime, default=datetime.datetime.utcnow())
    update = sa.Column(sa.DateTime, default=datetime.datetime.utcnow())


class GetOrQuery(BaseQuery):
    def get_or(self, ident, default=None):
        return self.get(ident) or default

    def get_all(self):
        return self.filter_by(delete=None)

    def getWithFlag(self, ident, RiseFlag=True):
        tmp = self.get(ident)
        if tmp is None and RiseFlag:
            raise DbException(400, "id")
        return tmp

    def getByName(self, name, RiseFlag=True):
        tmp = self.filter_by(name=name).first()
        if tmp is None and RiseFlag:
            raise DbException(404, "Name not found.")
        return tmp

    def getByEmail(self, email, RiseFlag=True):
        tmp = self.filter_by(email=email).first()
        if tmp is None and RiseFlag:
            raise DbException(400, "email")
        return tmp

    def getByNameOrEmail(self, nameOrEmail, RiseFlag=True):
        if '@' in nameOrEmail:
            return self.filter_by(email=nameOrEmail).first()
        else:
            return self.filter_by(name=nameOrEmail).first()
        raise DbException(400, "nameOrEmail")
        return None
