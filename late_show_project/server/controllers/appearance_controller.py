from flask import Blueprint, request, jsonify
from models import db
from models.appearance import Appearance
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data.get('rating'),
            guest_id=data.get('guest_id'),
            episode_id=data.get('episode_id')
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Invalid data'}), 400