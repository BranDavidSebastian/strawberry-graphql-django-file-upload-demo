1. `pip install -r requirements.txt`
2. `./manage.py migrate`
3. `./manage.py runserver`
4. `curl localhost:8000/graphql/ -F operations='{ "query": "mutation($file: Upload!){ readFile(file: $file) }", "variables": { "file": null } }' -F map='{ "file": ["variables.file"] }' -F file=@a.txt`
5. Result is "Unsupported content type"
6. Go to requirements.txt, comment newer versions and uncomment old ones
7. `pip install -r requirements.txt` again
8. in urls.py remove 'multipart_uploads_enabled=True'
9. `curl localhost:8000/graphql/ -F operations='{ "query": "mutation($file: Upload!){ readFile(file: $file) }", "variables": { "file": null } }' -F map='{ "file": ["variables.file"] }' -F file=@a.txt`
10. now it works