import streamlit as st
import pandas as pd
import os
# Tab 2: Analytics
def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("survey_responses.csv", mode="a", header=not st.session_state.csv_file_exists, index=False)
    st.session_state.csv_file_exists = True

def main():
    st.title("Cropnal Survey")
    tabs = ["Farmer Survey","Vegetable Survey", "Admin Analytics"]
    current_tab = st.selectbox("Select Tab", tabs)

    if current_tab == "Farmer Survey":
        st.header("Farmer Survey")
        csv_filename = "farmer_survey_data.csv"
        file_exists = os.path.isfile(csv_filename)

        st.subheader("Farmer Information")
        farmer_name = st.text_input("Farmer Name", "John Doe")
        village = st.text_input("Village", "Sample Village")
        mobile = st.text_input("Mobile", "1234567890")

        st.subheader("Main Income Crops")
        crop_name = st.text_input("Crop Name", "Rice")
        crop_duration = st.number_input("Crop Duration (months)", min_value=1, step=1, value=6)
        crop_area = st.number_input("Crop Area in Bigha", min_value=0.1, step=0.1, value=5.0)
        seeds = st.number_input("Seeds", value=1000)
        fertilizer_cost = st.number_input("Fertilizer Cost", min_value=0, value=5000)
        fertilizer_type = st.text_input("Which Fertilizer", "NPK")
        pesticide_cost = st.number_input("Pesticide Cost", min_value=0, value=1000)

        st.subheader("Water Supply")
        water_supply_options = st.radio("Water Supply Options", ["Tube Well", "Canal Water"], index=0)
        water_supply_system = st.selectbox("Water Supply System", ["Randomly", "Drip Irrigation", "Fountains", "Others"], index=1)
        water_system_cost = st.number_input("Cost of Water System", min_value=0, value=2000)

        st.subheader("Labor and Yield")
        labour_cost = st.number_input("Labour Cost", min_value=0, value=3000)
        crop_yield = st.number_input("Crop Yield in KG", min_value=0, value=5000)

        st.subheader("Market Information")
        selling_market = st.text_input("Selling Market", "Local Market")
        market_price = st.number_input("Market Price", min_value=0, value=10)

        st.subheader("Challenges and Satisfaction")
        weather_issue = st.text_input("Weather Issue", "Drought")
        gov_compensation = st.checkbox("Government Compensation", value=True)
        crop_insurance = st.checkbox("Crop Insurance", value=False)
        storage_challenges = st.checkbox("Storage Challenges", value=True)

        st.subheader("Miscellaneous and Satisfaction")
        happy_with_income = st.radio("Are you happy with your current income?", ["Yes", "No"], index=0)
        farming_job_satisfaction = st.radio("Is salary farming job okay?", ["Yes", "No"], index=1)
        inspire_other_farmers = st.radio("Open to inspiring other farmers?", ["Yes", "No"], index=0)

        miscellaneous_cost = st.number_input("Miscellaneous Cost", min_value=0, value=500)
        extra_description = st.text_area("Extra Description", "No additional comments")

        if st.button("Submit"):
            # Store data in CSV
            data = {
                "Farmer Name": farmer_name,
                "Village": village,
                "Mobile": mobile,
                "Crop Name": crop_name,
                "Crop Duration (months)": crop_duration,
                "Crop Area in Bigha": crop_area,
                "Seeds": seeds,
                "Fertilizer Cost": fertilizer_cost,
                "Which Fertilizer": fertilizer_type,
                "Pesticide Cost": pesticide_cost,
                "Water Supply Options": water_supply_options,
                "Water Supply System": water_supply_system,
                "Cost of Water System": water_system_cost,
                "Labour Cost": labour_cost,
                "Crop Yield in KG": crop_yield,
                "Selling Market": selling_market,
                "Market Price per KG ": market_price,
                "Weather Issue": weather_issue,
                "Government Compensation": gov_compensation,
                "Crop Insurance": crop_insurance,
                "Storage Challenges": storage_challenges,
                "Happy with Income": happy_with_income,
                "Farming Job Satisfaction": farming_job_satisfaction,
                "Inspire Other Farmers": inspire_other_farmers,
                "Miscellaneous Cost": miscellaneous_cost,
                "Extra Description": extra_description
            }

            # Check if the file exists to determine whether to write the header
            mode = "w" if not file_exists else "a"

            df = pd.DataFrame(data, index=[0])
            df.to_csv(csv_filename, mode=mode, header=not file_exists, index=False)

            st.success("Survey submitted successfully!")
            st.toast('Data Saved', icon='😍')

    elif current_tab == "Admin Analytics":
        st.header("Admin Analytics")

        # Choose survey type
        survey_type = st.selectbox("Select Survey Type", ["farmer_survey", "vegetable_survey"])

        

        

        
        if survey_type=="farmer_survey":
            csv_filename = f"{survey_type.lower()}_data.csv"
            data = pd.read_csv(csv_filename) 
            # Display data table
            st.subheader("Data Table")
            st.dataframe(data)

            # Display relevant graphs
            st.subheader("Data Analytics")

            # Total number of entries
            total_entries = len(data)
            if 'Happy with Income' in data.columns:
                st.subheader("Farmers Happiness Distribution")

                # Calculate percentage of happy and unhappy farmers
                happy_percentage = (data['Happy with Income'] == 'Yes').sum() / total_entries * 100
                unhappy_percentage = (data['Happy with Income'] == 'No').sum() / total_entries * 100

                # Determine background color based on happiness percentage
                background_color_happy = "#4CAF50"
                background_color_sad = "#FF5733"
                background_color_total = "#808080"  # Grey for total

                # Create labeled areas with big green or red background
                st.markdown(
                    f"""
                    <div style='background-color: #0000; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between;'>
                        <div style='background-color: {background_color_happy}; padding: 10px; border-radius: 10px;'>
                            <h4 style='color: white; font-size: 20px; text-align: center;'> {happy_percentage:.2f}%</h4>
                            <p style='color: white; text-align: center;'>Happy Farmers</p>
                        </div>
                        <div style='background-color: {background_color_total}; padding: 10px; border-radius: 10px;'>
                            <h4 style='color: white; font-size: 20px; text-align: center;'> {total_entries}</h4>
                            <p style='color: white; text-align: center;'>Total Farmers</p>
                        </div>
                        <div style='background-color: {background_color_sad}; padding: 10px; border-radius: 10px;'>
                            <h4 style='color: white; font-size: 20px; text-align: center;'> {unhappy_percentage:.2f}%</h4>
                            <p style='color: white; text-align: center;'>Unhappy Farmers</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                data.fillna(0, inplace=True)
                data["Seeds"] = pd.to_numeric(data["Seeds"], errors='coerce')
                data["Fertilizer Cost"] = pd.to_numeric(data["Fertilizer Cost"], errors='coerce')
                data["Pesticide Cost"] = pd.to_numeric(data["Pesticide Cost"], errors='coerce')
                data["Cost of Water System"] = pd.to_numeric(data["Cost of Water System"], errors='coerce')
                data["Labour Cost"] = pd.to_numeric(data["Labour Cost"], errors='coerce')
                data["Miscellaneous Cost"] = pd.to_numeric(data["Miscellaneous Cost"], errors='coerce')

                data['cost of cultivation'] = data["Seeds"]+ data["Fertilizer Cost"]+ data["Pesticide Cost"]+ data["Cost of Water System"]+ data["Labour Cost"]+ data["Miscellaneous Cost"]


                data['revenue'] = data["Crop Yield in KG"] * data["Market Price"]
                # Calculate net profit
                data['Net Profit'] = data['revenue'] - data['cost of cultivation']

                # Calculate monthly income
                data['monthly income'] = data['Net Profit'] / data["Crop Duration (months)"]

                data['percentage_profit'] = 100*(data['Net Profit']/data['revenue'])
                df_1 = pd.DataFrame(data,columns=['revenue','cost of cultivation'])
                
                print(df_1)
                df = data 
                # Graph: Farmers vs Cost of Cultivation
                st.subheader("Farmers vs Cost of Cultivation")
                st.write("Visualizing farmers' cost of cultivation trends, net profits, and monthly incomes through area and bar charts aids in understanding financial aspects, enabling informed decision-making for sustainable agriculture.")
                st.area_chart(df_1)

                # Graph: Farmer vs percentage Net Profit
                st.subheader("Farmer vs Percentage Profit")
                st.bar_chart(df.set_index("Farmer Name")["percentage_profit"],color="#009000")

                # Graph: Farmer vs Monthly Income
                st.subheader("Farmer vs Monthly Income")
                st.bar_chart(df.set_index("Farmer Name")["monthly income"],color="#D2222D")
                                



        elif survey_type=="vegetable_survey":   

            csv_filename = "survey_responses.csv"
            st.header("Analytics")

            # Load survey responses from CSV
            data = pd.read_csv("survey_responses.csv")
            st.table(data)

            
            total_entries = len(data)
            if 'Ready to Purchase at Low Prices' in data.columns:
                st.subheader("Ready to Purchase at Low Prices")

                # Calculate percentage of happy and unhappy farmers
                happy_percentage = (data['Ready to Purchase at Low Prices'] == 'Yes').sum() / total_entries * 100
                unhappy_percentage = (data['Ready to Purchase at Low Prices'] == 'No').sum() / total_entries * 100

                # Determine background color based on happiness percentage
                background_color_happy = "#4CAF50"
                background_color_sad = "#FF5733"
                background_color_total = "#808080"  # Grey for total

                # Create labeled areas with big green or red background
                st.markdown(
                    f"""
                    <div style='background-color: #0000; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between;'>
                        <div style='background-color: {background_color_happy}; padding: 10px; border-radius: 10px;'>
                            <h4 style='color: white; font-size: 20px; text-align: center;'> {happy_percentage:.2f}%</h4>
                            <p style='color: white; text-align: center;'>Low Price Purchaser</p>
                        </div>
                        <div style='background-color: {background_color_total}; padding: 10px; border-radius: 10px;'>
                            <h4 style='color: white; font-size: 20px; text-align: center;'> {total_entries}</h4>
                            <p style='color: white; text-align: center;'>Total Survey Entries</p>
                        </div>
                        <div style='background-color: {background_color_sad}; padding: 10px; border-radius: 10px;'>
                            <h4 style='color: white; font-size: 20px; text-align: center;'> {unhappy_percentage:.2f}%</h4>
                            <p style='color: white; text-align: center;'>Dont Care</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            if 'Fair Prices to Purchase' in data.columns:
                st.subheader("Fair Prices to Purchase ?")

                # Calculate percentage of happy and unhappy farmers
                happy_percentage = (data['Fair Prices to Purchase'] == 'Yes').sum() / total_entries * 100
                unhappy_percentage = (data['Fair Prices to Purchase'] == 'No').sum() / total_entries * 100

                # Determine background color based on happiness percentage
                background_color_happy = "#4CAF50"
                background_color_sad = "#FF5733"
                background_color_total = "#808080"  # Grey for total

                # Create labeled areas with big green or red background
                st.markdown(
                    f"""
                    <div style='background-color: #0000; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between;'>
                        <div style='background-color: {background_color_happy}; padding: 10px; border-radius: 10px;'>
                            <h4 style='color: white; font-size: 20px; text-align: center;'> {happy_percentage:.2f}%</h4>
                            <p style='color: white; text-align: center;'>Fair Prices</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"""
<div style='background-color: #0000; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between;'>
                        <div style='background-color: {background_color_sad}; padding: 10px; border-radius: 10px;'>
                            <h4 style='color: white; font-size: 20px; text-align: center;'> {unhappy_percentage:.2f}%</h4>
                            <p style='color: white; text-align: center;'>Fair Prices</p>
                    </div>
                    """,unsafe_allow_html=True
                )

                selected_restaurant = st.text_input("Enter Restaurant Name:")
                if selected_restaurant:
                    fetched_rows_data = data[data["Shop Name"].str.lower() == selected_restaurant.lower()]
                    st.write(fetched_rows_data)
                    if not fetched_rows_data.empty:
                        # Display total kilograms supplied with expiry time
                        st.subheader(f"Total Kilograms Supplied by {selected_restaurant}:")
                        total_kg = fetched_rows_data["Weight (kg)"].sum()
                        st.header(f"Total Kilograms: {total_kg}")
                        rows_kg = fetched_rows_data[["Name of Vegetable/Fruit/Grain/Nuts","Weight (kg)"]]
                        # Bar plot for "Name of Vegetable/Fruit/Grain/Nuts" vs "Weight (kg)"
                        st.subheader(f"Bar Plot for {selected_restaurant}:")
                        st.write(rows_kg)
                        st.area_chart(rows_kg.set_index("Name of Vegetable/Fruit/Grain/Nuts"))



                    else:
                        st.warning(f"No data found for the restaurant: {selected_restaurant}")


            

            


        elif survey_type == "trader_survey":
            st.error("PENDING !!")
            csv_filename = f"{survey_type.lower()}_data.csv"

            data = pd.read_csv(csv_filename)
            # Display data table
            st.subheader("Data Table")
            st.dataframe(data)

            # Display relevant graphs
            st.subheader("Data Analytics")

            # Total number of entries
            total_entries_trader = len(data)
            st.subheader("Trader Analysis")

            # Calculate total traders
            total_traders = total_entries_trader

            # Calculate percentage of happy and unhappy traders
            happy_percentage_trader = (data['Happiness Index'] == 'Yes').sum() / total_traders * 100
            unhappy_percentage_trader = (data['Happiness Index'] == 'No').sum() / total_traders * 100

            # Determine background color based on happiness percentage for traders
            background_color_happy_trader = "#4CAF50"
            background_color_sad_trader = "#FF5733"
            background_color_total_trader = "#808080"  # Grey for total

            # Create labeled areas with big green or red background for traders
            st.markdown(
                f"""
                <div style='background-color: #0000; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between;'>
                    <div style='background-color: {background_color_happy_trader}; padding: 10px; border-radius: 10px;'>
                        <h4 style='color: white; font-size: 20px; text-align: center;'> {happy_percentage_trader:.2f}%</h4>
                        <p style='color: white; text-align: center;'>Happy Traders</p>
                    </div>
                    <div style='background-color: {background_color_total_trader}; padding: 10px; border-radius: 10px;'>
                        <h4 style='color: white; font-size: 20px; text-align: center;'> {total_traders}</h4>
                        <p style='color: white; text-align: center;'>Total Traders</p>
                    </div>
                    <div style='background-color: {background_color_sad_trader}; padding: 10px; border-radius: 10px;'>
                        <h4 style='color: white; font-size: 20px; text-align: center;'> {unhappy_percentage_trader:.2f}%</h4>
                        <p style='color: white; text-align: center;'>Unhappy Traders</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )







    elif current_tab == "Vegetable Survey":
        file_exists = os.path.isfile("survey_responses.csv")
        if "csv_file_exists" not in st.session_state:
                st.session_state.csv_file_exists = False

        st.header("Participant Information")
        name = st.text_input("Name", value="John Doe")
        phone_number = st.number_input("Phone Number", value=1234567890, format="%d")
        shop_name = st.text_input("Shop Name", value="Doe Mart")
        location_area = st.text_input("Location (Area)", value="Sample Area")
        location_city = st.text_input("Location (City)", value="Sample City")
        shop_type_options = ["Large Restaurants", "Food Chains", "Food Lari", "FastFood Shop",
                             "Food Processor Plant", "Vegetable Lari", "Vegetable Store"]
        shop_type = st.selectbox("Type of Shop/Lari", shop_type_options, index=2)
        main_product = st.text_input("Main Product", value="Vegetables")

        # Supply Information
        st.header("Supply Information")
        veg_name = st.text_input("Name of Vegetable/Fruit/Grain/Nuts", value="Tomatoes")
        category_options = ["Vegetable", "Fruit", "Grain", "Nuts"]
        category = st.selectbox("Category", category_options, index=0)
        weight = st.number_input("Weight (kg)", value=10, format="%d")
        price_per_kg = st.number_input("Price per KG", value=50.0)
        transport_cost = st.number_input("Transport Cost", value=10.0)
        source_of_supply = st.text_input("Source of Supply", value="Local Farms")
        expiry_time = st.number_input("Expiry Time (days)", value=7, format="%d")
        fair_prices = st.radio("Is this fair prices to purchase for them?", ["Yes", "No"], index=0)
        ready_to_purchase = st.radio("Are they ready to purchase at low prices?", ["Yes", "No"], index=0)
        if ready_to_purchase == "Yes":
            expected_low_prices = st.number_input("Expected Low Prices", value=40, format="%d")

        # Display submitted information
        if st.button("Submit"):
            st.subheader("Submitted Information:")
            # Save to CSV
            data = {
                "Name": [name],
                "Phone Number": [phone_number],
                "Shop Name": [shop_name],
                "Location (Area)": [location_area],
                "Location (City)": [location_city],
                "Type of Shop/Lari": [shop_type],
                "Main Product": [main_product],
                "Name of Vegetable/Fruit/Grain/Nuts": [veg_name],
                "Category": [category],
                "Weight (kg)": [weight],
                "Price per KG": [price_per_kg],
                "Transport Cost": [transport_cost],
                "Source of Supply": [source_of_supply],
                "Expiry Time (days)": [expiry_time],
                "Fair Prices to Purchase": [fair_prices],
                "Ready to Purchase at Low Prices": [ready_to_purchase],
                "Expected Low Prices": [expected_low_prices] if ready_to_purchase == "Yes" else [None],
            }

            # Check if the file exists to determine whether to write the header
            mode = "w" if not file_exists else "a"

            df = pd.DataFrame(data)
            df.to_csv("survey_responses.csv", mode=mode, header=not file_exists, index=False)

            st.success("Survey submitted successfully!")
            st.toast("Data successfully added!")



                    
    elif current_tab=="Trader Wholesaler Survey":

        st.header("PENDING : Trader Wholesaler Survey Form")

        # Wholesaler Information
        name = st.text_input("Name", "John Doe")
        date = st.date_input("Date", pd.to_datetime("today"))
        address = st.text_area("Address", "Sample Address")
        contact_number = st.text_input("Contact Number", "1234567890")

        # Market Access
        st.subheader("Market Access")
        expanding_to_new_markets = st.radio("Expanding to new markets?", ["Yes", "No"], index=0)
        current_market_access_challenges = st.text_area("Current market accessibility challenges", "Limited market reach")

        # Product Range
        st.subheader("Product Range")
        products_interested_in = st.text_input("Types of products you are interested in purchasing", "Fresh produce")

        # Product Quality
        st.subheader("Product Quality")
        product_quality_importance = st.slider("Importance of product quality (1-10)", min_value=1, max_value=10, value=8)

        # Supplier Relationships
        st.subheader("Supplier Relationships")
        supplier_relationships_importance = st.slider("Importance of good supplier relationships (1-10)", min_value=1, max_value=10, value=9)

        # Order Quantity
        st.subheader("Order Quantity")
        preferred_order_quantity = st.number_input("Preferred order quantity (in units)", min_value=1, value=100)

        # Delivery Preferences
        st.subheader("Delivery Preferences")
        preferred_delivery_frequency = st.text_input("Preferred delivery frequency (e.g., daily, weekly)", "Weekly")

        # Payment Terms
        st.subheader("Payment Terms")
        preferred_payment_terms = st.text_input("Preferred payment terms (e.g., credit period)", "Net 30 days")

        # Market Trends
        st.subheader("Market Trends")
        awareness_of_current_market_trends = st.radio("Awareness of current market trends?", ["Yes", "No"], index=1)
        willingness_to_adapt_to_new_trends = st.radio("Willingness to adapt to new market trends?", ["Yes", "No"], index=0)

        # Sustainability
        st.subheader("Sustainability")
        importance_of_sustainability = st.slider("Importance of sustainable farming practices (1-10)", min_value=1, max_value=10, value=7)

        # Feedback
        st.subheader("Feedback")
        feedback_suggestions = st.text_area("Any specific feedback or suggestions for improvement?", "Overall good experience")

        if st.button("Submit"):
            # Store data in CSV
            data = {
                "Name": [name],
                "Date": [date],
                "Address": [address],
                "Contact Number": [contact_number],
                "Expanding to New Markets": [expanding_to_new_markets],
                "Current Market Access Challenges": [current_market_access_challenges],
                "Products Interested In": [products_interested_in],
                "Product Quality Importance": [product_quality_importance],
                "Supplier Relationships Importance": [supplier_relationships_importance],
                "Preferred Order Quantity": [preferred_order_quantity],
                "Preferred Delivery Frequency": [preferred_delivery_frequency],
                "Preferred Payment Terms": [preferred_payment_terms],
                "Awareness of Current Market Trends": [awareness_of_current_market_trends],
                "Willingness to Adapt to New Trends": [willingness_to_adapt_to_new_trends],
                "Importance of Sustainability": [importance_of_sustainability],
                "Feedback and Suggestions": [feedback_suggestions],
            }

            df = pd.DataFrame(data)
            df.to_csv("trader_survey_data.csv", mode="a", header=not st.file_uploader("trader_wholesaler_survey_data.csv"))

            st.success("Survey submitted successfully!")
            st.toast("Data successfully added!")


                



    

            


        
    


if __name__ == "__main__":
    main()
