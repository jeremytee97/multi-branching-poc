# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Feel free to remove any parts that are uneeded to keep the changelog concise.

<!--- changelog for features or fixes can be written here according to convention above - this will be compiled into a release section through CI/CD when publishing a release --->
## Unreleased
### Added
- Update workflow ([#99](https://github.com/MoneyLion/de-python-util/pull/99))

## [2.0.0] - 2023-11-17
### Added
- Setup documentation workflow and published guides. Documentation is now viewable on http://dpu.moneylion.com ([#99](https://github.com/MoneyLion/de-python-util/pull/99))
- Update codeowners to `data-engineering-maintainers` ([#104](https://github.com/MoneyLion/de-python-util/pull/104))
- Capped pydantic to v1, snowflake connector to 3.0.3 and boto3 to 1.27.1 for older python versions to temporarily bypass deprecation warnings ([#104](https://github.com/MoneyLion/de-python-util/pull/104))
- Disable mypy checks temporarily until dpu is updated ([#104](https://github.com/MoneyLion/de-python-util/pull/104))
- Added comments to update DPU to be compatible with newer package versions ([#104](https://github.com/MoneyLion/de-python-util/pull/104))
- Added query tag to snowflake connection session parameters ([#105](https://github.com/MoneyLion/de-python-util/pull/105))

## [1.6.0] - 2023-01-04
### Added
- CI/CD workflow for releasing to Github with approval phase ([#86](https://github.com/MoneyLion/de-python-util/pull/86))
  
  This addition also turns on [protected tags](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-tag-protection-rules) for the repo to prevent accidental deletion of tags. Read [RELEASE.md](https://github.com/MoneyLion/de-python-util/blob/master/RELEASE.md) for more details.
- Drop support for Python 3.6 due to reaching End of Life ([#88](https://github.com/MoneyLion/de-python-util/pull/88))
- Upgrade base development & pre-commit python version to be 3.9 ([#88](https://github.com/MoneyLion/de-python-util/pull/88))
  
  Dependencies are updated to the latest version available in early **January 2022**. This update also no longer caps the dependencies with an upper limit as how open-source projects does to allow a more friendly developer experience when installing `dpu` with other packages (by minimizing dependencies conflict)
- Added unit tests for utilities functions ([#87](https://github.com/MoneyLion/de-python-util/pull/87))
- Added unit tests for database services ([#84](https://github.com/MoneyLion/de-python-util/pull/84))

<!--- Tag links placeholder --->
[1.6.0]: https://github.com/MoneyLion/de-python-util/releases/tag/1.6.0
[2.0.0]: https://github.com/jeremytee97/multi-branching-poc/releases/tag/2.0.0
