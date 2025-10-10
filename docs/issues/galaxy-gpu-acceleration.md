# Issue Draft: GPU-Accelerated Tooling for Galaxy Project

- **Repository Target:** galaxyproject/tools-iuc (or relevant tool repo)
- **Labels:** `enhancement`, `performance`, `GPU`, `flagship::bio-llm-eval`, `contrib::galaxy`
- **Milestone:** Galaxy 24.2 cycle (Q4 2025)

## Summary

Several high-usage genomics workflows in Galaxy remain CPU-bound, leading to long queue times. This issue proposes porting the `bwa_mem` alignment tool to leverage GPU acceleration (CUDA) while preserving reproducibility and testability within Galaxy’s tool ecosystem.

## Goals

1. Deliver a GPU-enabled wrapper for `bwa_mem` (using NVIDIA Clara Parabricks or open CUDA kernels).
2. Provide benchmarking data comparing CPU vs. GPU performance on standard datasets.
3. Ensure the tool passes Galaxy’s automated tool tests and integrates with workflow histories.

## Tasks

- [ ] Align with maintainers on preferred GPU runtime (Docker base image vs. Conda package).
- [ ] Draft design doc outlining dependencies, hardware assumptions, and fallbacks.
- [ ] Implement tool wrapper and update `tool_conf.xml`.
- [ ] Add unit/integration tests with small sample dataset.
- [ ] Record benchmarking results (cpu vs gpu) and include in documentation.
- [ ] Update documentation/tutorial notebook demonstrating workflow speedups.
- [ ] Prepare blog post outline co-authored with maintainer (optional but desired).

## Acceptance Criteria

- Tool executes successfully on GPU-enabled runners with documented prerequisites.
- Automated tests pass in CI or designated GPU testing environment.
- Benchmarks show ≥4x speedup vs. CPU baseline on >=10GB test dataset.
- Documentation includes reproducibility notes and compatibility matrix.
- Maintainer review approved and merged before 15 Nov 2025.

## Notes

- Investigate existing GPU work (e.g., [Galaxy training materials](https://training.galaxyproject.org)) to avoid duplication.
- Consider packaging GPU dependencies via Conda-forge (`cudatoolkit`) or containerized approach if simpler.
