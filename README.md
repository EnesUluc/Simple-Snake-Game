# 🐍 Simple Snake Game - Python + Docker

A simple graphical **Snake Game** developed in Python using `tkinter`. This project is containerized with Docker and can be run on any platform. Windows users can use `VcXsrv (XLaunch)` to display the GUI.

---

## ⚙️ Requirements

### 1. Install Required Tools

- Python (for development)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [VcXsrv](https://sourceforge.net/projects/vcxsrv/) (for X11 GUI support on Windows)

---

## ▶️ VcXsrv Configuration (X11 Display Server - for Windows)

1. Launch the `XLaunch` (VcXsrv) application.
2. Follow these steps in the wizard:
   - ✅ **Multiple Windows**
   - ✅ **Start no client**
   - ✅ **Disable access control** (this is important!)
3. Click "Finish" and ensure it's running in the background (you should see its icon in the system tray).

---

## 🐳 Build Docker Image

In your terminal or PowerShell, navigate to the project folder (e.g. `src/`) and run:

```bash
cd src
docker build -t simple-snake-game .
```

 Run the Application (Windows PowerShell)
   1-Make sure VcXsrv (XLaunch) is running
   2-Set the DISPLAY envireonment variable and start the container:
   ```bash
    $env:DISPLAY="host.docker.internal:0.0"
    docker run --rm -e DISPLAY=host.docker.internal:0.0 simple-snake-game
   ```

