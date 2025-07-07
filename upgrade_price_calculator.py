import streamlit as st

def calculate_upgrade_price(current_plan_price, target_plan_price, extra_discount):
    difference = target_plan_price - current_plan_price
    final_price = max(difference - extra_discount, 0)
    discount_percentage = (1 - (final_price / target_plan_price)) * 100 if target_plan_price else 0
    return round(final_price, 2), round(discount_percentage, 2)

def main():
    st.set_page_config(page_title="Upgrade Price Calculator", layout="centered")
    st.title("Assisted Plan Upgrade Calculator")
    st.write("Use this tool to calculate upgrade pricing and applicable discounts.")

    with st.expander("Edit Plan Prices", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            basic_price = st.number_input("Assisted Filing Basic Plan Price", value=2359.82)
            premium_price = st.number_input("Assisted Filing Premium Plan Price", value=5356.82)
        with col2:
            elite_price = st.number_input("Assisted Filing Elite Plan Price", value=6749.82)
            luxury_price = st.number_input("Assisted Filing Luxury Plan Price", value=17699.53)

    plan_prices = {
        "Basic": basic_price,
        "Premium": premium_price,
        "Elite": elite_price,
        "Luxury": luxury_price,
    }

    st.subheader("Plan Selection")
    col1, col2 = st.columns(2)
    with col1:
        current_plan = st.selectbox("Select Current Plan", list(plan_prices.keys())[:-1])
    with col2:
        target_plan = st.selectbox("Select Target Plan", list(plan_prices.keys())[1:])

    if plan_prices[current_plan] >= plan_prices[target_plan]:
        st.error("Target plan must be of higher value than current plan.")
        return

    st.subheader("Customer Offer")
    customer_offer = st.number_input("Enter Amount Customer is Willing to Pay", value=0.0)

    raw_difference = plan_prices[target_plan] - plan_prices[current_plan]
    calculated_extra_discount = raw_difference - customer_offer if customer_offer > 0 else 0

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Price Difference", f"₹{raw_difference:.2f}")
    with col2:
        st.metric("Calculated Discount", f"₹{calculated_extra_discount:.2f}")

    extra_discount = st.number_input("Adjust Discount (Optional)", value=calculated_extra_discount)

    final_price, discount_percentage = calculate_upgrade_price(
        plan_prices[current_plan], plan_prices[target_plan], extra_discount
    )

    st.subheader("Summary")
    st.write(f"**Amount to be Paid by Customer:** ₹{final_price}")
    st.write(f"**Suggested Coupon Discount:** {discount_percentage}%")

if __name__ == "__main__":
    main()
