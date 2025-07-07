# Deploy to Streamlit Cloud - Step by Step

## Prerequisites
- GitHub account
- Streamlit Cloud account (free at share.streamlit.io)

## Step 1: Upload to GitHub

1. **Create a new repository on GitHub:**
   - Go to [github.com](https://github.com) and sign in
   - Click "New" to create a new repository
   - Name it something like `euler-method-solver`
   - Make it public (required for free Streamlit Cloud)
   - Check "Add a README file"

2. **Upload your files:**
   - Click "uploading an existing file" 
   - Drag and drop these files:
     - `app.py`
     - `streamlit_requirements.txt`
     - `packages.txt`
     - `README.md`
   - Create a folder called `.streamlit` and upload `config.toml` inside it

## Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Create new app:**
   - Click "New app"
   - Select your GitHub repository
   - Choose the branch (usually `main`)
   - Set main file path to `app.py`
   - Advanced settings:
     - Requirements file: `streamlit_requirements.txt`
     - Packages file: `packages.txt`

3. **Deploy:**
   - Click "Deploy"
   - Wait for deployment (usually 2-5 minutes)
   - Your app will be available at: `https://your-repo-name.streamlit.app`

## Step 3: Share Your App

Once deployed, you can:
- Share the public URL with anyone
- App updates automatically when you push changes to GitHub
- View logs and manage the app from your Streamlit Cloud dashboard

## Troubleshooting

**Common issues:**
- Make sure repository is public
- Check that `streamlit_requirements.txt` is in the root directory
- Verify all file names are correct (case-sensitive)
- If deployment fails, check the logs in Streamlit Cloud

**File requirements:**
- `app.py` - Main application (must be in root)
- `streamlit_requirements.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit configuration

## Alternative: Quick Deploy Button

Add this to your GitHub README for one-click deployment:

```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourusername/euler-method-solver/main/app.py)
```

Replace `yourusername` and `euler-method-solver` with your actual GitHub username and repository name.