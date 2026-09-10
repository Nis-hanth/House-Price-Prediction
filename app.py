# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle

# # ============================================================
# # 2. LOAD THE TRAINED ML MODEL
# # ============================================================

# with open("Hose_price_model.pkl","rb") as file:
#     model = pickle.load(file)


# # ============================================================
# # 3. STREAMLIT PAGE SETTINGS
# # ============================================================

# st.set_page_config(

#     page_title="House Priice Prediction",

#     page_icon="🏠",
#     layout="wide"
# )





# st.title("🏠 House Price Prediction")
# st.write(
#           "Enter The House Details below To predict The Sal price"
# )

# # ============================================================ # 3. CUSTOM CSS # ============================================================ # Add our own CSS to make the application attractive st.markdown( """ <style> /* Main application background */ .stApp { background-color: #f5f7fa; } /* Main title */ .main-title { text-align: center; font-size: 45px; font-weight: bold; margin-bottom: 5px; } /* Subtitle */ .subtitle { text-align: center; font-size: 18px; margin-bottom: 30px; } /* Prediction result box */ .prediction-box { padding: 25px; border-radius: 15px; text-align: center; margin-top: 25px; background-color: white; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); } /* Price text */ .price { font-size: 35px; font-weight: bold; } /* Section heading */ .section-title { font-size: 24px; font-weight: bold; margin-top: 10px; margin-bottom: 15px; } </style> """, unsafe_allow_html=True )


# # ============================================================
# # 5. USER INPUT - OVERALL QUALITY
# # ============================================================

# overall_qual = st.number_input(
#     "Overall Quality",
#     min_value=1,
#     max_value=10,
#     value=5
# )
# gr_liv_area = st.number_input(
#     "Living Area (sqft)",
#    min_value=100,
#    max_value=10000,
#    value=1500

# )

# garage_cars = st.number_input(
#     "Garage Cars",
#     min_value=0,
#     max_value=5,
#     value=2
# )
# total_bsmt_sf = st.number_input(
#   "Total Basement Area (sqft)",
#   min_value=0,
#   max_value=5000,
#   value=1000
# )

# year_built = st.number_input(
#     "Year Built",
#     min_value=1800,
#     max_value=2026,
#     value=2000
# )

# full_bath = st.number_input(
#     "Full Bathrooms",
#     min_value=0,
#     max_value=5,
#     value=2
# )

# bedroom_abv_gr = st.number_input(
#     "Bedrooms",
#     min_value=0,
#     max_value=10,
#     value=3
# )

# lot_area = st.number_input(
#     "Lot Area (sqft)",
#     min_value=100,
#     max_value=100000,
#     value=8000
# )

# if st.button("Predict House Price"):
#     new_house = pd.DataFrame({
#        'OverallQual':[overall_qual], 
#        'GrLivArea':[gr_liv_area],
#          'GarageCars':[garage_cars], 
#          'TotalBsmtSF':[total_bsmt_sf],
#        'YearBuilt':[year_built],
#          'FullBath':[full_bath], 
#          'BedroomAbvGr':[bedroom_abv_gr], 
#          'LotArea':[lot_area]
#     })
#     prediction = model.predict(new_house)[0]

#     st.success(
#         f"🏠 Predicted sale price: ₹{prediction:,.2f}"
#     )





# ============================================================
# HOUSE PRICE PREDICTION APP
# ============================================================

# Import Streamlit
import streamlit as st

# Import Pandas
import pandas as pd

# Import pickle
# Used to load our trained ML model
import pickle


# ============================================================
# 1. LOAD TRAINED MODEL
# ============================================================

# Open the saved ML model
with open("Hose_price_model.pkl", "rb") as file:

    # Load the model
    model = pickle.load(file)


# ============================================================
# 2. PAGE SETTINGS
# ============================================================

# Configure the Streamlit page
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)


# ============================================================
# 3. CUSTOM CSS
# ============================================================

