import json

"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Creation of container with attribute id and value. Usage of name 
instead of ID is allowed. Attribute value must be used as array.

Imput Example:
    createAttributeTerm(5471, [389832,379361,387323,445594,429610,492511,379364,446674])
Output Example:
    {"terms": {"attributes.5471.value_id:": ["389832", "379361", "387323", "445594", "429610", "492511", "379364", "446674"]}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""

def createAttributeTerm(attr_id, attr_val):
    a = isinstance(attr_val, str)
    if a is True:
        new_attr = f"attributes.{attr_id}.value_name:"  
        new_list = attr_val
    else:
        new_attr = f"attributes.{attr_id}.value_id:"  
        attr_val_len = len(attr_val)
        new_list = []
        for x in range(0, attr_val_len):
            b = attr_val[x]
            new_list.append(str(b))
    new_term = json.dumps({"terms":{new_attr:new_list}})
    return new_term

"""
Creation of container with manufacturer. Usage of name 
instead of ID is allowed.

Input Example:
    newmanterm = createManufacturerTerm("Lenovo")
Output Example:
    {"terms": {"manufacturer_name:": "Lenovo"}}

"""

def createManufacturerTerm(manufact_val):
    a = isinstance(manufact_val, str)
    if a is True:
        new_attr = "manufacturer_name:"
    else:
        new_attr = "manufacturer_id"
    new_term = json.dumps({"terms":{new_attr:manufact_val}})
    return new_term

"""
Creation of container composition. This function has 6 arguments:
    1. Logic - must/should/not etc...
    2. Term 1 (Manufacturer Term Preferable)
    3. Term 2
    4. Term 3
    5. Term 4
    6. Term 5
Logic and Term 1 must be used, others are optional

"""

def composeTerms(logic, man_term, term1 = 0, term2 = 0, term3 = 0, term4 =0):
    a = isinstance(logic, str)
    if a is True:
        if man_term != 0:
            man_term = json.loads(man_term)
            query = json.dumps({"query":{"bool":{logic:[man_term]}}})
        if term1 != 0:
            term1 = json.loads(term1)
            query = json.dumps({"query":{"bool":{logic:[man_term, term1]}}})
        if term2 != 0:
            term2 = json.loads(term2)
            query = json.dumps({"query":{"bool":{"must":[man_term, term1, term2]}}})
        if term3 != 0:
            term3 = json.loads(term3)
            query = json.dumps({"query":{"bool":{"must":[man_term, term1, term2, term3]}}})
        if term4 != 0:
            term4 = json.loads(term4)
            query = json.dumps({"query":{"bool":{"must":[man_term, term1, term2, term3, term4]}}})
    else:
        print("wakalaka")
    return query
