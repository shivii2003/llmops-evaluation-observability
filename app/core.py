def evaluate(records):
    if not records: return {'count':0,'citation_coverage':0}
    return {'count':len(records),'citation_coverage':sum(bool(r.get('sources')) for r in records)/len(records)}
