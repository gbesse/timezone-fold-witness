import datetime as dt
from zoneinfo import ZoneInfo,ZoneInfoNotFoundError
from .common import integer

def candidates(raw,zone):
 local=dt.datetime.fromisoformat(raw)
 if local.tzinfo is not None:raise ValueError('local_datetime_required')
 result={}
 for fold in (0,1):
  aware=local.replace(tzinfo=zone,fold=fold);utc=aware.astimezone(dt.timezone.utc);back=utc.astimezone(zone)
  if back.replace(tzinfo=None)==local:result.setdefault(utc,{'fold':fold,'utc':utc.isoformat(),'offset_seconds':int(aware.utcoffset().total_seconds())})
 return [result[k]for k in sorted(result)]
def run(data):
 try:zone=ZoneInfo(data['zone'])
 except(ZoneInfoNotFoundError,ValueError):raise ValueError('zone')from None
 start=candidates(data['start_local'],zone);end=candidates(data['end_local'],zone)
 def selected(items,key):
  if key not in data:return items
  fold=integer(data[key],0,1)
  if len(items)==1:return items
  return[x for x in items if x['fold']==fold]
 pairs=[]
 for a in selected(start,'start_fold'):
  for b in selected(end,'end_fold'):
   seconds=(dt.datetime.fromisoformat(b['utc'])-dt.datetime.fromisoformat(a['utc'])).total_seconds();pairs.append({'start_fold':a['fold'],'end_fold':b['fold'],'elapsed_seconds':seconds,'chronological':seconds>=0})
 return {'zone':data['zone'],'start':{'status':'gap'if not start else'ambiguous'if len(start)>1 else'unique','candidates':start},'end':{'status':'gap'if not end else'ambiguous'if len(end)>1 else'unique','candidates':end},'possible_intervals':pairs,'timezone_database_version':'runtime_database_not_pinned','model':'actual_zoneinfo_utc_roundtrip_no_silent_fold_choice'}