# Add our own CSS to make the application attractive
st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background-color: #f5f7fa;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Prediction result box */
    .prediction-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 25px;
        background-color: white;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }

    /* Price text */
    .price {
        font-size: 35px;
        font-weight: bold;
    }

    /* Section heading */
    .section-title {
        font-size: 24px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 4. HEADER
# ============================================================

# Display attractive title
st.markdown(
    '<div class="main-title">🏠 House Price Predictor</div>',
    unsafe_allow_html=True
)

# Display subtitle
st.markdown(
    '<div class="subtitle">'
    'Predict the estimated house sale price using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


# Add horizontal line
st.divider()


# ============================================================
# 5. HOUSE DETAILS
# ============================================================

# Section heading
st.markdown(
    '<div class="section-title">🏡 Enter House Details</div>',
    unsafe_allow_html=True
)


# Create two columns
col1, col2 = st.columns(2)


# ============================================================
# LEFT COLUMN
# ============================================================

with col1:

    # Overall quality
    overall_qual = st.slider(
        "⭐ Overall Quality",
        min_value=1,
        max_value=10,
        value=5
    )

    # Living area
    gr_liv_area = st.number_input(
        "📐 Living Area (sqft)",
        min_value=100,
        max_value=10000,
        value=1500
    )

    # Garage cars
    garage_cars = st.number_input(
        "🚗 Garage Cars",
        min_value=0,
        max_value=5,
        value=2
    )

    # Basement area
    total_bsmt_sf = st.number_input(
        "🏠 Basement Area (sqft)",
        min_value=0,
        max_value=5000,
        value=1000
    )


# ============================================================
# RIGHT COLUMN
# ============================================================

with col2:

    # Year built
    year_built = st.number_input(
        "📅 Year Built",
        min_value=1800,
        max_value=2026,
        value=2000
    )

    # Full bathrooms
    full_bath = st.number_input(
        "🛁 Full Bathrooms",
        min_value=0,
        max_value=5,
        value=2
    )

    # Bedrooms
    bedroom_abv_gr = st.number_input(
        "🛏️ Bedrooms",
        min_value=0,
        max_value=10,
        value=3
    )

    # Lot area
    lot_area = st.number_input(
        "🌳 Lot Area (sqft)",
        min_value=100,
        max_value=100000,
        value=8000
    )


# ============================================================
# 6. PREDICTION BUTTON
# ============================================================

# Create three columns to center the button
button_col1, button_col2, button_col3 = st.columns([1, 2, 1])


with button_col2:

    # Prediction button
    predict_button = st.button(
        "🔮 Predict House Price",
        use_container_width=True
    )


# ============================================================
# 7. PREDICTION
# ============================================================

# Run prediction when button is clicked
if predict_button:

    # Create DataFrame using user inputs
    new_house = pd.DataFrame({

        # Overall quality
        "OverallQual": [overall_qual],

        # Living area
        "GrLivArea": [gr_liv_area],

        # Garage cars
        "GarageCars": [garage_cars],

        # Basement area
        "TotalBsmtSF": [total_bsmt_sf],

        # Year built
        "YearBuilt": [year_built],

        # Full bathrooms
        "FullBath": [full_bath],

        # Bedrooms
        "BedroomAbvGr": [bedroom_abv_gr],

        # Lot area
        "LotArea": [lot_area]
    })


    # Make prediction using trained model
    prediction = model.predict(new_house)[0]


    # ========================================================
    # 8. DISPLAY PREDICTION
    # ========================================================

    st.markdown(
        """
        <div class="prediction-box">

        <h2>🎯 Estimated House Price</h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    # Display price using Streamlit metric
    st.metric(
        label="🏠 Predicted Sale Price",
        value=f"₹{prediction:,.2f}"
    )


    # ========================================================
    # 9. SHOW INPUT DETAILS
    # ========================================================

    st.divider()

    st.subheader("📋 House Details Used for Prediction")


    # Create a nice table
    display_data = pd.DataFrame({

        "Feature": [
            "Overall Quality",
            "Living Area",
            "Garage Cars",
            "Basement Area",
            "Year Built",
            "Full Bathrooms",
            "Bedrooms",
            "Lot Area"
        ],

        "Value": [
            overall_qual,
            f"{gr_liv_area:,} sqft",
            garage_cars,
            f"{total_bsmt_sf:,} sqft",
            year_built,
            full_bath,
            bedroom_abv_gr,
            f"{lot_area:,} sqft"
        ]
    })


    # Display the table
    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# 10. INFORMATION SECTION
# ============================================================

st.divider()

st.subheader("ℹ️ About This Application")

st.write(
    """
    This application uses a Machine Learning model based on
    Linear Regression to estimate house sale prices.

    The model uses the following features:

    • Overall Quality
    • Living Area
    • Garage Cars
    • Basement Area
    • Year Built
    • Full Bathrooms
    • Bedrooms
    • Lot Area
    """
)


# ============================================================
# 11. FOOTER
# ============================================================

st.divider()

st.caption(
    "🤖 House Price Prediction | Built with Python, "
    "Scikit-learn & Streamlit"
)

