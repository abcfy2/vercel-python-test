# Vercel Python Test

## Deploy on Vercel

```sh
vercel --prod
```

Required environment variables:

- `GEMINI_API_KEY`: Get from [gemini-api](https://ai.google.dev/gemini-api/docs/api-key). It's free.

## Locally

Save `GEMINI_API_KEY=<your_api_key>` in `.env` then run:

```sh
python -m venv venv
source venv/bin/activate
pip install -U -r requirements.txt
uvicorn api.index:app --reload
```
