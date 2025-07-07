import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def euler_method(k, x0, y0, x_target, h):
    """
    Implement Euler's method for solving dy/dx = ky
    
    Parameters:
    k: proportionality constant
    x0: initial x value
    y0: initial y value
    x_target: target x value to stop at
    h: step size
    
    Returns:
    DataFrame with step-by-step calculations
    """
    # Calculate number of steps
    n_steps = int((x_target - x0) / h)
    
    # Initialize arrays to store results
    x_values = [x0]
    y_values = [y0]
    dy_dx_values = [k * y0]
    
    # Perform Euler's method iterations
    x_current = x0
    y_current = y0
    
    for i in range(n_steps):
        # Calculate derivative at current point
        dy_dx = k * y_current
        
        # Update values using Euler's method
        x_next = x_current + h
        y_next = y_current + h * dy_dx
        
        # Store values
        x_values.append(x_next)
        y_values.append(y_next)
        dy_dx_values.append(k * y_next)
        
        # Update current values
        x_current = x_next
        y_current = y_next
    
    # Create DataFrame for results
    df = pd.DataFrame({
        'Step': range(len(x_values)),
        'x': x_values,
        'y': y_values,
        'dy/dx': dy_dx_values
    })
    
    return df

def analytical_solution(k, x0, y0, x):
    """
    Calculate the analytical solution for dy/dx = ky
    Solution: y = y₀ * e^(k*(x-x₀))
    """
    return y0 * math.exp(k * (x - x0))

def validate_inputs(k, x0, y0, x_target, h):
    """
    Validate input parameters
    """
    errors = []
    
    try:
        k = float(k)
    except (ValueError, TypeError):
        errors.append("Proportionality constant k must be a valid number")
        
    try:
        x0 = float(x0)
    except (ValueError, TypeError):
        errors.append("Initial x value must be a valid number")
        
    try:
        y0 = float(y0)
    except (ValueError, TypeError):
        errors.append("Initial y value must be a valid number")
        
    try:
        x_target = float(x_target)
    except (ValueError, TypeError):
        errors.append("Target x value must be a valid number")
        
    try:
        h = float(h)
        if h <= 0:
            errors.append("Step size must be positive")
    except (ValueError, TypeError):
        errors.append("Step size must be a valid positive number")
    
    if len(errors) == 0:
        if x_target <= x0:
            errors.append("Target x value must be greater than initial x value")
    
    return errors

# Main Streamlit application
def main():
    st.title("Euler's Method Solver")
    st.markdown("### Differential Equation: dy/dx = ky")
    
    # Educational content
    with st.expander("📚 About Euler's Method"):
        st.markdown("""
        **Euler's Method** is a first-order numerical procedure for solving ordinary differential equations (ODEs) 
        with a given initial value.
        
        For the differential equation **dy/dx = ky**, where:
        - **k** is the proportionality constant
        - The rate of change of y is directly proportional to the current value of y
        
        **The Method:**
        1. Start with initial values (x₀, y₀)
        2. Calculate the slope at the current point: dy/dx = ky
        3. Use the slope to estimate the next point: y_{n+1} = y_n + h × (dy/dx)
        4. Repeat until reaching the target x value
        
        **Analytical Solution:** y = y₀ × e^(k×(x-x₀))
        """)
    
    # Input section
    st.header("Input Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        k = st.number_input("Proportionality constant (k)", 
                           value=0.5, 
                           help="The constant k in the equation dy/dx = ky")
        
        x0 = st.number_input("Initial x value (x₀)", 
                            value=0.0, 
                            help="Starting x coordinate")
        
        y0 = st.number_input("Initial y value (y₀)", 
                            value=1.0, 
                            help="Starting y coordinate")
    
    with col2:
        x_target = st.number_input("Target x value", 
                                  value=2.0, 
                                  help="X value to stop the calculation at")
        
        h = st.number_input("Step size (h)", 
                           value=0.1, 
                           min_value=0.001,
                           help="Size of each step in the calculation")
    
    # Validate inputs
    if st.button("Calculate Solution", type="primary"):
        errors = validate_inputs(k, x0, y0, x_target, h)
        
        if errors:
            st.error("Please fix the following errors:")
            for error in errors:
                st.error(f"• {error}")
        else:
            # Perform calculations
            with st.spinner("Calculating..."):
                # Get Euler's method results
                results_df = euler_method(k, x0, y0, x_target, h)
                
                # Calculate analytical solution at target point
                analytical_result = analytical_solution(k, x0, y0, x_target)
                euler_result = results_df.iloc[-1]['y']
                
                # Display results
                st.success("Calculation completed!")
                
                # Final results comparison
                st.header("Final Results")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Euler's Method Result", f"{euler_result:.6f}")
                
                with col2:
                    st.metric("Analytical Solution", f"{analytical_result:.6f}")
                
                with col3:
                    error = abs(euler_result - analytical_result)
                    st.metric("Absolute Error", f"{error:.6f}")
                
                # Step-by-step results table
                st.header("Step-by-Step Calculations")
                
                # Format the DataFrame for better display
                display_df = results_df.copy()
                display_df['x'] = display_df['x'].round(6)
                display_df['y'] = display_df['y'].round(6)
                display_df['dy/dx'] = display_df['dy/dx'].round(6)
                
                st.dataframe(display_df, use_container_width=True)
                
                # Plot the results
                st.header("Visualization")
                
                # Create analytical solution curve for comparison
                x_analytical = np.linspace(x0, x_target, 1000)
                y_analytical = [analytical_solution(k, x0, y0, x) for x in x_analytical]
                
                fig, ax = plt.subplots(figsize=(10, 6))
                
                # Plot analytical solution
                ax.plot(x_analytical, y_analytical, 'b-', label='Analytical Solution', linewidth=2)
                
                # Plot Euler's method results
                ax.plot(results_df['x'], results_df['y'], 'ro-', label="Euler's Method", markersize=4)
                
                # Add initial point
                ax.plot(x0, y0, 'go', markersize=8, label='Initial Point')
                
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_title(f'Solution of dy/dx = {k}y with Initial Condition ({x0}, {y0})')
                ax.legend()
                ax.grid(True, alpha=0.3)
                
                st.pyplot(fig)
                
                # Export functionality
                st.header("Export Results")
                
                # Convert DataFrame to CSV
                csv = results_df.to_csv(index=False)
                
                st.download_button(
                    label="Download Results as CSV",
                    data=csv,
                    file_name=f"euler_method_results_k{k}_h{h}.csv",
                    mime="text/csv"
                )
                
                # Display calculation summary
                with st.expander("📊 Calculation Summary"):
                    st.write(f"**Differential Equation:** dy/dx = {k}y")
                    st.write(f"**Initial Condition:** ({x0}, {y0})")
                    st.write(f"**Target x:** {x_target}")
                    st.write(f"**Step Size:** {h}")
                    st.write(f"**Number of Steps:** {len(results_df) - 1}")
                    st.write(f"**Final Euler Result:** {euler_result:.6f}")
                    st.write(f"**Analytical Result:** {analytical_result:.6f}")
                    st.write(f"**Absolute Error:** {abs(euler_result - analytical_result):.6f}")
                    st.write(f"**Relative Error:** {abs(euler_result - analytical_result) / abs(analytical_result) * 100:.4f}%")

if __name__ == "__main__":
    main()
