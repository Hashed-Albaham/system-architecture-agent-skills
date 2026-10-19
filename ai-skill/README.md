
## Automated checks

The repository's GitHub Actions workflow `.github/workflows/validate-skills.yml` runs on pushes to `main`, pull requests, and manual dispatch. It compiles the validator and checks skill frontmatter, package links, required specialist count, and all 28 chapter entries. It requires no project dependency installation. The workflow verifies package structure, not whether a particular architecture is correct or secure.
