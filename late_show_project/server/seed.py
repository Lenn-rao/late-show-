from app import app, db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from werkzeug.security import generate_password_hash
from datetime import date

def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Seed users
        user1 = User(username='admin', password_hash=generate_password_hash('password'))
        db.session.add(user1)

        # Seed guests
        guest1 = Guest(name='John Doe', occupation='Actor')
        guest2 = Guest(name='Jane Smith', occupation='Comedian')
        db.session.add_all([guest1, guest2])

        # Seed episodes
        episode1 = Episode(date=date(2025, 6, 1), number=101)
        episode2 = Episode(date=date(2025, 6, 2), number=102)
        db.session.add_all([episode1, episode2])

        # Seed appearances
        appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
        appearance2 = Appearance(rating=5, guest_id=2, episode_id=1)
        db.session.add_all([appearance1, appearance2])

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed()