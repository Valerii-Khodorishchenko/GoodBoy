from datetime import datetime, timezone

from goodboy import db


MAX_LENGTH_NAME = 128


class BaseMixin:
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime,
        default=lambda:datetime.now(timezone.utc)
    )


class Activity(BaseMixin, db.Model):
    name = db.Column(db.String(MAX_LENGTH_NAME), nullable=False, unique=True)
    description = db.Column(db.Text)
    action_types = db.relationship(
        'ActionType',
        back_populates='activity',
        cascade='all, delete-orphan'
    )
    rewards = db.relationship(
        'Reward',
        back_populates='activity',
        cascade='all, delete-orphan'
    )


class ActionType(BaseMixin, db.Model):
    activity_id = db.Column(
        db.Integer,
        db.ForeignKey('activity.id'),
        nullable=False
    )
    name = db.Column(db.String(MAX_LENGTH_NAME), nullable=False)
    unit = db.Column(db.String(MAX_LENGTH_NAME))
    coefficient = db.Column(db.Float, nullable=False)
    activity = db.relationship('Activity', back_populates='action_types')
    entries = db.relationship(
        'ActionEntry',
        back_populates='action_type',
        cascade='all, delete-orphan'
    )


class ActionEntry(BaseMixin, db.Model):
    action_type_id = db.Column(
        db.Integer,
        db.ForeignKey('action_type.id'),
        nullable=False
    )
    action_type = db.relationship('ActionType', back_populates='entries')


class Reward(BaseMixin, db.Model):
    activity_id = db.Column(
        db.Integer,
        db.ForeignKey('activity.id'),
        nullable=False
    )
    name = db.Column(db.String(MAX_LENGTH_NAME), nullable=False)
    description = db.Column(db.Text)
    cost = db.Column(db.Integer, nullable=False)
    is_claimed = db.Column(db.Boolean, default=False)
    activity = db.relationship('Activity', back_populates='rewards')
