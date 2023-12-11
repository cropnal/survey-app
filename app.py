import streamlit as st
import pandas as pd
import os
# Tab 2: Analytics
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

                
                df_1 = pd.DataFrame(data,columns=['revenue','cost of cultivation'])
                print(df_1)
                df = data 
                # Graph: Farmers vs Cost of Cultivation
                st.subheader("Farmers vs Cost of Cultivation")
                st.area_chart(df_1)

                # Graph: Farmer vs Net Profit
                st.subheader("Farmer vs Net Profit")
                st.bar_chart(df.set_index("Farmer Name")["Net Profit"],color="#007000")

                # Graph: Farmer vs Monthly Income
                st.subheader("Farmer vs Monthly Income")
                st.bar_chart(df.set_index("Farmer Name")["monthly income"],color="#D2222D")
                                



        elif survey_type=="vegetable_survey":   
            csv_filename = f"{survey_type.lower()}_data.csv"

            data = pd.read_csv(csv_filename) 
            # Display data table
            st.subheader("Data Table")
            st.dataframe(data)

            # Display relevant graphs
            st.subheader("Data Analytics")

            # Total number of entries
            total_entries = len(data)
            st.subheader("Vegetable Sellers Analysis")

            # Calculate total vegetable sellers
            total_vegetable_sellers = total_entries

            # Calculate percentage of happy and unhappy vegetable sellers
            happy_percentage_vegetable = (data['Happiness Index'] == 'Yes').sum() / total_vegetable_sellers * 100
            unhappy_percentage_vegetable = (data['Happiness Index'] == 'No').sum() / total_vegetable_sellers * 100


            # Determine background color based on happiness percentage
            background_color_happy_vegetable = "#4CAF50"
            background_color_sad_vegetable = "#FF5733"
            background_color_total_vegetable = "#808080"  # Grey for total

            # Create labeled areas with big green or red background for vegetable sellers
            st.markdown(
                f"""
                <div style='background-color: #0000; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between;'>
                    <div style='background-color: {background_color_happy_vegetable}; padding: 10px; border-radius: 10px;'>
                        <h4 style='color: white; font-size: 20px; text-align: center;'> {happy_percentage_vegetable:.2f}%</h4>
                        <p style='color: white; text-align: center;'>Happy Vegetable Sellers</p>
                    </div>
                    <div style='background-color: {background_color_total_vegetable}; padding: 10px; border-radius: 10px;'>
                        <h4 style='color: white; font-size: 20px; text-align: center;'> {total_vegetable_sellers}</h4>
                        <p style='color: white; text-align: center;'>Total Vegetable Sellers</p>
                    </div>
                    <div style='background-color: {background_color_sad_vegetable}; padding: 10px; border-radius: 10px;'>
                        <h4 style='color: white; font-size: 20px; text-align: center;'> {unhappy_percentage_vegetable:.2f}%</h4>
                        <p style='color: white; text-align: center;'>Unhappy Vegetable Sellers</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Count occurrences of each type
            type_counts = data['Kg Sold per Day'].value_counts().reset_index()
            type_counts.columns = ['Kg Sold per Day', 'Number of People']

            # Streamlit app
            st.subheader("Vegetable seller's VS CAPACTIY")

            # Bar chart
            st.markdown("Bar Chart - Kg Sold per Day vs Number of People")
            st.bar_chart(type_counts.set_index('Kg Sold per Day'),color='#BF40BF')

            data['Net Profit'] = ((data['Selling Price']-data['Vegetable Purchase Value per KG'])*data['Kg Purchase'])-data['Spoilage Losses']-data['Transport Cost']
            data['Net Profit per kg'] = (
                    (data['Selling Price'] - data['Vegetable Purchase Value per KG']) * data['Kg Purchase'] -
                    data['Spoilage Losses'] - data['Transport Cost']
            ) / data['Kg Purchase']

            st.subheader('Age-wise Total KG Selling')
            st.write("This line chart illustrates how the total kilograms sold per day varies with the seller's age. It helps in understanding the selling trend based on age, indicating the productivity or efficiency of sellers at different age groups.")
            line_chart_data_kg_sold = data[['Age', 'Kg Sold per Day']]
            line_chart_data_kg_sold.set_index('Age', inplace=True)
            st.area_chart(line_chart_data_kg_sold)

            # Line chart: Age vs Net Profit and Age vs Net Profit per KG
            st.subheader('Age-wise Net Profit and Net Profit per KG')
            st.write("This line chart represents two trends. The first line shows the net profit for each age group, helping to identify how the overall profit changes with the seller's age. The second line represents the net profit per kilogram, indicating the bargaining skills or pricing strategies of different age groups.")
            line_chart_data_net_profit = data[['Age', 'Net Profit per kg']]
            line_chart_data_net_profit.set_index('Age', inplace=True)
            st.area_chart(line_chart_data_net_profit)


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
        st.title("Vegetable Survey")
        
        # Check if the CSV file exists
        csv_filename = "vegetable_survey_data.csv"
        file_exists = os.path.isfile(csv_filename)

        # Vegetable Information
        seller_name = st.text_input("Seller Name", "Vegetable Seller")
        vegetable_name = st.text_input("Vegetable Name", "Tomato")
        age = st.number_input("Enter Age",value=30)
        amount_purchase = st.number_input("Kg purchase", min_value=0.0, value=10.0)
        purchase_value_per_kg = st.number_input("Vegetable Purchase Value per KG", min_value=0.0, value=5.0)
        transport_cost = st.number_input("Transport Cost", min_value=0.0, value=50.0)
        spoilage_losses = st.number_input("Spoilage Losses", min_value=0.0, value=10.0)
        selling_price = st.number_input("Selling Price", min_value=0.0, value=15.0)
        
        # Purchase Information
        purchase_location = st.text_input("Purchase Location", "Local Market")

        # Happiness Index
        happiness_index = st.radio("Happy with Income?", ["Yes", "No"], index=0)

        # Additional Information
        phone_number = st.text_input("Phone Number", "")
        lower_price_preference = st.checkbox("I want vegetables at a lower price")

        # New Questions
        income_insecurity = st.radio("Are you insecure about your income source?", ["Yes", "No"], index=1)
        
        # Additional Question
        kg_sold_per_day = st.number_input("How many kilograms of vegetables/fruits do you sell in a day?", min_value=0)

        if st.button("Submit"):
            # Store data in CSV
            data = {
                "Seller Name": [seller_name],
                "Age": [age],
                "Vegetable Name": [vegetable_name],
                "Vegetable Purchase Value per KG": [purchase_value_per_kg],
                "Kg Purchase": [amount_purchase],
                "Transport Cost": [transport_cost],
                "Spoilage Losses": [spoilage_losses],
                "Selling Price": [selling_price],
                "Purchase Location": [purchase_location],
                "Happiness Index": [happiness_index],
                "Phone Number": [phone_number],
                "Lower Price Preference": [lower_price_preference],
                "Income Insecurity": [income_insecurity],
                "Kg Sold per Day": [kg_sold_per_day]
            }

            # Check if the file exists to determine whether to write the header
            mode = "w" if not file_exists else "a"

            df = pd.DataFrame(data)
            df.to_csv(csv_filename, mode=mode, header=not file_exists, index=False)

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
