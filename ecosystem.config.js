module.exports = {
  apps: [
    {
      name: "madaniy-hayot-backend",
      script: "venv/bin/gunicorn",
      args: [
        "--workers", "3",
        "--bind", "127.0.0.1:8003",
        "config.wsgi:application"
      ],
      cwd: "./",
      interpreter: "python3",
      env: {
        DEBUG: "False",
        PYTHONPATH: "."
      },
      autorestart: true,
      watch: false,
      max_memory_restart: "1G"
    }
  ]
};
