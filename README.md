## `config.json` format

```json
[
    {
        "url": "https://...",
        "message": "Notification message for this URL",
        "matches": [
            {
                "message": "Notification message for this specific match. This overrides the URL message.",
                "startswith": "https://...",
                "endswith": ".filetype"
            }
        ]
    }
]
```

- the `message` inside a match is optional
- `startswith` and `endswith` are mandatory