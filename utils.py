from importlib import import_module as imm

from os import getenv


def render_template_file(file_name: str, **kwargs: dict):
    """
    Higher level api for rendering templates.
    """
    from config.stage import settings

    return settings.render_template.get_template(file_name).render(**kwargs)


def import_module(path):
    return imm(path)


def import_class(path):

    if isinstance(path, str):

        value, class_name = path.rsplit(".", 1)
        module = import_module(value)

        return getattr(module, class_name)

    else:

        return path


def env_str(env_name: str, default: str) -> str:

    return getenv(env_name, default)


def env_int(env_name: str, default: int) -> int:

    return int(getenv(env_name, default))


def env_float(env_name: str, default: float) -> float:

    return float(getenv(env_name, default))


def env_bool(env_name: str, default: bool) -> bool:

    return bool(getenv(env_name, default))