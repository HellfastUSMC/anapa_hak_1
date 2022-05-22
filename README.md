# anapa_hak_1

```bash
cp .env.dev .env
docker compose up --build
```

You can set `RUN_MIGRATIONS` and `INIT_DB` environment variables to control the deployment flow. Set `"yes"` if you want any.

The API will be at `0.0.0.0:80/api/`
