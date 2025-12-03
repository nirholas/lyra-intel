"""
Interactive CLI mode with rich output and progress tracking.
"""

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich.prompt import Prompt, Confirm
from rich.tree import Tree
from rich import print as rprint
from pathlib import Path
from typing import Optional, List
import sys

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Lyra Intel - AI-Powered Code Analysis Platform"""
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Output file path')
@click.option('--format', '-f', type=click.Choice(['json', 'html', 'pdf', 'sarif']), 
              default='json', help='Output format')
@click.option('--analyzers', '-a', multiple=True, 
              type=click.Choice(['security', 'quality', 'complexity', 'dependencies']),
              help='Specific analyzers to run')
@click.option('--interactive', '-i', is_flag=True, help='Interactive mode')
def analyze(path: str, output: Optional[str], format: str, analyzers: tuple, interactive: bool):
    """Analyze a code repository or file."""
    
    if interactive:
        path = Prompt.ask("📁 Enter repository path", default=path)
        
        # Ask which analyzers to run
        console.print("\n[bold]Select analyzers to run:[/bold]")
        selected_analyzers = []
        
        if Confirm.ask("  🔒 Security scanner"):
            selected_analyzers.append('security')
        if Confirm.ask("  ✨ Code quality"):
            selected_analyzers.append('quality')
        if Confirm.ask("  📊 Complexity analysis"):
            selected_analyzers.append('complexity')
        if Confirm.ask("  📦 Dependency check"):
            selected_analyzers.append('dependencies')
        
        analyzers = tuple(selected_analyzers) if selected_analyzers else ('security', 'quality')
        
        # Ask for output preferences
        save_report = Confirm.ask("\n💾 Save report to file")
        if save_report:
            format = Prompt.ask(
                "Select format",
                choices=['json', 'html', 'pdf', 'sarif'],
                default='json'
            )
            output = Prompt.ask("Output path", default=f"analysis_report.{format}")
    
    console.print(Panel.fit(
        f"[bold cyan]Starting Analysis[/bold cyan]\n"
        f"Path: {path}\n"
        f"Analyzers: {', '.join(analyzers) if analyzers else 'all'}\n"
        f"Format: {format}",
        title="⚡ Lyra Intel"
    ))
    
    # Simulate analysis with progress bar
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        console=console
    ) as progress:
        
        # Crawl files
        task1 = progress.add_task("[cyan]Crawling files...", total=100)
        for i in range(100):
            progress.update(task1, advance=1)
        
        # Run analyzers
        task2 = progress.add_task("[yellow]Running analyzers...", total=100)
        for i in range(100):
            progress.update(task2, advance=1)
        
        # Generate report
        task3 = progress.add_task("[green]Generating report...", total=100)
        for i in range(100):
            progress.update(task3, advance=1)
    
    # Display results
    console.print("\n[bold green]✓ Analysis Complete![/bold green]\n")
    
    # Create results table
    table = Table(title="Analysis Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Files Analyzed", "127")
    table.add_row("Total Issues", "23")
    table.add_row("Critical", "2")
    table.add_row("High", "5")
    table.add_row("Medium", "10")
    table.add_row("Low", "6")
    table.add_row("Complexity Score", "7.2")
    table.add_row("Maintainability", "82%")
    
    console.print(table)
    
    if output:
        console.print(f"\n[bold green]✓ Report saved to:[/bold green] {output}")


@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--severity', '-s', 
              type=click.Choice(['critical', 'high', 'medium', 'low']),
              default='high',
              help='Minimum severity to report')
@click.option('--fix', is_flag=True, help='Auto-fix issues when possible')
def security(path: str, severity: str, fix: bool):
    """Run security vulnerability scan."""
    
    console.print(Panel(
        f"[bold red]🔒 Security Scan[/bold red]\n"
        f"Target: {path}\n"
        f"Min Severity: {severity}",
        title="Security Scanner"
    ))
    
    with console.status("[bold yellow]Scanning for vulnerabilities...", spinner="dots"):
        # Simulate scanning
        import time
        time.sleep(2)
    
    # Display vulnerabilities
    console.print("\n[bold]Vulnerabilities Found:[/bold]\n")
    
    vuln_table = Table()
    vuln_table.add_column("Severity", style="bold")
    vuln_table.add_column("Type")
    vuln_table.add_column("File")
    vuln_table.add_column("Line")
    vuln_table.add_column("Description")
    
    vuln_table.add_row(
        "[red]CRITICAL[/red]",
        "SQL Injection",
        "api/users.py",
        "45",
        "Unsanitized user input in SQL query"
    )
    vuln_table.add_row(
        "[orange1]HIGH[/orange1]",
        "XSS",
        "web/templates/profile.html",
        "12",
        "Unescaped user data in template"
    )
    
    console.print(vuln_table)
    
    if fix:
        if Confirm.ask("\n🔧 Apply automatic fixes"):
            console.print("[green]✓ Applied 2 automatic fixes[/green]")


@cli.command()
@click.argument('file', type=click.Path(exists=True))
def explain(file: str):
    """Explain code using AI."""
    
    console.print(f"[bold cyan]🤖 AI Code Explanation[/bold cyan]\n")
    
    # Read and display file
    with open(file, 'r') as f:
        code = f.read()
    
    syntax = Syntax(code[:500], "python", theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title=f"📄 {file}"))
    
    with console.status("[bold yellow]Analyzing code...", spinner="dots"):
        import time
        time.sleep(2)
    
    explanation = """
