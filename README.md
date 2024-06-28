# Rov backend

## Start Development

To start the pigpio Daemon. Only run once after reboot.
```bash
sudo pigpiod
```

Enter python virtual environment. Install the dependencies. Start the FastAPI Server in Development mode (automatic hot reload).
```bash
source .venv/bin/activate
python install -r requirements.txt
fastapi dev main.py
```

Maybe VS Code enters the virtual environment automatically. So you only have to start the pigpio Daemon and fastapi.
