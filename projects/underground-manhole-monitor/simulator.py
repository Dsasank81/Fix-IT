"""IoT manhole sensor simulator with threshold-based alert generation."""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json, random, time, argparse

@dataclass
class Reading:
    timestamp: str
    water_level_cm: float
    gas_ppm: float
    temperature_c: float
    tilt_deg: float
    alert: str

def classify(water, gas, tilt):
    alerts=[]
    if water >= 70: alerts.append("HIGH_WATER_LEVEL")
    if gas >= 25: alerts.append("DANGEROUS_GAS_LEVEL")
    if tilt >= 12: alerts.append("ABNORMAL_TILT")
    return "|".join(alerts) if alerts else "NORMAL"

def generate():
    water=random.uniform(5,95); gas=random.uniform(1,40); tilt=random.uniform(0,20)
    return Reading(datetime.now(timezone.utc).isoformat(),round(water,2),round(gas,2),round(random.uniform(20,55),2),round(tilt,2),classify(water,gas,tilt))

def main():
    p=argparse.ArgumentParser(); p.add_argument("--count",type=int,default=10); p.add_argument("--interval",type=float,default=0.5); p.add_argument("--output",default="readings.jsonl"); a=p.parse_args()
    with open(a.output,"a",encoding="utf-8") as f:
        for _ in range(a.count):
            r=generate(); line=json.dumps(asdict(r)); f.write(line+"\n"); print(line); time.sleep(a.interval)
if __name__=="__main__": main()
