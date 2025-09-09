# Sprite CLI 🚀

A lightweight Python CLI tool for serving static websites locally with ease. Perfect for quickly testing your HTML, CSS, and JavaScript files in a local development environment.

## Features

- 🚀 **Quick Setup**: Start a local web server with a single command
- 📁 **Smart Detection**: Automatically detects if your directory contains static website files
- 🌐 **Cross-Platform**: Works on Windows, macOS, and Linux
- ⚡ **Fast & Lightweight**: Built with Python's built-in HTTP server
- 🎨 **CORS Support**: Includes CORS headers for local API testing
- 🔧 **Flexible Configuration**: Customizable host and port settings

## Installation

### From PyPI (Recommended)

```bash
pip install sprite-cli
```

### From Source

```bash
git clone https://github.com/regularguythatcodes/sprite.git
cd sprite
pip install -e .
```

## Usage

### Basic Usage

Navigate to your static website directory and run:

```bash
cd /path/to/your/website
sprite serve
```

This will start a local web server at `http://localhost:8000`.

### Custom Port and Host

```bash
sprite serve --port 3000 --host 0.0.0.0
```

### Open Browser Automatically

```bash
sprite serve --open
```

### Check Directory

Verify if your current directory is suitable for serving:

```bash
sprite check
```

## Commands

### `sprite serve`

Start a local web server to serve static files from the current directory.

**Options:**
- `--port, -p`: Port to serve on (default: 8000)
- `--host, -h`: Host to bind to (default: localhost) 
- `--open, -o`: Open browser automatically

**Examples:**
```bash
# Basic usage
sprite serve

# Custom port
sprite serve --port 3000

# Bind to all interfaces
sprite serve --host 0.0.0.0

# Open browser automatically
sprite serve --open

# Combine options
sprite serve --port 3000 --host 0.0.0.0 --open
```

### `sprite check`

Check if the current directory contains static website files and show a summary.

```bash
sprite check
```

### `sprite version`

Show the current version of Sprite CLI.

```bash
sprite version
```

## Requirements

- Python 3.7 or higher
- Your static website files (HTML, CSS, JS) in the current directory

## Directory Structure

Sprite works best when run in a directory containing your static website files:

```
my-website/
├── index.html
├── style.css
├── script.js
├── assets/
│   ├── images/
│   └── fonts/
└── pages/
    └── about.html
```

## Features in Detail

### Smart Directory Detection

Sprite automatically checks if your current directory contains static website files before starting the server. It looks for:

- HTML files (`.html`, `.htm`)
- CSS files (`.css`)
- JavaScript files (`.js`)

### CORS Support

The built-in server includes CORS headers, making it easy to test APIs and cross-origin requests during local development.

### Graceful Shutdown

Press `Ctrl+C` to gracefully shutdown the server.

### Error Handling

- Port availability checking
- Directory validation
- Clear error messages and suggestions

## Common Use Cases

### Frontend Development

Perfect for testing static HTML, CSS, and JavaScript projects:

```bash
cd my-frontend-project
sprite serve --open
```

### Static Site Generators

Great for previewing generated static sites:

```bash
cd dist  # or build, public, etc.
sprite serve
```

### Quick File Sharing

Share files over your local network:

```bash
sprite serve --host 0.0.0.0 --port 8080
```

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, try a different port:

```bash
sprite serve --port 3000
```

### Permission Denied

On some systems, you may need elevated privileges for ports below 1024:

```bash
sudo sprite serve --port 80
```

### No HTML Files Found

Make sure you're in the correct directory containing your website files:

```bash
sprite check  # Verify your directory
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### Version 1.0.0
- Initial release
- Basic static file serving
- CLI interface with click
- Directory validation
- CORS support
- Custom host and port configuration
- Browser auto-open option
