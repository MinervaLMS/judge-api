"""Ping __init__ module."""

from app.ping.views import ping

from app.ping.judge_endpoint.endpoint import judge_endpoint_bp


__all__ = ["ping", "judge_endpoint_bp"]
