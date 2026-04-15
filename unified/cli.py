import click
import sys
from pathlib import Path
from unified.config import Config
from unified.shell import UnifiedShell

@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Unified Platform: sovereign models + developer tools + IDE"""
    pass

@cli.command()
def keygen():
    """Generate a new sovereign key (pookie keygen wrapper)"""
    import subprocess
    print("Running pookie keygen...")
    result = subprocess.run(["pookie", "keygen"], capture_output=False)
    sys.exit(result.returncode)

@cli.command()
@click.option("--env", default=".env", help="Path to .env file")
def shell(env):
    """Start interactive shell"""
    try:
        config = Config.from_env(env_file=env if Path(env).exists() else None)
        shell_instance = UnifiedShell(config)
        shell_instance.run()
    except ValueError as e:
        click.echo(f"❌ {e}", err=True)
        click.echo("\nTo set up:", err=True)
        click.echo("  1. Run: unified-cli keygen", err=True)
        click.echo("  2. Set: export POOKIE_KEY=pk-...", err=True)
        click.echo("  3. Run: unified-cli shell", err=True)
        sys.exit(1)

@cli.command()
@click.argument("command", nargs=-1)
def run(command):
    """Run shell command via unified platform"""
    if not command:
        click.echo("Usage: unified-cli run <command>", err=True)
        sys.exit(1)

    try:
        config = Config.from_env()
        shell_instance = UnifiedShell(config)
        result = shell_instance.toollama_client.bash_execute(" ".join(command))

        if result.get("success"):
            click.echo(result.get("stdout", ""))
        else:
            click.echo(f"Error: {result.get('error')}", err=True)
            sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

def main():
    """Main entry point"""
    try:
        cli()
    except KeyboardInterrupt:
        print("\n\nInterrupted")
        sys.exit(130)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
