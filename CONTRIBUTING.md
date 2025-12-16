# Contributing to Keplers.email Examples

Thank you for your interest in contributing to the Keplers.email Python examples!

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest improvements
- Provide clear reproduction steps
- Include your Python version and OS
- Share error messages and logs (with credentials removed)

### Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use consistent indentation (4 spaces)
- Follow existing code patterns
- Add docstrings for complex functions
- Keep functions focused and small

### Testing Your Changes

Before submitting:

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Test with placeholder credentials**:
   ```bash
   cp .env.example .env
   ```

4. **Verify code runs**:
   ```bash
   python main.py
   ```

5. **Check for errors**:
   - Syntax errors
   - Linting issues (use `flake8` or `pylint`)
   - Runtime errors

### Security Requirements

**CRITICAL**: Before committing:

- ✅ Never commit `.env` files with real credentials
- ✅ Use placeholder values in `.env.example`
- ✅ Use `os.getenv()` for all configuration
- ✅ Review changes with `git diff`
- ✅ Verify `.gitignore` is working

### Documentation

- Update README files if behavior changes
- Add docstrings for complex logic
- Include examples for new features
- Update environment variable tables

### Commit Messages

Use clear, descriptive commit messages:

```
Add email template example with attachments

- Implement template variable substitution
- Add attachment handling
- Update README with new example
```

### What We're Looking For

**Welcomed Contributions**:
- Bug fixes
- Documentation improvements
- Additional email examples
- Error handling improvements
- New API endpoint examples
- Performance optimizations
- Type hints and annotations

**Please Avoid**:
- Breaking changes without discussion
- Unrelated feature additions
- Reformatting existing code
- Changes to dependencies without justification

## Questions?

Feel free to open an issue for questions about:
- How to implement a feature
- Whether a contribution would be accepted
- Technical decisions in the codebase

## License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers this project.
