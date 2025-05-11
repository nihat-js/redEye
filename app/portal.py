from flask import Blueprint, render_template, g, request, jsonify, current_app, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import uuid

from app import mongo

portalBlueprint = Blueprint('portalBlueprint', __name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'zip', 'rar', "html",
                      "css"
                      "script", "py", "ps1", ""]


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@portalBlueprint.get("/portal")
@jwt_required()
def portal():
    return render_template("portal/index.html", current_user=g.current_user)


@portalBlueprint.get("/portal/enumeration")
@jwt_required()
def enumerate():
    return render_template("portal/enumeration.html", current_user=g.current_user)


@portalBlueprint.get("/portal/exploitation")
@jwt_required()
def exploit():
    username = get_jwt_identity()
    user = mongo.db.users.find_one({"username": username})
    return render_template("portal/exploitation.html", current_user=g.current_user)


@portalBlueprint.get("/portal/activeDirectory")
@jwt_required()
def ad():
    return render_template("portal/activeDirectory.html", current_user=g.user)


@portalBlueprint.get("/portal/privilegeEscalation")
@jwt_required()
def privilege():
    return render_template("portal/privilegeEscalation.html", current_user=g.current_user)


@portalBlueprint.get("/uploads")
@jwt_required()
def uploads():
    return render_template('portal/uploads.html', current_user=g.current_user)


@portalBlueprint.post("/portal/upload")
@jwt_required()
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    original_filename = secure_filename(file.filename)
    file_ext = original_filename.rsplit('.', 1)[1].lower()
    if not file_ext in ALLOWED_EXTENSIONS:
        return jsonify({'error': 'File type not allowed'}), 400

    try:
        # Generate unique filename
        unique_filename = f"{uuid.uuid4()}.{file_ext}"
        # Save file
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, unique_filename)
        file.save(file_path)

        # Save file info to database
        file_size = os.path.getsize(file_path)
        print(file_size)
        file_record = {
            'original_filename': original_filename,
            'stored_filename': unique_filename,
            'file_type': file_ext,
            'size': file_size,
            'upload_date': datetime.utcnow(),
            'owner_id': str(g.current_user["_id"]),
            'owner_username': g.current_user["username"],
        }
        print(file_record)
        uploadedFile = mongo.db.uploads.insert_one(file_record)

        return jsonify({
            'message': 'File uploaded successfully',
            'file': {
                'id': str(uploadedFile.inserted_id),
                'filename': original_filename,
            }
        }), 200

    except Exception as e:
        current_app.logger.error(f"Upload error: {str(e)}")
        return jsonify({'error': 'Failed to upload file'}), 500


@portalBlueprint.get("/api/files")
@jwt_required()
def list_files():
    try:
        files = list(mongo.db.uploads.find({'owner_id': str(g.current_user["_id"])}))
        for file in files:
            file['_id'] = str(file['_id'])
        return jsonify(files)
    except Exception as e:
        current_app.logger.error(f"List files error: {str(e)}")
        return jsonify({'error': 'Failed to list files'}), 500


@portalBlueprint.delete("/api/files/<file_id>")
@jwt_required()
def delete_file(file_id):
    try:
        # Get file info from database
        file = mongo.db.uploads.find_one({
            'owner_id': g.current_user['id']
        })

        if not file:
            return jsonify({'error': 'File not found'}), 404

        # Delete physical file
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file['stored_filename'])
        if os.path.exists(file_path):
            os.remove(file_path)

        # Delete database record
        mongo.db.uploads.delete_one({'id': file_id})

        return jsonify({'message': 'File deleted successfully'}), 200

    except Exception as e:
        current_app.logger.error(f"Delete file error: {str(e)}")
        return jsonify({'error': 'Failed to delete file'}), 500


@portalBlueprint.get("/files/<filename>")
@jwt_required()
def serve_file(filename):
    try:
        # Verify file ownership
        file = mongo.db.uploads.find_one({
            'stored_filename': filename,
            'owner_id': g.current_user['id']
        })

        if not file:
            return jsonify({'error': 'File not found'}), 404

        return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

    except Exception as e:
        current_app.logger.error(f"Serve file error: {str(e)}")
        return jsonify({'error': 'Failed to serve file'}), 500
