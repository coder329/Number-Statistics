import streamlit as st

st.set_page_config(
    page_title="Number Statistics",
    page_icon="🔢",
    layout="centered"
)

st.title("🔢 Number Statistics")
st.write(
    "Enter your own numbers and the application will identify "
    "even numbers, odd numbers, the largest number, and the smallest number."
)

st.divider()

st.subheader("📝 Enter Your Numbers")

numbers_input = st.text_area(
    "Enter numbers separated by commas or new lines:",
    placeholder="Example: 12, 7, 25, 4, 18, 31",
    height=150
)

if st.button("Analyze Numbers", type="primary"):

    if not numbers_input.strip():

        st.warning("Please enter at least one number.")

    else:

        try:

            cleaned_input = numbers_input.replace("\n", ",")

            numbers = [
                float(value.strip())
                for value in cleaned_input.split(",")
                if value.strip()
            ]

            if not numbers:
                st.warning("Please enter valid numbers.")

            else:

                even_numbers = [
                    number for number in numbers
                    if number % 2 == 0
                ]

                odd_numbers = [
                    number for number in numbers
                    if number % 2 != 0
                ]

                largest_number = max(numbers)
                smallest_number = min(numbers)

                st.success("Number analysis completed successfully! ✅")

                st.divider()

                st.subheader("📊 Results")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Total Numbers", len(numbers))
                    st.metric("Even Numbers", len(even_numbers))

                with col2:
                    st.metric("Odd Numbers", len(odd_numbers))
                    st.metric("Largest Number", largest_number)

                st.metric("Smallest Number", smallest_number)

                st.divider()

                st.subheader("✅ Even Numbers")
                st.write(even_numbers)

                st.subheader("🔢 Odd Numbers")
                st.write(odd_numbers)

        except ValueError:

            st.error(
                "Invalid input. Please enter numbers separated "
                "by commas or new lines."
            )

st.divider()

st.caption("Number Statistics | Built with Python and Streamlit")