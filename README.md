1. `uv install`
2. `uv run ./manage.py migrate`
3. `uv run ./manage.py runserver`
4. `curl localhost:8000/graphql/ -F operations='{ "query": "mutation($file: Upload!){ readFile(file: $file) }", "variables": { "file": null } }' -F map='{ "file": ["variables.file"] }' -F file=@a.txt`
