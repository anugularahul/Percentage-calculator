import streamlit as st

def calculate_upgrade_price(current_plan_price, target_plan_price, extra_discount):
    difference = target_plan_price - current_plan_price
    final_price = max(difference - extra_discount, 0)  # prevent negative values
    discount_percentage = (1 - (final_price / target_plan_price)) * 100 if target_plan_price else 0
    return round(final_price, 2), round(discount_percentage, 2)

def main():
    st.title("ClearTax Plan Upgrade Calculator")

    st.header("Plan Selling Prices (Editable)")
    basic_price = st.number_input("Assisted Filing Basic Plan Price", value=2359.82)
    premium_price = st.number_input("Assisted Filing Premium Plan Price", value=5356.82)
    elite_price = st.number_input("Assisted Filing Elite Plan Price", value=6749.82)
    luxury_price = st.number_input("Assisted Filing Luxury Plan Price", value=17699.53)

    st.header("Upgrade Details")
    current_plan = st.selectbox("Current Plan", ["Basic", "Premium", "Elite"])
    target_plan = st.selectbox("Target Plan", ["Premium", "Elite", "Luxury"])

    plan_prices = {
        "Basic": basic_price,
        "Premium": premium_price,
        "Elite": elite_price,
        "Luxury": luxury_price,
    }

    if plan_prices[current_plan] >= plan_prices[target_plan]:
        st.error("Target plan must be of higher value than current plan.")
        return

    st.subheader("Customer Offer Handling")
    customer_offer = st.number_input("Amount Customer is Ready to Pay (₹)", value=0.0)

    # Calculate required discount if customer_offer is provided
    raw_difference = plan_prices[target_plan] - plan_prices[current_plan]
    calculated_extra_discount = raw_difference - customer_offer

    # Show auto-updated additional discount
    st.write(f"Calculated Additional Discount: ₹{max(calculated_extra_discount, 0):.2f}")

    # Allow user to manually adjust additional discount (if needed)
    extra_discount = st.number_input("Override Additional Discount (₹)", value=max(calculated_extra_discount, 0.0))

    final_price, discount_percentage = calculate_upgrade_price(
        plan_prices[current_plan], plan_prices[target_plan], extra_discount
    )

    st.success(f"Amount to be paid by customer: ₹{final_price}")
    st.info(f"Generate coupon code with discount: {discount_percentage}%")

if __name__ == "__main__":
    main()
