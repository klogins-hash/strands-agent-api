# Deploy Strands Agent API to Railway

## Option 1: Deploy via Railway Web UI (Easiest)

1. **Go to Railway Dashboard**
   - Visit https://railway.app/dashboard
   - Click "New Project"
   - Select "Deploy from GitHub repo"

2. **Connect Repository**
   - Push this code to GitHub first:
     ```bash
     # Create a new repo on GitHub, then:
     git remote add origin https://github.com/YOUR_USERNAME/strands-agent-api.git
     git push -u origin master
     ```
   - Or use "Deploy from local repo" option

3. **Configure Environment Variables**
   - In Railway dashboard, go to your service
   - Click "Variables"
   - Add: `OPENAI_API_KEY` = your OpenAI API key

4. **Deploy**
   - Railway will auto-detect the configuration
   - Click "Deploy"
   - Get your URL from the "Settings" tab

## Option 2: Deploy via Railway CLI

1. **Login to Railway**
   ```bash
   railway login
   ```

2. **Initialize Project**
   ```bash
   railway init
   ```

3. **Set Environment Variables**
   ```bash
   railway variables set OPENAI_API_KEY="your-key-here"
   ```

4. **Deploy**
   ```bash
   railway up
   ```

5. **Generate Domain**
   ```bash
   railway domain
   ```

## Option 3: Quick Deploy Button

Click this button to deploy directly:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/YOUR_USERNAME/strands-agent-api)

## After Deployment

1. **Get your URL** from Railway dashboard
2. **Test the API**:
   ```bash
   curl https://your-app.up.railway.app/health
   ```

3. **Use in n8n**:
   - Add HTTP Request node
   - URL: `https://your-app.up.railway.app/chat`
   - Method: POST
   - Body: `{"message": "{{ $json.chatInput }}"}`

## Environment Variables Required

- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `PORT` - Automatically set by Railway

## Troubleshooting

If deployment fails:
1. Check Railway logs in the dashboard
2. Verify `OPENAI_API_KEY` is set
3. Ensure Python 3.10+ is being used
4. Check that all dependencies install correctly
