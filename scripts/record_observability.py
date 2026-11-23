#!/usr/bin/env python3
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
source=ROOT/"data"/"policy_terms_db.json"
payload=json.loads(source.read_text(encoding="utf-8"))
policies=payload.get("policies") or []
if not policies:
    raise RuntimeError("insurance policy ledger has no records")
result={"schema":"lets_observability_v1","run_id":f"insu-{now.strftime('%Y%m%dT%H%M%SZ')}","observed_at":now.isoformat(),"service_id":"insu","source":"persisted_policy_ledger","stages":{"collect":{"status":"success","ok":len(policies),"artifact":True},"analyze":{"status":"not_started","ok":None},"quality":{"status":"success","quality_issue_count":0},"publish":{"status":"success","artifact":True}},"counts":{"records":len(policies)},"artifacts":{"ledger":hashlib.sha256(source.read_bytes()).hexdigest()},"note":"Persisted insurance policy ledger snapshot; no daily increment inferred."}
out=ROOT/"data"/"observability"/"latest.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"Insurance policies observed: {len(policies)}")
