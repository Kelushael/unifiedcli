# Contributing

Contributions welcome! This is a unified platform combining three awesome projects:
- **pookie** — Sovereign model distribution
- **TOOLLAMA** — Developer tools via MCP
- **YahushuaCLI** — Interactive IDE

## Areas to Improve

- [ ] Additional TOOLLAMA tool integrations
- [ ] Web UI for memory management
- [ ] Performance optimizations
- [ ] Better error messages and logging
- [ ] Integration with official MCP servers
- [ ] Process management tools
- [ ] Environment variable tools

## Development Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/awesome-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run tests: `pytest tests/ -v`
6. Commit: `git commit -m "feat: add awesome feature"`
7. Push and create a pull request

## Code Style

- PEP 8
- Type hints preferred for public functions
- Docstrings for all public functions and classes

## Testing

```bash
# Install test dependencies
pip install pytest pytest-mock

# Run tests
pytest tests/ -v

# Run with coverage
pytest --cov=unified tests/
```

## Building Documentation

Documentation is in README.md and inline docstrings. Keep it clear and practical.

## Questions?

Open an issue or discussion. This is a community project!
