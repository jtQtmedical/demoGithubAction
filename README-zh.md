# GitHub Actions 中文示例

本範例涵蓋：
- `.github/workflows/ci-matrix.yml`：Node × OS matrix、PHP 測試、needs 依賴。
- `.github/workflows/pr-fastcheck.yml`：Path filter + concurrency 取消過時工作。
- `cd-examples/`：四種 CD 方案（VM / K8s / GCP Cloud Run / AWS ECS）。
- `.github/workflows/reusable-tests.yml`：可被 workflow_call 重用的工作流。

> 注意：雲端帳號/OIDC 需依環境設定 Secrets（或使用雲供應商教學）。
