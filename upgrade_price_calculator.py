import streamlit as st

def calculate_upgrade_price(current_plan_price, target_plan_price, extra_discount):
    difference = target_plan_price - current_plan_price
    final_price = max(difference - extra_discount, 0)
    discount_percentage = (1 - (final_price / target_plan_price)) * 100 if target_plan_price else 0
    return round(final_price, 2), round(discount_percentage, 2)

def main():
    st.set_page_config(page_title="Upgrade Price Calculator", layout="centered")
    st.title("🚀 Assisted Plan Upgrade Calculator")

    with st.expander("🛠️ Edit Plan Prices", expanded=False):
        st.markdown("Edit selling prices of each plan below:")
        col1, col2 = st.columns(2)
        with col1:
            basic_price = st.number_input("Basic", value=2359.82)
            premium_price = st.number_input("Premium", value=5356.82)
        with col2:
            elite_price = st.number_input("Elite", value=6749.82)
            luxury_price = st.number_input("Luxury", value=17699.53)

    plan_prices = {
        "Basic": basic_price,
        "Premium": premium_price,
        "Elite": elite_price,
        "Luxury": luxury_price,
    }

    st.markdown("### 📋 Select Plans")
    col1, col2 = st.columns(2)
    with col1:
        current_plan = st.selectbox("Current Plan", list(plan_prices.keys())[:-1])
    with col2:
        target_plan = st.selectbox("Target Plan", list(plan_prices.keys())[1:])

    if plan_prices[current_plan] >= plan_prices[target_plan]:
        st.error("Target plan must be of higher value than current plan.")
        return

    st.markdown("### 💰 Customer Offer & Discount")
    customer_offer = st.number_input("How much is customer ready to pay?", value=0.0)
    raw_difference = plan_prices[target_plan] - plan_prices[current_plan]
    calculated_extra_discount = raw_difference - customer_offer

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Price Difference", f"₹{raw_difference:.2f}")
    with col2:
        st.metric("Auto Discount", f"₹{max(calculated_extra_discount, 0):.2f}")

    extra_discount = st.number_input("🔧 Adjust Discount (if needed)", value=max(calculated_extra_discount, 0.0))

    final_price, discount_percentage = calculate_upgrade_price(
        plan_prices[current_plan], plan_prices[target_plan], extra_discount
    )

    st.markdown("---")
    st.markdown("### 📊 Final Summary")
    st.success(f"**Customer needs to pay:** ₹{final_price}")
    st.info(f"**Apply coupon code with {discount_percentage}% discount**")

if __name__ == \"__main__\":
    main()
