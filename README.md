# OpenStarbound Server Manager
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/assasin34/OpenStarbound-Server-Manager)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/github/license/assasin34/OpenStarbound-Server-Manager)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)

A graphical server manager for OpenStarbound, built with Python and PySide6. This tool provides an easy-to-use interface for managing your OpenStarbound dedicated server, monitoring its performance, and viewing connected players.

## Contents

* [Features](#features)
* [Getting Started](#getting-started)
* [Configuration](#configuration)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Acknowledgements](#acknowledgements)
* [License](#license)

## Features

* **Server Control:** Easily Start, Stop, and Restart your OpenStarbound server with dedicated buttons.
* **Live Console:** View the raw server console output in real-time.
* **Player Monitoring:** See a list of currently connected players and a live player count.
* **Resource Tracking:** Monitor CPU and RAM usage for both the server process and your total system.
* **Server Status:** Get at-a-glance information on the server's status (Offline, Starting, Online, etc.), uptime, and public IP address.
* **Ngrok Integration:** Optional, one-click `ngrok` support to easily open your server to the public internet without manual port forwarding.
* **Configuration UI:** A simple settings dialog to configure paths to your server and `ngrok` executables.
* **Server Config Editor:** Edit your `starbound_server.config` directly from the application.

## Getting Started

### Prerequisites

* Windows
* A local copy of the OpenStarbound dedicated server

### Installation

#### Option 1: Download the latest release (Recommended)

1. Download the latest release from the **Releases** page.
2. Run `OpenStarbound-Server-Manager.exe`.
3. Configure your server paths in **Settings** before starting the server.

#### Option 2: Run from source

Clone the repository:

```sh
git clone https://github.com/assasin34/OpenStarbound-Server-Manager.git
cd OpenStarbound-Server-Manager
```

Install the required packages:

```sh
pip install -r requirements.txt
```

Run the application:

```sh
python main.py
```

## Configuration

The first time you run the application, it will create a `settings.json` file with default values.

Open the application and click the **Settings** button in the top-right corner.

You must provide the correct paths for:

* **Server Executable:** The full path to your `starbound_server.exe`.
* **Server Executable Folder:** The directory where the server executable is located.

Optionally, if you want to use `ngrok`:

* Enable **Use Ngrok**.
* Provide the paths to `ngrok.exe` and its containing folder.

Click **Save** to apply your changes.

Alternatively, you can manually edit the `settings.json` file:

```json
{
    "server_executable": "C:/path/to/your/starbound_server.exe",
    "server_directory": "C:/path/to/your/server_folder",
    "ngrok_executable": "C:/path/to/your/ngrok.exe",
    "ngrok_directory": "C:/path/to/your/ngrok_folder",
    "storage_path": "...",
    "assets_path": "...",
    "use_ngrok": true
}
```

## Usage

1. Launch OpenStarbound Server Manager.
2. Open **Settings** and configure your server paths.
3. (Optional) Enable and configure `ngrok`.
4. Click **Start** to launch the server.
5. Monitor the server through the console, player list, status information, and resource usage panels.
6. Use **Stop** or **Restart** to manage the server at any time.

### Interface Overview

* **Server Controls:** Use the **Start**, **Stop**, and **Restart** buttons to manage the server.
* **Players and Console:** The main window displays the list of connected players on the left and the live server console on the right.
* **Server Info:** Displays the server's status, uptime, public IP address (or `ngrok` URL), and current player count.
* **Resource Usage:** Displays real-time CPU and RAM usage for both the server and your system.

## Roadmap

### Completed

* [x] Server management
* [x] Live console
* [x] Player monitoring
* [x] Resource monitoring
* [x] Ngrok integration
* [x] Server Config Editor

### Planned

* [ ] Crash Handling
* [ ] Automatic backups
* [ ] Plugin/Mod manager
* [ ] Player Location Tracking
* [ ] Implement native Dark Mode support
* [ ] Refresh user interface for a more modern look
* [ ] Multiple server profiles

## Acknowledgements

* [OpenStarbound](https://github.com/OpenStarbound/OpenStarbound) – The open-source reimplementation and enhancement of the Starbound engine.
* [Starbound Server GUI (PenGUIn)](https://community.playstarbound.com/threads/penguin-starbound-server-gui.118075/) – Inspiration for the overall concept and several server management features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
