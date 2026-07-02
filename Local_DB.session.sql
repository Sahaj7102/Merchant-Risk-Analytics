SELECT 
    merchant_typology,
    COUNT(*) AS merchant_count,
    ROUND(AVG(custom_risk_score), 2) AS avg_calculated_risk,
    SUM(actual_fraud_count) AS total_detected_fraud,
    SUM(drain_tx_count) AS total_drain_anomalies
FROM mid_elite_risk_metrics
GROUP BY merchant_typology
ORDER BY avg_calculated_risk DESC;