"""Build the flat list of instances to probe from the ConfigMap JSON."""


def build_instances(instances_config, env_list):
    """
    Walk the ConfigMap and return a flat list of dicts:
        [{"business_line": ..., "env": ..., "url": ..., "version": ...}, ...]
    Filtered on env_list.
    """
    instances = []
    for business_line, envs in instances_config.items():
        for env, json_instances in envs.items():
            if env not in env_list:
                continue
            for ji in json_instances:
                app_code = ji.get("APP_CODE", "APXXXXXX")
                release_uid = ji.get("RELEASE_UUID", "e9e9e9e9")
                instances.append({
                    "business_line": business_line,
                    "env": env,
                    "url": f"astronomer-{app_code}-{env}-{release_uid}",
                    "version": ji.get("VERSION", "x.y.z"),
                })
    return instances
