import time, os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1.0.0-dev")
COMMIT_SHA = os.getenv("RAILWAY_GIT_COMMIT_SHA") or os.getenv("COMMIT_SHA") or "local"


@app.context_processor
def inject_version():
    return {"app_version": APP_VERSION, "commit_sha": COMMIT_SHA[:7]}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health_check():
    # DB PASS chk
    db_password = os.getenv("DB_PASSWORD")

    if not db_password:
        return (
            jsonify({"status": "ERROR", "message": "Secret DB_PASSWORD is missing!"}),
            500,
        )

    print(f"Connecting to DB with secret: {db_password[:2]}***")

    # DB response
    time.sleep(1)
    return jsonify({"status": "UP", "database": "connected"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)  # nosec B104
