from pdm.cli.actions import resolve_candidates_from_lockfile
from pdm.core import Core
from pdm.pep517 import api


def get_requires_for_build_wheel(config_settings=None):
    project = Core().create_project(".")
    dependencies = project.get_dependencies("build")
    resolved = resolve_candidates_from_lockfile(project, dependencies.values())

    reqs = []
    for candidate in resolved.values():
        reqs.append(candidate.req.as_pinned_version(candidate.version).as_line())
    return reqs


get_requires_for_build_sdist = get_requires_for_build_wheel
get_requires_for_build_editable = get_requires_for_build_wheel


def __getattr__(name):
    return getattr(api, name)
