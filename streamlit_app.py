import streamlit as st

st.title("M.A.Y.L.A")
st.image("logo.png", caption="")

def main():
    st.title("Genetic Profile & Clinical Trials Finder")
    
    # User inputs
    physician = st.text_input("Enter the physician's name:")
    name = st.text_input("Enter patient's name:")
    email = st.text_input("Enter patient's email:")
    year = st.number_input("Enter patient's year of birth:", min_value=1900, max_value=2025, step=1)
    city = st.text_input("From what country and city is the patient from:")
    
    # Consent section
    st.subheader("Consent")
    patient_consent = st.checkbox("As the patient, I acknowledge and consent to the release of my information to M.A.Y.L.A as well as my participation. I acknowledge that I have the right to withdraw at any time with no consequence.")
    physician_consent = st.checkbox("As the physician, I confirm that I have discussed all the required information with the patient and I will oversee the entire process with M.A.Y.L.A.")
    
    # Signatures
    patient_signature = st.text_input("Patient Signature:")
    physician_signature = st.text_input("Physician Signature:")
    
    # File upload
    uploaded_file = st.file_uploader("Upload Medical Report & History (PDF or TXT)", type=["pdf", "txt"])
    
    # Submission button
    submitted = st.button("Submit")
    
    if submitted and patient_consent and physician_consent:
        if uploaded_file is not None:
            st.success("Medical report uploaded successfully.")
        st.error("No clinical trials found.")
        
        # Group Connection Service
        st.subheader("Group Connection Service")
        group_consent = st.checkbox("Do you agree to have your contact shared with the people that match your condition?", key="group_consent")
        
    # Ensure the section remains visible even after interactions
    if "group_consent" in st.session_state and st.session_state.group_consent:
        st.success("Your contact will be shared with matching individuals.")
        st.markdown("[Click here to connect with others with this genetic profile](#)")

if __name__ == "__main__":
    main()
