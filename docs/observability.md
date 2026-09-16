# 运行可观测性

商用运行建议记录以下字段：

- `request_id`：一次生成请求的唯一标识。
- `model`、`platform`、`goal`：用于定位配置和结果差异。
- `duration_seconds`、`tokens_used`：用于性能和成本统计。
- `variant_count`、`quality_gate_passed`：用于比较候选质量。
- `error_type`：区分配置、网络、供应商和解析错误。

日志中禁止写入 API Key、完整账号配置、个人信息和未脱敏的用户内容。生产环境应设置超时、重试上限、成本上限和告警阈值，并保留可回滚的版本号。
