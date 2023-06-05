"""An example program that uses the elsapy module"""

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json

## Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

client = ElsClient(config['apikey'])

# doc_srch = FullDoc('vpn AND PUBYEAR = 2021','sciencedirect')
# print(doc_srch._uri)
# doc_srch.execute(client, get_all = True)
# print ("doc_srch has", len(doc_srch.results), "results.")
# print(doc_srch.results)

doc_srch = ElsSearch('vpn and OPENACCESS(1)', 'sciencedirect')
doc_srch.execute(client, get_all = True)
print("doc_srch has", len(doc_srch.results), "results.")

file_output = []
for i in range(0, 300):
    doi_doc = FullDoc(doi = doc_srch.results[i]["prism:doi"])
    if doi_doc.read(client):
        print("Przetwarzanie", i+1, "artykułu.")
        file_output.append(doi_doc._data)
    else:
        print ("Read document failed.")

with open('wyniki3.txt', 'w', encoding="utf-8") as f:
    for line in file_output:
        f.write(f"{line}\n")


# print(doc_srch.results[24]["dc:identifier"])

# with open('wyniki.txt', 'w', encoding="utf-8") as f:
#     for line in doc_srch.results:
#         f.write(f"{line},\n")

#
# doi_doc = FullDoc(doi = '10.1016/j.procs.2021.12.298')
# if doi_doc.read(client):
#     print ("doi_doc.title: ", doi_doc.title)
#     doi_doc.write()
# else:
#     print ("Read document failed.")