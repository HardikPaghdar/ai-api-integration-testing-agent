# AI API Integration Testing Agent

An OpenAPI analysis prototype that inventories documented operations, flags missing documentation, and creates a starter test plan for happy paths and write-operation validation.

## Included
- Reads a local OpenAPI JSON document.
- Lists HTTP operations with path, operation ID, parameters, and documentation status.
- Flags undocumented responses and missing summaries.
- Produces a structured starter test plan without sending network requests.
- Includes a sample API spec and unit tests.

## Run
Requires Python 3.10+.

```bash
python - <<'PY'
import json
from app import analyze_openapi, load_spec
result = analyze_openapi(load_spec("examples/openapi.json"))
print(json.dumps(result, indent=2))
PY
```

## Tests
`python -m unittest discover -s tests -v`

## Limitations and next steps
This demo does not call the API under test, resolve every OpenAPI reference, validate every schema, or generate executable tests. Review the plan and add a separately configured test runner with explicit base URLs, authentication from environment variables, timeouts, test-data cleanup, and an allowlist so generated tests cannot hit unintended systems.

## Explore more

- [AI Automated QA Test Generator](https://github.com/HardikPaghdar/ai-automated-qa-test-generator) — requirements-based test plans.
- [AI Website Audit Agent](https://github.com/HardikPaghdar/ai-website-audit-agent) — rule-based HTML audit.
- [AI Agent Evaluation Platform](https://github.com/HardikPaghdar/ai-agent-evaluation-platform) — agent run evaluation.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
