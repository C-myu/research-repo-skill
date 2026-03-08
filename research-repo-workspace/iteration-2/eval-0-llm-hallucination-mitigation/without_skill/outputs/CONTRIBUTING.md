# Contributing Guidelines

Thank you for your interest in contributing to the LLM Hallucination Mitigation Research Repository!

## How to Contribute

### Adding New Papers

1. **Place papers in appropriate category**:
   - Detection papers → `/papers/detection/`
   - Alignment/Training papers → `/papers/alignment/`
   - Evaluation papers → `/papers/evaluation/`

2. **Include these files**:
   - PDF of the paper
   - BibTeX citation
   - Short summary (1-2 paragraphs)
   - Key methodology overview

3. **Update README**:
   - Add paper to the relevant category README
   - Include citation information

### Adding Implementations

1. **Place code in appropriate directory**:
   - Detection code → `/code/detection/`
   - Training code → `/code/training/`
   - Evaluation code → `/code/evaluation/`

2. **Follow code style**:
   - Use Python type hints
   - Include docstrings
   - Add unit tests

3. **Document usage**:
   - Add usage examples
   - Include requirements
   - Document expected inputs/outputs

### Adding Experimental Results

1. **Organize experiments**:
   - Create dedicated directory under `/experiments/`
   - Include configuration file (YAML)
   - Save results (JSON format)

2. **Document findings**:
   - Write analysis in experiment README
   - Include visualizations
   - Note any limitations

### Adding Datasets

1. **Place in appropriate directory**:
   - `/data/datasets/` for benchmark datasets
   - `/data/baselines/` for baseline models

2. **Include metadata**:
   - Source and citation
   - Dataset statistics
   - Preprocessing steps
   - License information

## Code Style Guidelines

### Python Style

- Follow PEP 8 guidelines
- Use Black for formatting
- Include type hints
- Write docstrings (Google style preferred)

Example:
```python
def detect_hallucination(text: str, threshold: float = 0.5) -> Dict[str, Any]:
    """
    Detect if text contains hallucinated content.

    Args:
        text: Input text to analyze
        threshold: Confidence threshold for classification

    Returns:
        Dictionary with detection results including:
            - is_hallucination: bool
            - confidence: float
            - details: Dict[str, Any]
    """
    pass
```

### Documentation Style

- Use clear, concise language
- Include examples
- Document edge cases
- Note computational requirements

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_detection.py

# Run with coverage
pytest --cov=code tests/
```

### Writing Tests

- Write unit tests for new functionality
- Include edge cases
- Mock external API calls
- Test with sample data

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add/update documentation
5. Run tests
6. Submit pull request

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] PR description explains changes

## Documentation

### Updating Documentation

- Keep READMEs up to date
- Add examples for new features
- Update installation instructions if needed
- Document any breaking changes

### Adding New Sections

- Use clear headings
- Include table of contents for long pages
- Add links to related sections
- Include diagrams where helpful

## Questions or Issues?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Documentation improvements
- General questions

Thank you for contributing!
