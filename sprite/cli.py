#!/usr/bin/env python3
"""
Sprite CLI - Command line interface for serving static websites.
"""

import os
import sys
import signal
import socket
from pathlib import Path
import click
from .server import StaticServer


def is_static_website_directory():
    """Check if current directory contains static website files."""
    current_dir = Path.cwd()
    
    # Check for common static website files
    html_files = list(current_dir.glob("*.html"))
    css_files = list(current_dir.glob("*.css")) or list(current_dir.glob("**/*.css"))
    js_files = list(current_dir.glob("*.js")) or list(current_dir.glob("**/*.js"))
    
    # At minimum, we should have HTML files
    return len(html_files) > 0


def is_port_available(port):
    """Check if a port is available for use."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('localhost', port))
        sock.close()
        return True
    except OSError:
        return False


@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option(version="1.0.0", prog_name="sprite")
def cli(ctx):
    """
    Sprite - A simple CLI tool for serving static websites locally.
    
    Run 'sprite serve' to start a local web server in the current directory.
    """
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@cli.command()
@click.option('--port', '-p', default=8000, type=int, help='Port to serve on (default: 8000)')
@click.option('--host', '-h', default='localhost', help='Host to bind to (default: localhost)')
@click.option('--open', '-o', is_flag=True, help='Open browser automatically')
def serve(port, host, open):
    """Start a local web server to serve static files from the current directory."""
    
    # Validate that we're in a directory with static website files
    if not is_static_website_directory():
        click.echo(
            click.style("❌ Error: ", fg="red") + 
            "No HTML files found in current directory.\n" +
            "Please run 'sprite serve' in a directory containing your static website files (HTML, CSS, JS).",
            err=True
        )
        sys.exit(1)
    
    # Check if port is available
    if not is_port_available(port):
        click.echo(
            click.style("❌ Error: ", fg="red") + 
            f"Port {port} is already in use. Try a different port with --port option.",
            err=True
        )
        sys.exit(1)
    
    # Start the server
    try:
        server = StaticServer(host, port, Path.cwd())
        
        click.echo(click.style("🚀 Sprite server starting...", fg="green"))
        click.echo(f"📁 Serving files from: {Path.cwd()}")
        click.echo(f"🌐 Server running at: {click.style(f'http://{host}:{port}', fg='blue', underline=True)}")
        click.echo(f"⏹️  Press {click.style('Ctrl+C', fg='yellow')} to stop the server")
        
        # Open browser if requested
        if open:
            import webbrowser
            webbrowser.open(f'http://{host}:{port}')
        
        # Handle graceful shutdown
        def signal_handler(signum, frame):
            click.echo(f"\n{click.style('🛑 Shutting down server...', fg='yellow')}")
            server.stop()
            click.echo(click.style("✅ Server stopped successfully!", fg="green"))
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        # Start serving
        server.serve_forever()
        
    except Exception as e:
        click.echo(
            click.style("❌ Error starting server: ", fg="red") + str(e),
            err=True
        )
        sys.exit(1)


@cli.command()
def check():
    """Check if the current directory is suitable for serving static files."""
    current_dir = Path.cwd()
    
    click.echo(f"📁 Checking directory: {current_dir}")
    
    # Check for HTML files
    html_files = list(current_dir.glob("*.html"))
    css_files = list(current_dir.glob("*.css")) + list(current_dir.glob("**/*.css"))
    js_files = list(current_dir.glob("*.js")) + list(current_dir.glob("**/*.js"))
    
    click.echo(f"📄 HTML files found: {len(html_files)}")
    click.echo(f"🎨 CSS files found: {len(css_files)}")
    click.echo(f"⚡ JavaScript files found: {len(js_files)}")
    
    if html_files:
        click.echo(click.style("✅ This directory looks good for serving!", fg="green"))
        
        # Show index file if it exists
        index_files = [f for f in html_files if f.name.lower() in ['index.html', 'index.htm']]
        if index_files:
            click.echo(f"🏠 Index file found: {index_files[0].name}")
        else:
            click.echo("ℹ️  No index.html found. Server will show directory listing.")
    else:
        click.echo(click.style("❌ No HTML files found in this directory.", fg="red"))
        click.echo("Please ensure you're in a directory with your static website files.")


@cli.command()
def version():
    """Show the version of Sprite."""
    from . import __version__
    click.echo(f"Sprite CLI version {__version__}")


if __name__ == '__main__':
    cli()