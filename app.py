"""OpenAPI document linter and test-plan generator. No network requests are sent."""
from pathlib import Path
import json
HTTP_METHODS={"get","post","put","patch","delete","options","head"}
def analyze_openapi(spec: dict) -> dict:
    if not isinstance(spec,dict): raise ValueError("OpenAPI document must be an object")
    paths=spec.get("paths")
    if not isinstance(paths,dict): raise ValueError("OpenAPI document must include a paths object")
    operations,issues=[],[]
    for path,item in paths.items():
        if not isinstance(item,dict):
            issues.append({"severity":"error","path":path,"message":"Path item must be an object"}); continue
        for method,operation in item.items():
            if method.lower() not in HTTP_METHODS: continue
            operation=operation if isinstance(operation,dict) else {}
            operations.append({"method":method.upper(),"path":path,"operation_id":operation.get("operationId") or f"{method.upper()} {path}","has_summary":bool(operation.get("summary")),"has_responses":bool(operation.get("responses")),"parameters":operation.get("parameters",[])})
            if not operation.get("responses"): issues.append({"severity":"warning","path":path,"method":method.upper(),"message":"No responses documented"})
            if not operation.get("summary"): issues.append({"severity":"info","path":path,"method":method.upper(),"message":"Add a short operation summary"})
    plan=[{"name":f"{op['method']} {op['path']} responds successfully","method":op["method"],"path":op["path"],"kind":"happy_path"} for op in operations]
    plan += [{"name":f"{op['method']} {op['path']} rejects invalid input","method":op["method"],"path":op["path"],"kind":"validation"} for op in operations if op["method"] in {"POST","PUT","PATCH"}]
    return {"title":spec.get("info",{}).get("title","Untitled API"),"openapi_version":spec.get("openapi"),"operation_count":len(operations),"operations":operations,"issues":issues,"test_plan":plan}
def load_spec(path: str | Path) -> dict:
    with open(path,encoding="utf-8") as handle: return json.load(handle)
