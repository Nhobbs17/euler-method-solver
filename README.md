# Euler's Method Solver

A Streamlit web application that implements Euler's method for solving differential equations of the form dy/dx = ky.

🔗 **[Try the Live App](https://your-app-name.streamlit.app)**

## Features

- Interactive web interface for inputting parameters
- Step-by-step calculations using Euler's method
- Comparison with analytical solution
- Visualization of results with matplotlib
- Export functionality for CSV download
- Input validation and error handling

## Quick Deploy to Streamlit Cloud

1. **Fork or download this repository**
2. **Upload to your GitHub account**
3. **Go to [share.streamlit.io](https://share.streamlit.io)**
4. **Click "New app" and connect your GitHub repository**
5. **Set main file path to `app.py`**
6. **Click "Deploy"**

## Local Installation

1. Install Python 3.8 or higher
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/euler-method-solver.git
   cd euler-method-solver
   ```
3. Install required packages:
   ```bash
   pip install -r streamlit_requirements.txt
   ```

## Usage

### Running Locally
```bash
streamlit run app.py
```

### Using the App
1. Open your browser to the URL shown (usually http://localhost:8501)
2. Enter your parameters:
   - **k**: Proportionality constant in the equation dy/dx = ky
   - **x₀**: Initial x value
   - **y₀**: Initial y value
   - **Target x**: The x value to stop calculations at
   - **Step size (h)**: Size of each step in the calculation
3. Click "Calculate Solution" to see the results

## Mathematical Background

This app solves differential equations of the form:
**dy/dx = ky**

Where:
- k is the proportionality constant
- The rate of change of y is directly proportional to the current value of y

The analytical solution is: **y = y₀ × e^(k×(x-x₀))**

## Files Structure

```
euler-method-solver/
├── app.py                      # Main application file
├── streamlit_requirements.txt  # Python dependencies
├── packages.txt               # System packages (if needed)
├── .streamlit/
│   └── config.toml           # Streamlit configuration
└── README.md                 # This file
```

## Deployment Options

### Streamlit Cloud (Recommended)
- Free hosting for public repositories
- Automatic updates from GitHub
- Easy sharing with public URL

### Other Platforms
- **Heroku**: Rename `streamlit_requirements.txt` to `requirements.txt` and add `Procfile`
- **Railway**: Direct GitHub integration
- **Render**: Automatic Streamlit detection

## License

This project is open source and available under the MIT License.