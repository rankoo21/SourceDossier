# Steward remediation record

This commit records the post-review verification for SourceDossier.

- The contract independently fetches both HTTPS sources inside nondeterministic execution.
- Source slots must use distinct hostnames, and exact response-body SHA-256 digests are stored with each finding.
- Validators compare the complete structured result, including both digests and both evidence codes, so changed bytes or disagreement fail closed.
- The executable contract suite covers clean URL rules, duplicate normalized IDs, malformed model output, changed source bytes, and validator disagreement.
- The deployed contract and public application are recorded in `artifacts/deployment.json` and `artifacts/hosting-verification.json`.

Verification command:

```text
python -m pytest tests/test_contract.py -q
```
