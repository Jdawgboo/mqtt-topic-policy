# MQTT Topic Policy

Validate MQTT topic strings against local prefix, depth, wildcard, and segment policies.

```bash
cat topic.json | python tool.py
python -m unittest -v
```

This utility does not connect to MQTT brokers or authorize publish/subscribe operations.
