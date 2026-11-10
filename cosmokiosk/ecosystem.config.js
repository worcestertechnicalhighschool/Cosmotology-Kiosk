module.exports = {
    apps: [
        {
            name: "Cosmetology-Kiosk",
            script: "../.venv/bin/gunicorn",
            args: "cosmokiosk.wsgi:application --workers 17 --bind 0.0.0.0:8080",
            interpreter: "none",
            env: {
                PYTHONUNBUFFERED: "1",
                DJANGO_PRODUCTION: "True",
            }
        }
    ]
}
