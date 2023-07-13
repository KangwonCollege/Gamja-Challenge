from enum import Enum


class Scope(Enum):
    repo = "repo"
    repo_status = "repo:status"

    repo_deployment = "repo_deployment"
    public_repo = "public_repo"
    repo_invite = "repo:invite"

    security_events = "security_events"

    admin_repo_hook = "admin:repo_hook"
    write_repo_hook = "write:repo_hook"
    read_repo_hook = "read:repo_hook"

    admin_organization = "admin:org"
    write_organization = "write:org"
    read_organization = "read:org"

    admin_public_key = "admin:public_key"
    write_public_key = "write:public_key"
    read_public_key = "read:public_key"

    admin_organization_hook = "admin:org_hook"
    gist = "gist"
    notifications = "notifications"

    user = "user"
    read_user = "read:user"
    user_email = "user:email"
    user_follow = "user:follow"

    project = "project"
    read_project = "read:project"
    delete_repo = "delete_repo"

    write_packages = "write:packages"
    read_packages = "read:packages"
    delete_packages = "delete:packages"

    admin_gpg_key = "admin:gpg_key"
    write_gpg_key = "write:gpg_key"
    read_gpg_key = "read:gpg_key"

    codespace = "codespace"
    workflow = "workflow"
