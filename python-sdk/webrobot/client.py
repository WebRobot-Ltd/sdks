"""WebRobot Python SDK — https://api.webrobot.eu (138 paths, OpenAPI 3.0)."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode, quote

import urllib.request
import urllib.error


class WebRobotClient:
    """Client for the WebRobot API.

    Usage::

        from webrobot.client import WebRobotClient

        client = WebRobotClient(api_key="your-api-key")
        projects = client.projects_list()

    Auth supports ``api_key`` (X-API-Key header) or ``jwt`` (Bearer token).
    """

    def __init__(
        self,
        base_url: str = "https://api.webrobot.eu",
        api_key: Optional[str] = None,
        jwt: Optional[str] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._jwt = jwt

    # ── internal helpers ──────────────────────────────────────────────────────

    def _headers(self) -> Dict[str, str]:
        h = {"Content-Type": "application/json", "Accept": "application/json"}
        if self._api_key:
            h["X-API-Key"] = self._api_key
        elif self._jwt:
            h["Authorization"] = f"Bearer {self._jwt}"
        return h

    def _url(self, path: str, params: Optional[Dict[str, Any]] = None) -> str:
        url = self.base_url + path
        if params:
            filtered = {k: v for k, v in params.items() if v is not None}
            if filtered:
                url += "?" + urlencode(filtered)
        return url

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Any] = None,
    ) -> Any:
        url = self._url(path, params)
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, headers=self._headers(), method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            raw = e.read()
            try:
                raise WebRobotError(e.code, json.loads(raw)) from e
            except (ValueError, AttributeError):
                raise WebRobotError(e.code, raw.decode(errors="replace")) from e

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", path, params=params)

    def _post(self, path: str, body: Any = None, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("POST", path, params=params, body=body)

    def _put(self, path: str, body: Any = None) -> Any:
        return self._request("PUT", path, body=body)

    def _delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("DELETE", path, params=params)

    @staticmethod
    def _enc(s: str) -> str:
        return quote(str(s), safe="")

    # ── Health ────────────────────────────────────────────────────────────────

    def health(self) -> Any:
        """GET /health"""
        return self._get("/health")

    # ── Projects ──────────────────────────────────────────────────────────────

    def projects_list(self) -> Any:
        """GET /webrobot/api/projects"""
        return self._get("/webrobot/api/projects")

    def project_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/projects"""
        return self._post("/webrobot/api/projects", body)

    def project_get(self, project_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}")

    def project_update(self, project_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/projects/id/{projectId}"""
        return self._put(f"/webrobot/api/projects/id/{self._enc(project_id)}", body)

    def project_delete(self, project_id: str) -> Any:
        """DELETE /webrobot/api/projects/id/{projectId}"""
        return self._delete(f"/webrobot/api/projects/id/{self._enc(project_id)}")

    def project_get_by_name(self, project_name: str) -> Any:
        """GET /webrobot/api/projects/{projectName}"""
        return self._get(f"/webrobot/api/projects/{self._enc(project_name)}")

    def project_get_metrics(self, project_id: str, start_time: Optional[str] = None, end_time: Optional[str] = None) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/metrics"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/metrics",
                         {"startTime": start_time, "endTime": end_time})

    def project_get_schedule(self, project_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/schedule"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/schedule")

    def project_set_schedule(self, project_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/projects/id/{projectId}/schedule"""
        return self._put(f"/webrobot/api/projects/id/{self._enc(project_id)}/schedule", body)

    # ── Jobs ──────────────────────────────────────────────────────────────────

    def jobs_list(self, project_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs")

    def job_create(self, project_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/projects/id/{projectId}/jobs"""
        return self._post(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs", body)

    def job_get(self, project_id: str, job_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}")

    def job_update(self, project_id: str, job_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/projects/id/{projectId}/jobs/{jobId}"""
        return self._put(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}", body)

    def job_delete(self, project_id: str, job_id: str) -> Any:
        """DELETE /webrobot/api/projects/id/{projectId}/jobs/{jobId}"""
        return self._delete(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}")

    def job_execute(self, project_id: str, job_id: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """POST /webrobot/api/projects/id/{projectId}/jobs/{jobId}/execute"""
        return self._post(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/execute", body or {})

    def job_stop(self, project_id: str, job_id: str) -> Any:
        """POST /webrobot/api/projects/id/{projectId}/jobs/{jobId}/stop"""
        return self._post(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/stop")

    def job_get_logs(self, project_id: str, job_id: str, task_id: Optional[str] = None,
                     pod_type: Optional[str] = None, executor_index: Optional[int] = None,
                     pod_name: Optional[str] = None, tail: Optional[int] = None) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}/logs"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/logs",
                         {"taskId": task_id, "podType": pod_type, "executorIndex": executor_index,
                          "podName": pod_name, "tail": tail})

    def job_get_metrics(self, project_id: str, job_id: str, start_time: Optional[str] = None, end_time: Optional[str] = None) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}/metrics"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/metrics",
                         {"startTime": start_time, "endTime": end_time})

    def job_completion_webhook(self, project_id: str, job_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/projects/id/{projectId}/jobs/{jobId}/completion"""
        return self._post(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/completion", body)

    # ── Tasks ─────────────────────────────────────────────────────────────────

    def tasks_list(self, project_id: str, job_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks")

    def task_create(self, project_id: str, job_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks"""
        return self._post(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks", body)

    def task_get(self, project_id: str, job_id: str, task_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks/{self._enc(task_id)}")

    def task_update(self, project_id: str, job_id: str, task_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}"""
        return self._put(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks/{self._enc(task_id)}", body)

    def task_delete(self, project_id: str, job_id: str, task_id: str) -> Any:
        """DELETE /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}"""
        return self._delete(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks/{self._enc(task_id)}")

    def task_start(self, project_id: str, job_id: str, task_id: str) -> Any:
        """POST /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/start"""
        return self._post(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks/{self._enc(task_id)}/start")

    def task_stop(self, project_id: str, job_id: str, task_id: str) -> Any:
        """POST /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/stop"""
        return self._post(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks/{self._enc(task_id)}/stop")

    def task_get_status(self, project_id: str, job_id: str, task_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/status"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks/{self._enc(task_id)}/status")

    def task_get_metrics(self, project_id: str, job_id: str, task_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/metrics"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/tasks/{self._enc(task_id)}/metrics")

    # ── Executions ────────────────────────────────────────────────────────────

    def execution_get_status(self, project_id: str, job_id: str, execution_id: str) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}/status"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/executions/{self._enc(execution_id)}/status")

    def execution_get_logs(self, project_id: str, job_id: str, execution_id: str,
                           pod_type: Optional[str] = None, executor_index: Optional[int] = None,
                           pod_name: Optional[str] = None, tail: Optional[int] = None) -> Any:
        """GET /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}/logs"""
        return self._get(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/executions/{self._enc(execution_id)}/logs",
                         {"podType": pod_type, "executorIndex": executor_index, "podName": pod_name, "tail": tail})

    def execution_cancel(self, project_id: str, job_id: str, execution_id: str) -> Any:
        """DELETE /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}"""
        return self._delete(f"/webrobot/api/projects/id/{self._enc(project_id)}/jobs/{self._enc(job_id)}/executions/{self._enc(execution_id)}")

    # ── Categories ────────────────────────────────────────────────────────────

    def categories_list(self) -> Any:
        """GET /webrobot/api/categories"""
        return self._get("/webrobot/api/categories")

    def category_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/categories"""
        return self._post("/webrobot/api/categories", body)

    def category_get(self, category_id: str) -> Any:
        """GET /webrobot/api/categories/id/{categoryId}"""
        return self._get(f"/webrobot/api/categories/id/{self._enc(category_id)}")

    def category_update(self, category_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/categories/id/{categoryId}"""
        return self._put(f"/webrobot/api/categories/id/{self._enc(category_id)}", body)

    def category_delete(self, category_id: str) -> Any:
        """DELETE /webrobot/api/categories/id/{categoryId}"""
        return self._delete(f"/webrobot/api/categories/id/{self._enc(category_id)}")

    def category_get_by_name(self, category_name: str) -> Any:
        """GET /webrobot/api/categories/{categoryName}"""
        return self._get(f"/webrobot/api/categories/{self._enc(category_name)}")

    # ── Agents ────────────────────────────────────────────────────────────────

    def agents_list(self, category_id: str) -> Any:
        """GET /webrobot/api/agents/{categoryId}"""
        return self._get(f"/webrobot/api/agents/{self._enc(category_id)}")

    def agent_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/agents"""
        return self._post("/webrobot/api/agents", body)

    def agent_get(self, category_id: str, agent_id: str) -> Any:
        """GET /webrobot/api/agents/{categoryId}/{agentId}"""
        return self._get(f"/webrobot/api/agents/{self._enc(category_id)}/{self._enc(agent_id)}")

    def agent_update(self, category_id: str, agent_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/agents/{categoryId}/{agentId}"""
        return self._put(f"/webrobot/api/agents/{self._enc(category_id)}/{self._enc(agent_id)}", body)

    def agent_delete(self, agent_id: str) -> Any:
        """DELETE /webrobot/api/agents/{agentId}"""
        return self._delete(f"/webrobot/api/agents/{self._enc(agent_id)}")

    def agent_get_by_name(self, category_id: str, agent_name: str) -> Any:
        """GET /webrobot/api/agents/{categoryId}/name/{agentName}"""
        return self._get(f"/webrobot/api/agents/{self._enc(category_id)}/name/{self._enc(agent_name)}")

    def agent_copy(self, agent_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/agents/{agentId}/copy"""
        return self._post(f"/webrobot/api/agents/{self._enc(agent_id)}/copy", body)

    # ── Datasets (v2) ─────────────────────────────────────────────────────────

    def datasets_list(self, type: Optional[str] = None, indexed: Optional[bool] = None, format: Optional[str] = None) -> Any:
        """GET /webrobot/api/datasets"""
        return self._get("/webrobot/api/datasets", {"type": type, "indexed": indexed, "format": format})

    def dataset_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/datasets"""
        return self._post("/webrobot/api/datasets", body)

    def dataset_get(self, dataset_id: str) -> Any:
        """GET /webrobot/api/datasets/{datasetId}"""
        return self._get(f"/webrobot/api/datasets/{self._enc(dataset_id)}")

    def dataset_update(self, dataset_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/datasets/{datasetId}"""
        return self._put(f"/webrobot/api/datasets/{self._enc(dataset_id)}", body)

    def dataset_delete(self, dataset_id: str) -> Any:
        """DELETE /webrobot/api/datasets/{datasetId}"""
        return self._delete(f"/webrobot/api/datasets/{self._enc(dataset_id)}")

    def dataset_get_fields(self, dataset_id: str) -> Any:
        """GET /webrobot/api/datasets/{datasetId}/fields"""
        return self._get(f"/webrobot/api/datasets/{self._enc(dataset_id)}/fields")

    def dataset_index(self, dataset_id: str) -> Any:
        """POST /webrobot/api/datasets/{datasetId}/index"""
        return self._post(f"/webrobot/api/datasets/{self._enc(dataset_id)}/index")

    def dataset_upload_file(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/datasets/upload"""
        return self._post("/webrobot/api/datasets/upload", body)

    def dataset_query(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/datasets/query"""
        return self._post("/webrobot/api/datasets/query", body)

    def dataset_query_by_task(self, task_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/datasets/query/task/{taskId}"""
        return self._post(f"/webrobot/api/datasets/query/task/{self._enc(task_id)}", body)

    def dataset_get_info_by_task(self, task_id: str) -> Any:
        """GET /webrobot/api/datasets/query/task/{taskId}/info"""
        return self._get(f"/webrobot/api/datasets/query/task/{self._enc(task_id)}/info")

    def dataset_get_task_by_output(self, dataset_id: str) -> Any:
        """GET /webrobot/api/datasets/query/by-dataset/{datasetId}/task"""
        return self._get(f"/webrobot/api/datasets/query/by-dataset/{self._enc(dataset_id)}/task")

    def dataset_list_tables(self, catalog: Optional[str] = None, schema: Optional[str] = None) -> Any:
        """GET /webrobot/api/datasets/query/tables"""
        return self._get("/webrobot/api/datasets/query/tables", {"catalog": catalog, "schema": schema})

    def dataset_get_columns(self, catalog: Optional[str] = None, schema: Optional[str] = None, table: Optional[str] = None) -> Any:
        """GET /webrobot/api/datasets/query/columns"""
        return self._get("/webrobot/api/datasets/query/columns", {"catalog": catalog, "schema": schema, "table": table})

    # ── Datasets Legacy ───────────────────────────────────────────────────────

    def datasets_legacy_list(self, status: Optional[str] = None) -> Any:
        """GET /webrobot/api/datasets-legacy/datasets"""
        return self._get("/webrobot/api/datasets-legacy/datasets", {"status": status})

    def dataset_legacy_get_status(self, dataset_id: str) -> Any:
        """GET /webrobot/api/datasets-legacy/datasets/{datasetId}/status"""
        return self._get(f"/webrobot/api/datasets-legacy/datasets/{self._enc(dataset_id)}/status")

    def dataset_legacy_get_versions(self, dataset_id: str) -> Any:
        """GET /webrobot/api/datasets-legacy/{datasetId}/versions"""
        return self._get(f"/webrobot/api/datasets-legacy/{self._enc(dataset_id)}/versions")

    def dataset_legacy_get_version(self, versionset_id: str) -> Any:
        """GET /webrobot/api/datasets-legacy/version/id/{versionsetId}"""
        return self._get(f"/webrobot/api/datasets-legacy/version/id/{self._enc(versionset_id)}")

    def dataset_legacy_delete_version(self, versionset_id: str) -> Any:
        """DELETE /webrobot/api/datasets-legacy/version/id/{versionsetId}"""
        return self._delete(f"/webrobot/api/datasets-legacy/version/id/{self._enc(versionset_id)}")

    def dataset_legacy_upload(self, project_id: str, bot_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/datasets-legacy/{projectId}/{botId}"""
        return self._post(f"/webrobot/api/datasets-legacy/{self._enc(project_id)}/{self._enc(bot_id)}", body)

    def dataset_legacy_get(self, project_id: str, bot_id: str, dataset_id: str) -> Any:
        """GET /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}"""
        return self._get(f"/webrobot/api/datasets-legacy/{self._enc(project_id)}/{self._enc(bot_id)}/{self._enc(dataset_id)}")

    def dataset_legacy_delete(self, project_id: str, bot_id: str, dataset_id: str) -> Any:
        """DELETE /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}"""
        return self._delete(f"/webrobot/api/datasets-legacy/{self._enc(project_id)}/{self._enc(bot_id)}/{self._enc(dataset_id)}")

    def dataset_legacy_get_input_url(self, project_id: str, bot_id: str, dataset_id: str) -> Any:
        """GET /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}/input/url"""
        return self._get(f"/webrobot/api/datasets-legacy/{self._enc(project_id)}/{self._enc(bot_id)}/{self._enc(dataset_id)}/input/url")

    # ── Cloud Credentials ─────────────────────────────────────────────────────

    def cloud_credentials_list(self, provider: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None) -> Any:
        """GET /webrobot/api/cloud-credentials"""
        return self._get("/webrobot/api/cloud-credentials", {"provider": provider, "page": page, "pageSize": page_size})

    def cloud_credential_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/cloud-credentials"""
        return self._post("/webrobot/api/cloud-credentials", body)

    def cloud_credential_get(self, credential_id: str) -> Any:
        """GET /webrobot/api/cloud-credentials/id/{credentialId}"""
        return self._get(f"/webrobot/api/cloud-credentials/id/{self._enc(credential_id)}")

    def cloud_credential_update(self, credential_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/cloud-credentials/id/{credentialId}"""
        return self._put(f"/webrobot/api/cloud-credentials/id/{self._enc(credential_id)}", body)

    def cloud_credential_delete(self, credential_id: str) -> Any:
        """DELETE /webrobot/api/cloud-credentials/id/{credentialId}"""
        return self._delete(f"/webrobot/api/cloud-credentials/id/{self._enc(credential_id)}")

    def cloud_credentials_by_provider(self, provider: str) -> Any:
        """GET /webrobot/api/cloud-credentials/provider/{provider}"""
        return self._get(f"/webrobot/api/cloud-credentials/provider/{self._enc(provider)}")

    def cloud_credential_test(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/cloud-credentials/test"""
        return self._post("/webrobot/api/cloud-credentials/test", body)

    def cloud_credential_decrypt_field(self, credential_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/cloud-credentials/id/{credentialId}/decrypt-field"""
        return self._post(f"/webrobot/api/cloud-credentials/id/{self._enc(credential_id)}/decrypt-field", body)

    # ── Auth ──────────────────────────────────────────────────────────────────

    def auth_me(self) -> Any:
        """GET /webrobot/api/auth/me"""
        return self._get("/webrobot/api/auth/me")

    def api_keys_list(self, organization: Optional[str] = None, organization_code: Optional[str] = None) -> Any:
        """GET /webrobot/api/auth/api-keys"""
        return self._get("/webrobot/api/auth/api-keys", {"organization": organization, "organization_code": organization_code})

    def api_key_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/auth/api-keys"""
        return self._post("/webrobot/api/auth/api-keys", body)

    def api_key_delete(self, key_id: str) -> Any:
        """DELETE /webrobot/api/auth/api-keys/{key_id}"""
        return self._delete(f"/webrobot/api/auth/api-keys/{self._enc(key_id)}")

    def organization_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/auth/organizations"""
        return self._post("/webrobot/api/auth/organizations", body)

    def organization_get(self, org_id: str) -> Any:
        """GET /webrobot/api/auth/organizations/{id}"""
        return self._get(f"/webrobot/api/auth/organizations/{self._enc(org_id)}")

    def organization_update(self, org_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/auth/organizations/{id}"""
        return self._put(f"/webrobot/api/auth/organizations/{self._enc(org_id)}", body)

    def organization_get_users(self, org_id: str) -> Any:
        """GET /webrobot/api/auth/organizations/{id}/users"""
        return self._get(f"/webrobot/api/auth/organizations/{self._enc(org_id)}/users")

    def organization_assign_user(self, org_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/auth/organizations/{id}/assign-user"""
        return self._post(f"/webrobot/api/auth/organizations/{self._enc(org_id)}/assign-user", body)

    def organization_billing_refresh(self) -> Any:
        """POST /webrobot/api/auth/organizations/billing/refresh"""
        return self._post("/webrobot/api/auth/organizations/billing/refresh", {})

    def user_invites_list(self) -> Any:
        """GET /webrobot/api/auth/user-invites"""
        return self._get("/webrobot/api/auth/user-invites")

    def user_invite_delete(self, invite_id: str) -> Any:
        """DELETE /webrobot/api/auth/user-invites/{id}"""
        return self._delete(f"/webrobot/api/auth/user-invites/{self._enc(invite_id)}")

    def partners_get_by_type(self, partner_type: str) -> Any:
        """GET /webrobot/api/auth/partners/{type}"""
        return self._get(f"/webrobot/api/auth/partners/{self._enc(partner_type)}")

    # ── Billing ───────────────────────────────────────────────────────────────

    def billing_plans_list(self, organization_id: Optional[str] = None, standard: Optional[bool] = None) -> Any:
        """GET /webrobot/api/billing/plans"""
        return self._get("/webrobot/api/billing/plans", {"organizationId": organization_id, "standard": standard})

    def billing_plan_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/billing/plans"""
        return self._post("/webrobot/api/billing/plans", body)

    def billing_plan_update(self, plan_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/billing/plans/{id}"""
        return self._put(f"/webrobot/api/billing/plans/{self._enc(plan_id)}", body)

    def billing_plan_delete(self, plan_id: str) -> Any:
        """DELETE /webrobot/api/billing/plans/{id}"""
        return self._delete(f"/webrobot/api/billing/plans/{self._enc(plan_id)}")

    def billing_custom_plan_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/billing/custom-plan"""
        return self._post("/webrobot/api/billing/custom-plan", body)

    # ── Admin ─────────────────────────────────────────────────────────────────

    def admin_etl_versions_list(self, build_type: Optional[str] = None, active_only: Optional[bool] = None) -> Any:
        """GET /webrobot/api/admin/etl-library-versions"""
        return self._get("/webrobot/api/admin/etl-library-versions", {"buildType": build_type, "activeOnly": active_only})

    def admin_etl_version_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/admin/etl-library-versions"""
        return self._post("/webrobot/api/admin/etl-library-versions", body)

    def admin_etl_version_get(self, version_id: str) -> Any:
        """GET /webrobot/api/admin/etl-library-versions/id/{id}"""
        return self._get(f"/webrobot/api/admin/etl-library-versions/id/{self._enc(version_id)}")

    def admin_etl_version_update(self, version_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/admin/etl-library-versions/id/{id}"""
        return self._put(f"/webrobot/api/admin/etl-library-versions/id/{self._enc(version_id)}", body)

    def admin_etl_version_delete(self, version_id: str) -> Any:
        """DELETE /webrobot/api/admin/etl-library-versions/id/{id}"""
        return self._delete(f"/webrobot/api/admin/etl-library-versions/id/{self._enc(version_id)}")

    def admin_plugin_installations_list(self, organization_id: Optional[str] = None, enabled_only: Optional[bool] = None) -> Any:
        """GET /webrobot/api/admin/plugin-installations"""
        return self._get("/webrobot/api/admin/plugin-installations", {"organizationId": organization_id, "enabledOnly": enabled_only})

    def admin_plugin_installation_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/admin/plugin-installations"""
        return self._post("/webrobot/api/admin/plugin-installations", body)

    def admin_plugin_installation_get(self, installation_id: str) -> Any:
        """GET /webrobot/api/admin/plugin-installations/{id}"""
        return self._get(f"/webrobot/api/admin/plugin-installations/{self._enc(installation_id)}")

    def admin_plugin_installation_update(self, installation_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/admin/plugin-installations/{id}"""
        return self._put(f"/webrobot/api/admin/plugin-installations/{self._enc(installation_id)}", body)

    def admin_plugin_installation_delete(self, installation_id: str) -> Any:
        """DELETE /webrobot/api/admin/plugin-installations/{id}"""
        return self._delete(f"/webrobot/api/admin/plugin-installations/{self._enc(installation_id)}")

    def admin_plugin_installation_enable(self, installation_id: str) -> Any:
        """POST /webrobot/api/admin/plugin-installations/{id}/enable"""
        return self._post(f"/webrobot/api/admin/plugin-installations/{self._enc(installation_id)}/enable")

    def admin_plugin_installation_disable(self, installation_id: str) -> Any:
        """POST /webrobot/api/admin/plugin-installations/{id}/disable"""
        return self._post(f"/webrobot/api/admin/plugin-installations/{self._enc(installation_id)}/disable")

    def admin_plugin_installation_reload(self) -> Any:
        """POST /webrobot/api/admin/plugin-installations/reload"""
        return self._post("/webrobot/api/admin/plugin-installations/reload")

    def admin_plugins_list(self, build_type: Optional[str] = None) -> Any:
        """GET /webrobot/api/admin/plugins"""
        return self._get("/webrobot/api/admin/plugins", {"buildType": build_type})

    def admin_plugin_enable(self, plugin_id: str, build_type: Optional[str] = None) -> Any:
        """POST /webrobot/api/admin/plugins/{pluginId}/enable"""
        return self._post(f"/webrobot/api/admin/plugins/{self._enc(plugin_id)}/enable", params={"buildType": build_type})

    def admin_plugin_disable(self, plugin_id: str, build_type: Optional[str] = None) -> Any:
        """POST /webrobot/api/admin/plugins/{pluginId}/disable"""
        return self._post(f"/webrobot/api/admin/plugins/{self._enc(plugin_id)}/disable", params={"buildType": build_type})

    def admin_system_logs(self, service: Optional[str] = None, level: Optional[str] = None,
                          tail: Optional[int] = None, start_time: Optional[str] = None, end_time: Optional[str] = None) -> Any:
        """GET /webrobot/api/projects/admin/system-logs"""
        return self._get("/webrobot/api/projects/admin/system-logs",
                         {"service": service, "level": level, "tail": tail, "startTime": start_time, "endTime": end_time})

    def admin_mark_zombies(self, timeout_hours: Optional[int] = None) -> Any:
        """POST /webrobot/api/projects/admin/tasks/mark-zombies"""
        return self._post("/webrobot/api/projects/admin/tasks/mark-zombies",
                          params={"timeoutHours": timeout_hours})

    # ── AI Providers ──────────────────────────────────────────────────────────

    def ai_providers_list(self) -> Any:
        """GET /webrobot/api/ai-providers/providers"""
        return self._get("/webrobot/api/ai-providers/providers")

    def ai_provider_models(self, provider: str) -> Any:
        """GET /webrobot/api/ai-providers/providers/{provider}/models"""
        return self._get(f"/webrobot/api/ai-providers/providers/{self._enc(provider)}/models")

    def ai_training_start(self, provider: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/ai-providers/providers/{provider}/training"""
        return self._post(f"/webrobot/api/ai-providers/providers/{self._enc(provider)}/training", body)

    def ai_training_get_status(self, provider: str, job_id: str) -> Any:
        """GET /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/status"""
        return self._get(f"/webrobot/api/ai-providers/providers/{self._enc(provider)}/training/{self._enc(job_id)}/status")

    def ai_training_get_logs(self, provider: str, job_id: str) -> Any:
        """GET /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/logs"""
        return self._get(f"/webrobot/api/ai-providers/providers/{self._enc(provider)}/training/{self._enc(job_id)}/logs")

    def ai_training_cancel(self, provider: str, job_id: str) -> Any:
        """DELETE /webrobot/api/ai-providers/providers/{provider}/training/{jobId}"""
        return self._delete(f"/webrobot/api/ai-providers/providers/{self._enc(provider)}/training/{self._enc(job_id)}")

    def ai_cost_estimate(self, provider: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/ai-providers/providers/{provider}/cost-estimate"""
        return self._post(f"/webrobot/api/ai-providers/providers/{self._enc(provider)}/cost-estimate", body)

    def ai_dataset_upload(self, provider: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/ai-providers/providers/{provider}/datasets"""
        return self._post(f"/webrobot/api/ai-providers/providers/{self._enc(provider)}/datasets", body)

    def ai_huggingface_publish(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/ai-providers/providers/huggingface/models/publish"""
        return self._post("/webrobot/api/ai-providers/providers/huggingface/models/publish", body)

    # ── Python Extensions ─────────────────────────────────────────────────────

    def python_ext_info(self) -> Any:
        """GET /webrobot/api/python-extensions/info"""
        return self._get("/webrobot/api/python-extensions/info")

    def python_ext_supported_types(self) -> Any:
        """GET /webrobot/api/python-extensions/supported-types"""
        return self._get("/webrobot/api/python-extensions/supported-types")

    def python_ext_list_by_agent(self, agent_id: str) -> Any:
        """GET /webrobot/api/python-extensions/agents/{agentId}/python-extensions"""
        return self._get(f"/webrobot/api/python-extensions/agents/{self._enc(agent_id)}/python-extensions")

    def python_ext_update_agent_extensions(self, agent_id: str, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/python-extensions/agents/{agentId}/python-extensions"""
        return self._post(f"/webrobot/api/python-extensions/agents/{self._enc(agent_id)}/python-extensions", body)

    def python_ext_get_agent_extensions(self, agent_id: str) -> Any:
        """GET /webrobot/api/python-extensions/agents/{agentId}/extensions"""
        return self._get(f"/webrobot/api/python-extensions/agents/{self._enc(agent_id)}/extensions")

    def python_ext_register(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/python-extensions/python-extensions/register"""
        return self._post("/webrobot/api/python-extensions/python-extensions/register", body)

    def python_ext_update(self, extension_id: str, body: Dict[str, Any]) -> Any:
        """PUT /webrobot/api/python-extensions/python-extensions/{extensionId}"""
        return self._put(f"/webrobot/api/python-extensions/python-extensions/{self._enc(extension_id)}", body)

    def python_ext_delete(self, extension_id: str) -> Any:
        """DELETE /webrobot/api/python-extensions/python-extensions/{extensionId}"""
        return self._delete(f"/webrobot/api/python-extensions/python-extensions/{self._enc(extension_id)}")

    def python_ext_validate(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/python-extensions/validate"""
        return self._post("/webrobot/api/python-extensions/validate", body)

    def python_ext_process_yaml(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/python-extensions/process-yaml"""
        return self._post("/webrobot/api/python-extensions/process-yaml", body)

    def python_ext_generate_pyspark(self, extension_id: str) -> Any:
        """POST /webrobot/api/python-extensions/python-extensions/{extensionId}/generate-pyspark"""
        return self._post(f"/webrobot/api/python-extensions/python-extensions/{self._enc(extension_id)}/generate-pyspark")

    # ── Cloud (Scheduler / Spark / Training) ──────────────────────────────────

    def cronjobs_list(self, namespace: Optional[str] = None) -> Any:
        """GET /webrobot/cloud/scheduler/cronjobs"""
        return self._get("/webrobot/cloud/scheduler/cronjobs", {"namespace": namespace})

    def cronjob_create(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/cloud/scheduler/cronjobs"""
        return self._post("/webrobot/cloud/scheduler/cronjobs", body)

    def cronjob_get(self, name: str, namespace: Optional[str] = None) -> Any:
        """GET /webrobot/cloud/scheduler/cronjobs/{name}"""
        return self._get(f"/webrobot/cloud/scheduler/cronjobs/{self._enc(name)}", {"namespace": namespace})

    def cronjob_delete(self, name: str, namespace: Optional[str] = None) -> Any:
        """DELETE /webrobot/cloud/scheduler/cronjobs/{name}"""
        return self._delete(f"/webrobot/cloud/scheduler/cronjobs/{self._enc(name)}", {"namespace": namespace})

    def spark_info(self) -> Any:
        """GET /webrobot/cloud/spark/info"""
        return self._get("/webrobot/cloud/spark/info")

    def spark_health(self) -> Any:
        """GET /webrobot/cloud/spark/health"""
        return self._get("/webrobot/cloud/spark/health")

    def spark_capabilities(self) -> Any:
        """GET /webrobot/cloud/spark/capabilities"""
        return self._get("/webrobot/cloud/spark/capabilities")

    def training_cloud_info(self) -> Any:
        """GET /webrobot/cloud/training/info"""
        return self._get("/webrobot/cloud/training/info")

    def training_cloud_health(self) -> Any:
        """GET /webrobot/cloud/training/health"""
        return self._get("/webrobot/cloud/training/health")

    # ── Import / Export (packages) ────────────────────────────────────────────

    def package_export_all(self) -> Any:
        """GET /webrobot/api/package/export/all"""
        return self._get("/webrobot/api/package/export/all")

    def package_export_project(self, project_id: str) -> Any:
        """GET /webrobot/api/package/export/id/{projectId}"""
        return self._get(f"/webrobot/api/package/export/id/{self._enc(project_id)}")

    def package_export_organization(self, organization_id: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """POST /webrobot/api/package/export/organization/{organizationId} (or GET)"""
        if body:
            return self._post(f"/webrobot/api/package/export/organization/{self._enc(organization_id)}", body)
        return self._get(f"/webrobot/api/package/export/organization/{self._enc(organization_id)}")

    def package_import_all(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """POST /webrobot/api/package/import/all (or GET)"""
        if body:
            return self._post("/webrobot/api/package/import/all", body)
        return self._get("/webrobot/api/package/import/all")

    def package_import_project(self, project_id: str, body: Optional[Dict[str, Any]] = None, filename: Optional[str] = None) -> Any:
        """POST /webrobot/api/package/import/id/{projectId} (or GET)"""
        if body:
            return self._post(f"/webrobot/api/package/import/id/{self._enc(project_id)}", body,
                               params={"filename": filename})
        return self._get(f"/webrobot/api/package/import/id/{self._enc(project_id)}")

    def package_import_organization(self, organization_id: str, body: Optional[Dict[str, Any]] = None, filename: Optional[str] = None) -> Any:
        """POST /webrobot/api/package/import/organization/{organizationId} (or GET)"""
        if body:
            return self._post(f"/webrobot/api/package/import/organization/{self._enc(organization_id)}", body,
                               params={"filename": filename})
        return self._get(f"/webrobot/api/package/import/organization/{self._enc(organization_id)}")

    def package_get_upload_url(self) -> Any:
        """GET /webrobot/api/package/upload"""
        return self._get("/webrobot/api/package/upload")

    def package_get_download_url(self) -> Any:
        """GET /webrobot/api/package/download"""
        return self._get("/webrobot/api/package/download")

    # ── ETL entitlements ──────────────────────────────────────────────────────

    def etl_get_entitlements(self, organization_id: Optional[str] = None) -> Any:
        """GET /webrobot/api/etl/entitlements"""
        return self._get("/webrobot/api/etl/entitlements", {"organizationId": organization_id})

    # ── Streaming ─────────────────────────────────────────────────────────────

    def streaming_reschedule_events(self, body: Dict[str, Any]) -> Any:
        """POST /webrobot/api/streaming/reschedule-events"""
        return self._post("/webrobot/api/streaming/reschedule-events", body)

    # ── Strapi tables (generic) ───────────────────────────────────────────────

    def strapi_list(self, table: str, page: Optional[int] = None, page_size: Optional[int] = None) -> Any:
        """GET /api/strapi-tables/{table}"""
        return self._get(f"/api/strapi-tables/{self._enc(table)}", {"page": page, "pageSize": page_size})

    def strapi_insert(self, table: str, body: Dict[str, Any]) -> Any:
        """POST /api/strapi-tables/{table}"""
        return self._post(f"/api/strapi-tables/{self._enc(table)}", body)

    def strapi_get(self, table: str, record_id: str) -> Any:
        """GET /api/strapi-tables/{table}/{id}"""
        return self._get(f"/api/strapi-tables/{self._enc(table)}/{self._enc(record_id)}")

    def strapi_update(self, table: str, record_id: str, body: Dict[str, Any]) -> Any:
        """PUT /api/strapi-tables/{table}/{id}"""
        return self._put(f"/api/strapi-tables/{self._enc(table)}/{self._enc(record_id)}", body)

    def strapi_delete(self, table: str, record_id: str) -> Any:
        """DELETE /api/strapi-tables/{table}/{id}"""
        return self._delete(f"/api/strapi-tables/{self._enc(table)}/{self._enc(record_id)}")

    # ── Manifest (pipeline YAML declarative) ─────────────────────────────────

    def manifest_apply(self, yaml_content: str) -> Any:
        """POST /webrobot/api/manifest/apply — apply a multi-document YAML manifest."""
        return self._post("/webrobot/api/manifest/apply", {"yaml": yaml_content})

    def manifest_validate(self, yaml_content: str) -> Any:
        """POST /webrobot/api/manifest/validate — validate without applying."""
        return self._post("/webrobot/api/manifest/validate", {"yaml": yaml_content})

    def manifest_export(self, kind: str, name_or_id: str) -> Any:
        """GET /webrobot/api/manifest/export — export resource as manifest YAML."""
        return self._get("/webrobot/api/manifest/export", {"kind": kind, "id": name_or_id})

    def manifest_stages_list(
        self,
        category: Optional[str] = None,
        extension_type: Optional[str] = None,
        search: Optional[str] = None,
    ) -> Any:
        """GET /webrobot/api/manifest/stages — list available pipeline stages."""
        return self._get(
            "/webrobot/api/manifest/stages",
            {"category": category, "type": extension_type, "search": search},
        )

    def manifest_stages_get(self, name: str) -> Any:
        """GET /webrobot/api/manifest/stages/{name} — stage detail."""
        return self._get(f"/webrobot/api/manifest/stages/{self._enc(name)}")


class WebRobotError(Exception):
    """Raised when the API returns an HTTP error response."""

    def __init__(self, status_code: int, detail: Any) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"HTTP {status_code}: {detail}")
