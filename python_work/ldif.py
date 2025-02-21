import base64
from typing import List
from typing import Dict

file = 'elo-acc01-03.ldif'

ldif: Dict[str,str] = {}
person: List[str] = []

with open(file) as f_obj:
    for line in f_obj:
        clean_line = line.rstrip()
        if not clean_line:
            key: str = person[0].removeprefix('dn: uid=').removesuffix(',ou=People,dc=rijkszaak,dc=nl')
            ldif[key] = person
            # print(person, end='')
            person = []
        else:
            person.append(clean_line)
# print(ldif)

for key, person in ldif.items():
    # print(person)
    sn, cn = '', ''
    for line_no in range(0, len(person)):
        line = person[line_no]
        if line.startswith('cn::'):
            base64_name = line.removeprefix('cn:: ')
            person[line_no] = 'cn: ' + base64.b64decode(base64_name).decode('utf-8')
            # print("convert " + base64_name + " into: " + person[line_no])

        if line.startswith('cn: '):
            cn = line.removeprefix('cn: ')
        
        if line.startswith('sn: '):
            sn = line.removeprefix('sn: ')
    
    print(cn + ', ' + sn) 


# print(ldif)


