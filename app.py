import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0, step=0.1)
    num2 = st.number_input("Enter the second number", value=0.0, step=0.1)

    # Dropdown for selecting the operation
    operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Button to calculate
    if st.button("Calculate"):
        result = None
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed.")

        # Display the result
        if result is not None:
            st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()