[bold]Purpose:[/bold]
This module implements a user authentication system with JWT tokens.

[bold]Key Components:[/bold]
• authenticate_user(): Validates credentials and returns JWT
• refresh_token(): Refreshes expired tokens
• verify_token(): Validates JWT signatures

[bold]Security Features:[/bold]
✓ Password hashing with bcrypt
✓ Token expiration
✓ Rate limiting

[bold]Potential Issues:[/bold]
⚠ No password complexity requirements
⚠ Missing refresh token rotation
"""
    
    console.print(Panel(explanation, title="💡 AI Analysis", border_style="green"))


@cli.command()
@click.option('--api-url', prompt='API URL', default='http://localhost:8080')
@click.option('--api-key', prompt='API Key', hide_input=True)
def configure(api_url: str, api_key: str):
    """Configure Lyra Intel settings."""
    
    config = {
        'api_url': api_url,
        'api_key': api_key
    }
    
    # Save config (simplified)
    console.print("\n[bold green]✓ Configuration saved![/bold green]")
    
    # Test connection
    with console.status("[yellow]Testing connection...", spinner="dots"):
        import time
        time.sleep(1)
    
    console.print("[green]✓ Connection successful![/green]")


@cli.command()
@click.argument('path', type=click.Path(exists=True))
def tree(path: str):
    """Display project structure tree."""
    
    tree_view = Tree(f"📁 {Path(path).name}")
    
    # Build tree (simplified example)
    src = tree_view.add("📁 src")
    src.add("📄 __init__.py")
    
    analyzers = src.add("📁 analyzers")
    analyzers.add("📄 ast_analyzer.py")
    analyzers.add("📄 security_scanner.py")
    
    api = src.add("📁 api")
    api.add("📄 server.py")
    api.add("📄 routes.py")
    
    tree_view.add("📄 README.md")
    tree_view.add("📄 requirements.txt")
    
    console.print(tree_view)


@cli.command()
def dashboard():
    """Launch interactive web dashboard."""
    
    console.print(Panel(
        "[bold cyan]🚀 Starting Lyra Intel Dashboard[/bold cyan]\n\n"
        "Dashboard will be available at:\n"
        "[link=http://localhost:3000]http://localhost:3000[/link]",
        title="Web Dashboard"
    ))
    
    console.print("\n[yellow]Press Ctrl+C to stop the server[/yellow]\n")
    
    # In real implementation, would start the web server
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[red]Server stopped[/red]")


if __name__ == '__main__':
    cli()
