# Intelligent Underground Manhole Monitoring (Prototype)

Simulates water-level, gas and tilt sensors, applies configurable threshold rules and records timestamped readings as JSON Lines.

## Run
`python simulator.py --count 20 --interval 1`

Thresholds in this demonstration are illustrative only. A real deployment needs calibrated, certified sensors, site-specific safety limits, reliable communications, fail-safe alerting and field validation. This simulator is not a safety instrument.
