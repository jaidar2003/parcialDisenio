from flask import Blueprint, request, jsonify
from services.mutant_service import MutantService

mutant_bp = Blueprint('mutant', __name__)
mutant_service = MutantService()

@mutant_bp.route('/mutant/', methods=['POST'])
def detect_mutant():
    data = request.get_json()
    dna = data.get("dna")
    if not dna:
        return jsonify({"error": "DNA sequence is required"}), 400

    is_mutant = mutant_service.is_mutant(dna)
    saved = mutant_service.save_dna(dna, is_mutant=is_mutant)

    if not saved:
        return jsonify({"message": "DNA sequence already exists"}), 409  # 409 Conflict

    if is_mutant:
        return jsonify({"message": "Mutant detected"}), 200
    else:
        return jsonify({"message": "Not a mutant"}), 403
    
@mutant_bp.route('/stats', methods=['GET'])
def get_stats():
    stats = mutant_service.get_stats()
    return jsonify(stats)

