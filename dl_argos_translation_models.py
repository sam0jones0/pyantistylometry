import json

import requests

r = requests.get(
    "https://raw.githubusercontent.com/argosopentech/argospm-index/main/index.json"
)
r.raise_for_status()

pkg_idx = json.loads(r.text)

for package in pkg_idx:
    ...


# single_pkg = [
#     {
#         "package_version": "1.0",
#         "argos_version": "1.0",
#         "from_code": "ar",
#         "from_name": "Arabic",
#         "to_code": "en",
#         "to_name": "English",
#         "links": [
#             "https://argosopentech.nyc3.digitaloceanspaces.com/argospm/translate-ar_en-1_0.argosmodel",
#             "ipfs://QmV5bmf8iqKpoGoyuTzEppaSWdceuW6zgiePaUr5ThPCpW",
#         ],
#     },
# ]