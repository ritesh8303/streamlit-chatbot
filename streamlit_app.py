import streamlit as st

# Chatbot Data
COMPANY_INFO = {
    "name": "TechXYZ",
    "about": "We specialize in AI, Cloud, and Software Development solutions.",
    "products": ["AI-powered Chatbots", "Cloud Services", "Web Applications"],
    "services": ["Custom Software Development", "IT Consulting", "Support & Maintenance"]
}

# Streamlit App
st.title("Welcome to the TechXYZ Chatbot")
st.write("Hi there! Ask me about our company, products, or services.")

# User Input
user_query = st.text_input("Your question:")

# Generate Response
if st.button("Ask"):
    if "about" in user_query.lower():
        st.success(COMPANY_INFO["about"])
    elif "products" in user_query.lower():
        st.success("Our products include: " + ", ".join(COMPANY_INFO["products"]))
    elif "services" in user_query.lower():
        st.success("Our services include: " + ", ".join(COMPANY_INFO["services"]))
    else:
        st.error("I'm sorry, I didn't understand. Please ask about 'about', 'products', or 'services'.")
