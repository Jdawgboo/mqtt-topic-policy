"""Validate MQTT topic strings without a broker connection."""
from __future__ import annotations
def validate(topic:str,policy:dict)->list[str]:
 errors=[];parts=topic.split('/')
 if not topic or '' in parts:errors.append('empty segment')
 if len(parts)>policy.get('max_depth',99):errors.append('too deep')
 if policy.get('prefix') and not topic.startswith(policy['prefix'].rstrip('/')+'/'):errors.append('wrong prefix')
 if not policy.get('allow_wildcards',False) and ('#' in topic or '+' in topic):errors.append('wildcard forbidden')
 allowed=set(policy.get('allowed_first_segments',[]))
 if allowed and parts[0] not in allowed:errors.append('first segment forbidden')
 return errors
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(validate(p['topic'],p['policy']),indent=2))
