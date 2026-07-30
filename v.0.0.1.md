A Scientific Dependency Graph and perform deterministic cross-artifact verification:

asve/
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── lint.yml
│   │   ├── release.yml
│   │   └── publish.yml
│   │
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODEOWNERS
│   └── dependabot.yml
│
├── docs/
│   ├── architecture.md
│   ├── cli.md
│   ├── api.md
│   ├── plugins.md
│   ├── rules.md
│   ├── examples.md
│   └── verification.md
│
├── examples/
│   ├── paper_project/
│   ├── software_project/
│   ├── broken_project/
│   └── demo_report/
│
├── configs/
│   ├── default.yaml
│   ├── publication.yaml
│   └── minimal.yaml
│
├── schemas/
│   ├── report.schema.json
│   ├── evidence.schema.json
│   ├── graph.schema.json
│   └── findings.schema.json
│
├── tests/
│   ├── test_cli.py
│   ├── test_project.py
│   ├── test_document.py
│   ├── test_dataset.py
│   ├── test_software.py
│   ├── test_graph.py
│   ├── test_report.py
│   └── test_rules.py
│
├── src/
│   └── asve/
│
│       ├── __init__.py
│       ├── __main__.py
│       ├── version.py
│       │
│       ├── cli.py
│       ├── project.py
│       ├── config.py
│       ├── constants.py
│       ├── exceptions.py
│       │
│       ├── discovery/
│       │   ├── __init__.py
│       │   ├── scanner.py
│       │   ├── artifacts.py
│       │   └── resolver.py
│       │
│       ├── parsers/
│       │   ├── __init__.py
│       │   ├── markdown.py
│       │   ├── latex.py
│       │   ├── notebook.py
│       │   ├── python.py
│       │   ├── yaml.py
│       │   ├── json.py
│       │   └── csv.py
│       │
│       ├── graph/
│       │   ├── __init__.py
│       │   ├── builder.py
│       │   ├── nodes.py
│       │   ├── edges.py
│       │   ├── evidence.py
│       │   └── visualize.py
│       │
│       ├── rules/
│       │   ├── __init__.py
│       │   ├── registry.py
│       │   ├── base.py
│       │   ├── document.py
│       │   ├── software.py
│       │   ├── dataset.py
│       │   └── references.py
│       │
│       ├── verification/
│       │   ├── __init__.py
│       │   ├── engine.py
│       │   ├── orchestrator.py
│       │   ├── findings.py
│       │   ├── severity.py
│       │   └── verifier.py
│       │
│       ├── report/
│       │   ├── __init__.py
│       │   ├── report.py
│       │   ├── markdown.py
│       │   ├── json.py
│       │   ├── html.py
│       │   └── summary.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   ├── artifact.py
│       │   ├── project.py
│       │   ├── finding.py
│       │   ├── evidence.py
│       │   ├── report.py
│       │   └── graph.py
│       │
│       ├── plugins/
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   └── base.py
│       │
│       └── utils/
│           ├── files.py
│           ├── hashing.py
│           ├── logging.py
│           ├── paths.py
│           ├── serialization.py
│           └── validation.py
│
├── pyproject.toml
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── CITATION.cff
└── Dockerfile

MVP Scope (v0.0.1)

To keep the first release focused and achievable we provide only six capabilities:

1. Project discovery: Identify manuscripts, source code, datasets, notebooks, and configuration files within a research project.

2. Dependency graph: Build a basic graph linking artifacts such as manuscripts to figures, code, and datasets.

3. Deterministic verification rules: Check for missing files, broken references, duplicate identifiers, and simple consistency issues.

4. Verification engine: Execute rules, collect findings, and classify them by severity.

5. Reporting: Generate Markdown and JSON reports summarizing findings and evidence.

6. Command-line interface: Provide commands such as asve init, asve verify, and asve report.
  
