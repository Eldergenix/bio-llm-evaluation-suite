# Issue Draft: MAIA Helm Chart & Compliance Enhancements

- **Repository Target:** maia-platform/maia (deployment or ops repo)
- **Labels:** `deployment`, `helm`, `compliance`, `contrib::maia`
- **Milestone:** MAIA Q4 2025 infrastructure sprint

## Summary

Hospitals evaluating MAIA need an opinionated deployment path that aligns with HIPAA requirements. This issue proposes adding production-ready Helm charts and compliance documentation to streamline installations on managed Kubernetes (EKS/GKE/AKS).

## Goals

1. Provide Helm charts with configurable profiles (dev, staging, prod) covering core MAIA services.
2. Integrate security controls: TLS, network policies, secrets management, audit logging.
3. Document HIPAA-aligned deployment checklist and reference architectures.

## Tasks

- [ ] Inventory existing deployment scripts/manifests; identify gaps for Helm packaging.
- [ ] Define chart structure (`charts/maia`, `charts/maia-deps`) with values files for common clusters.
- [ ] Implement templates for:
  - Application services (API, frontend, worker agents)
  - Database/storage dependencies
  - Ingress with TLS and auth integration
- [ ] Add NetworkPolicy and PodSecurity admission settings.
- [ ] Wire secrets via external secret providers (e.g., AWS Secrets Manager).
- [ ] Provide sample CI workflow for chart linting and security scans.
- [ ] Write deployment guide covering:
  - HIPAA considerations (audit logs, PHI isolation)
  - Backup/restore procedures
  - Clinician feedback loop integration
- [ ] Validate on an EKS test cluster; document results and screenshots.

## Acceptance Criteria

- Helm charts deploy successfully on EKS/GKE with minimal manual edits.
- Security controls (TLS, NetworkPolicy, secrets) enabled by default.
- Documentation includes HIPAA alignment checklist and troubleshooting tips.
- CI checks (lint + template render) pass; maintainers approve review before 05 Dec 2025.

## Notes

- Coordinate with maintainers on preferred chart repository structure.
- Consider optionally publishing to ArtifactHub for visibility once stable.
